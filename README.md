# NimbusHR RevOps Dashboard & Churn Prediction

An end-to-end Revenue Operations (RevOps) analytics project simulating a 
SaaS company's sales funnel, churn patterns, and revenue attribution.  
Built to showcase SQL, Python, Tableau, and automation skills in a 
real-world business context.

📄 **Case Study:** [View full project write-up](docs/case_study.md)

---

## 📌 Project Overview
NimbusHR is a fictional B2B SaaS HR software provider.  
This project models how a RevOps Analyst or GTM Analytics Engineer would:
1. Consolidate data from CRM, subscription, and marketing sources.
2. Build dashboards for sales/marketing performance.
3. Predict churn risk for customer retention strategy.

---

## 🛠️ Tech Stack
- **SQL** — data extraction, joins, aggregations
- **Python** — pandas for prep, scikit-learn for churn prediction
- **Tableau** — dashboarding & storytelling
- **SQLite** — lightweight relational database for simulation
- **Git/GitHub** — version control & project presentation

---

## 📊 Features & Deliverables

### 1. Funnel & Revenue Dashboard
- **Visualization:** Leads → MQL → SQL → Closed Won  
- **KPIs:** Conversion rates, revenue by segment, deal velocity  
- **SQL:** Aggregated CRM + marketing campaign data

### 2. Churn Analysis
- **Visualization:** Cohort retention chart in Tableau  
- **SQL:** Joins subscription and churn tables to calculate churn rates  
- **KPIs:**  
  - Monthly churn rate  
  - Lifetime Value (LTV)  
  - Payback period  

### 3. Churn Prediction (Python)
A logistic regression model using:
- **Inputs:** Contract type, tenure, monthly charges, support tickets  
- **Output:** Probability of churn (0–1)  
- **Tech:** pandas for cleaning and scikit-learn for modeling

---

## 📂 Project Structure
nimbushr-revops-dashboard/  
│  
├── data/                  # Database & raw data  
│   └── nimbushr_revops.db  
│  
├── sql/                   # SQL queries  
│   └── revops_queries.sql  
│  
├── python/                # Python scripts  
│   └── churn_model.py  
│  
├── docs/                  # Optional case studies, screenshots  
│  
└── README.md              # Project overview  

---

## 🚀 How to Run Locally

**1️⃣ Clone the repo**  
`git clone https://github.com/romanlicursi/nimbushr-revops-dashboard.git`  
`cd nimbushr-revops-dashboard`  

**2️⃣ Install Python dependencies**  
`pip install pandas scikit-learn`  

**3️⃣ Explore the SQL**  
`sqlite3 data/nimbushr_revops.db`  
`.read sql/revops_queries.sql`  

**4️⃣ Run churn prediction**  
`python python/churn_model.py`  

---

## 💡 Business Impact Framing
If this were a real SaaS company:
- **Retention Strategy:** Target high-risk customers from churn model with 
retention campaigns.
- **Marketing Efficiency:** Cut spend on low-ROI campaigns; double down on 
high CAC payback.
- **Revenue Growth:** Improve upsell targeting by combining churn risk + 
usage metrics.

---

## 📸 Screenshots & Visuals
*To be added after Tableau dashboard is published on Tableau Public.*

---

## 📬 Contact
Built by **Roman Licursi** — 
[LinkedIn](https://www.linkedin.com/in/romanlicursi) | 
[GitHub](https://github.com/romanlicursi)

