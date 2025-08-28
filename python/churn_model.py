# churn_model.py
# Purpose: Train a simple churn-risk model and write scores back to SQLite as 'subscriptions_scored'.
# Usage:   python3 python/churn_model.py data/nimbushr_revops.db
# Reqs:    pandas, numpy, scikit-learn

import sys
import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd


def main(db_path="nimbushr_revops.db"):
    # --- Resolve repo-rooted folders regardless of where we run from ---
    ROOT = Path(__file__).resolve().parents[1]          # repo root (since this file is in /python)
    OUTPUTS = ROOT / "outputs"
    DOCS = ROOT / "docs"
    OUTPUTS.mkdir(exist_ok=True)
    DOCS.mkdir(exist_ok=True)

    # --- Open DB ---
    conn = sqlite3.connect(db_path)

    # --- Load tables ---
    subs = pd.read_sql_query("SELECT * FROM subscriptions", conn)
    leads = pd.read_sql_query("SELECT lead_id, lead_source FROM leads", conn)

    # --- Join features (left join on lead_id) ---
    df = subs.merge(leads, on="lead_id", how="left")

    # --- Feature selection (only keep columns that exist) ---
    target = "churned"
    expected_feats = [
        "monthly_revenue",
        "tenure_months",
        "contract_type",
        "payment_method",
        "lead_source",
    ]
    available_feats = [c for c in expected_feats if c in df.columns]

    if target not in df.columns:
        raise ValueError(
            f"Target column '{target}' not found. Available columns: {list(df.columns)}"
        )
    if not available_feats:
        raise ValueError(
            f"No expected feature columns found. Looked for: {expected_feats}. "
            f"Available: {list(df.columns)}"
        )

    # --- Prepare X / y ---
    y = df[target].astype(int)
    X = pd.get_dummies(df[available_feats], drop_first=True)

    # Basic sanity: need at least 2 classes
    if y.nunique() < 2:
        raise ValueError("Target 'churned' needs at least two classes (0/1) to train.")

    # --- Train / test split ---
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    # --- Model ---
    from sklearn.linear_model import LogisticRegression

    model = LogisticRegression(max_iter=1000, solver="liblinear")
    model.fit(X_train, y_train)

    # --- Model evaluation ---
    from sklearn.metrics import roc_auc_score, accuracy_score

    y_prob = model.predict_proba(X_test)[:, 1]
    y_pred = (y_prob >= 0.5).astype(int)
    auc = roc_auc_score(y_test, y_prob)
    acc = accuracy_score(y_test, y_pred)
    print(f"AUC: {auc:.3f}  |  Accuracy: {acc:.3f}")

    # --- Model drivers (coefficients) ---
    feature_names = X.columns
    coefs = pd.Series(model.coef_[0], index=feature_names)
    drivers = coefs.sort_values(key=lambda s: s.abs(), ascending=False).round(4)

    drivers_df = drivers.reset_index()
    drivers_df.columns = ["feature", "coefficient"]
    drivers_df.to_csv(DOCS / "model_coefficients.csv", index=False)

    with open(DOCS / "model_readout.md", "w") as f:
        f.write("# Model Drivers (Logistic Regression)\n\n")
        f.write("Higher positive = higher churn risk; negative = lower churn risk.\n\n")
        f.write("## Top signals by absolute impact\n")
        f.write("```\n" + drivers.head(15).to_string() + "\n```\n")

    # --- Score all rows using the full feature matrix ---
    y_all = model.predict_proba(X)[:, 1]

    # Align scores back to original subscriptions rows by position
    # (df rows still correspond one-to-one with subs after the left merge)
    scored = subs.copy().reset_index(drop=True)
    scored["churn_risk_score"] = y_all

    # --- Write outputs ---
    # 1) Back to SQLite
    scored.to_sql("subscriptions_scored", conn, if_exists="replace", index=False)

    # 2) CSV for Tableau
    scored_csv_path = OUTPUTS / "subscriptions_scored.csv"
    scored.to_csv(scored_csv_path, index=False)

    conn.close()
    print(
        f"Wrote table 'subscriptions_scored' to SQLite and '{scored_csv_path}' to disk."
    )


if __name__ == "__main__":
    db_path = sys.argv[1] if len(sys.argv) > 1 else "nimbushr_revops.db"
    main(db_path)
