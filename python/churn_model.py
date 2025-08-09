# churn_model.py
# Purpose: Train a simple churn-risk model and write scores back to SQLite as 'subscriptions_scored'.
# Usage: python churn_model.py [optional_path_to_db]
# Requirements: pandas, scikit-learn, numpy, sqlite3

import sys
import sqlite3
import pandas as pd
import numpy as np

def main(db_path="nimbushr_revops.db"):
    conn = sqlite3.connect(db_path)

    # Load tables
    subs = pd.read_sql_query("SELECT * FROM subscriptions", conn)
    leads = pd.read_sql_query("SELECT lead_id, lead_source FROM leads", conn)

    # Join features
    df = subs.merge(leads, on="lead_id", how="left")

    # Basic feature set
    features = ["monthly_revenue", "tenure_months", "contract_type", "payment_method", "lead_source"]
    target = "churned"

    # One-hot encode categoricals
    X = pd.get_dummies(df[features], drop_first=True)
    y = df[target].astype(int)

    # Train/test split
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

    # Model
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression(max_iter=1000, solver="liblinear")
    model.fit(X_train, y_train)

    # Evaluate quickly
    from sklearn.metrics import roc_auc_score, accuracy_score
    y_prob = model.predict_proba(X_test)[:,1]
    y_pred = (y_prob >= 0.5).astype(int)
    auc = roc_auc_score(y_test, y_prob)
    acc = accuracy_score(y_test, y_pred)
    print(f"AUC: {auc:.3f}  |  Accuracy: {acc:.3f}")

    # Score all rows
    df["churn_risk_score"] = model.predict_proba(X)[:,1]

    # Write back as a new table
    # Keep original columns + risk score
    out_cols = [c for c in subs.columns] + ["churn_risk_score"]
    scored = df[out_cols].copy()
    scored.to_sql("subscriptions_scored", conn, if_exists="replace", index=False)

    # Also export CSV for convenience
    scored.to_csv("subscriptions_scored.csv", index=False)
    conn.close()
    print("Wrote table 'subscriptions_scored' to SQLite and 'subscriptions_scored.csv' to disk.")

if __name__ == '__main__':
    db_path = sys.argv[1] if len(sys.argv) > 1 else "nimbushr_revops.db"
    main(db_path)
