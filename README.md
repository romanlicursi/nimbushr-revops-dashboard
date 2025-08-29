# NimbusHR RevOps Dashboard & Churn Prediction

📊 **Live Dashboard on Tableau Public:** [View Here](https://public.tableau.com/views/RealNimbus/Dashboard1?:language=en-US&publish=yes&:sid=&:display_count=n&:origin=viz_share_link)  
📄 **Case Study:** [View full project write-up](docs/case_study.md)

🧠 Summary KPI: This dashboard analyzes funnel conversion, churn risk, CAC, and payback period for a fictional SaaS company. It identifies drop-off points and flags 15% of customers as high-churn risk based on a logistic regression model.

---

## 📌 Project Overview
NimbusHR is a fictional B2B SaaS HR software provider.  
This project simulates how a RevOps Analyst or GTM Analytics Engineer would combine **SQL, Python, and Tableau** to track funnel performance, customer acquisition efficiency, retention, and churn risk.

---

## 📊 Key Insights
- **CAC per Customer:** Avg ≈ **$1,015**; Payback ≈ **3.3 months**  
- **By Source:** Organic & Email efficient; LinkedIn costly + slow payback  
- **Trend:** CAC spiked in **Aug (~$1.4k)** after mid-year surge; earlier months steady at ~$850–$920  
- **Retention:** Early cohorts (Feb–Mar) retained >45% at 3 months; later cohorts <15% by 3 months and near 0% by 6 months  
- **Churn Risk:** ~15% of customers flagged ≥60% churn probability. High-risk customers often show **low tenure + monthly/credit card contracts**  

---

## 🛠️ Tech Stack
- **SQL** → Funnel conversion, CAC by source, churn summaries, LTV, payback (`sql/revops_queries.sql`)  
- **Python** → Logistic regression churn model (`python/churn_model.py`)  
  - Outputs: `outputs/subscriptions_scored.csv`  
  - Model drivers: `docs/model_coefficients.csv`, `docs/model_readout.md`  
- **Tableau** → Interactive dashboard (Funnel, CAC, Payback, Retention, Churn Risk)  
- **SQLite** → Lightweight relational DB (`data/nimbushr_revops.db`)  
- **Git/GitHub** → Version control & portfolio presentation  

---

## 📂 Repository Structure
```
nimbushr-revops-dashboard/
├── data/          # SQLite DB + raw CSVs
├── sql/           # SQL queries
├── python/        # Churn model script
├── outputs/       # Model outputs (subscriptions_scored.csv)
├── docs/          # Case study, drivers, screenshots
├── dashboard/     # Tableau packaged workbook (.twbx)
└── README.md
```

---

## 🚀 How to Run Locally

```bash
# 1. Clone
git clone https://github.com/romanlicursi/nimbushr-revops-dashboard.git
cd nimbushr-revops-dashboard

# 2. Install Python deps
pip install -r requirements.txt

# 3. Explore SQL
sqlite3 data/nimbushr_revops.db
.read sql/revops_queries.sql

# 4. Run churn model
python3 python/churn_model.py data/nimbushr_revops.db
```

---

## 📈 Model Performance

**Logistic Regression**
- **AUC = 0.793
- **Accuracy = 0.794 

**Top churn drivers:**
- Outbound SDR Outreach (–) and Tenure (–) → lower churn risk
- Paid Search (+), Monthly Contracts (+), Credit Card (+) → higher churn risk

---

## 📸 Dashboard Preview

*Interactive dashboard available on [Tableau Public](https://public.tableau.com/views/RealNimbus/Dashboard1?:language=en-US&publish=yes&:sid=&:display_count=n&:origin=viz_share_link)*

---

## 💡 Business Impact (Simulated)

If implemented at a real SaaS company, this workflow would:
- Improve funnel conversion visibility (MQL → SQL drop-offs)
- Reallocate spend away from high-CAC, long payback channels (LinkedIn)
- Prioritize retention campaigns for high-risk accounts flagged by the model
- Provide exec team a single source of truth for GTM performance

---

👤 Built by Roman Licursi — [LinkedIn](www.linkedin.com/in/roman-licursi-3aab2a160) | [GitHub](https://github.com/romanlicursi)
