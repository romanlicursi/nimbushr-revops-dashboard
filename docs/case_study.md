# NimbusHR RevOps Dashboard – Case Study

## 1. Business Context
NimbusHR is a fictional B2B SaaS company providing HR software for 
mid-sized businesses.  
As the company scaled, leadership needed **clear visibility into their 
sales funnel, churn trends, and marketing ROI** to make data-driven 
decisions.

**Key Business Questions:**
1. Where are leads dropping off in the funnel?
2. Which customer segments are most at risk of churn?
3. Are marketing campaigns generating a positive return on spend?

---

## 2. Objective
Design an **end-to-end RevOps analytics workflow** that:
- Consolidates CRM, subscription, and marketing data into one source of 
truth.
- Visualizes KPIs in a self-serve dashboard.
- Predicts churn risk for proactive retention strategies.

---

## 3. Solution Overview
This project was built as a **simulation of a real RevOps/GTM Analytics 
role**, covering:
1. **Data Engineering:**  
   - SQL queries to join CRM, subscription, and campaign tables.  
   - Aggregations for funnel conversion rates, LTV, CAC payback.
2. **Data Science (Light AI):**  
   - Python + scikit-learn logistic regression model for churn prediction.  
   - Features: contract type, tenure, monthly spend, support tickets.
3. **Data Visualization:**  
   - Tableau dashboards for sales funnel, churn cohorts, and campaign ROI.  
   - Interactive filters for segment, channel, and time period.

---

## 4. Results (Simulated Metrics)
- **Funnel Optimization:** Identified a 42% drop-off from MQL → SQL, 
prompting SDR outreach process review.
- **Churn Prediction:** Model achieved 91% accuracy on test data, flagging 
18% of customers as high-risk.
- **Marketing ROI:** Revealed one campaign with a CAC payback of 18 months 
vs. company target of <12 months.

---

## 5. Technical Highlights
- **SQL:** Complex joins, GROUP BY aggregations, CTEs for funnel stage 
rollups.
- **Python:** pandas for cleaning, scikit-learn for model training and 
evaluation.
- **Tableau:** Multi-page dashboard with funnel visualization, cohort 
retention curves, and ROI charts.
- **Automation-Ready:** Workflow could integrate with HubSpot API to push 
churn risk scores back into CRM.

---

## 6. Business Impact
If implemented at a real SaaS company, this dashboard and churn model 
would:
- Improve **retention** by targeting at-risk customers before they churn.
- Increase **revenue efficiency** by reallocating budget from low-ROI 
campaigns.
- Provide **executive visibility** into GTM performance via a single 
source of truth.

---

## 7. Next Steps (If This Were Live)
1. Integrate with live CRM and billing data.
2. Automate churn risk score updates via API.
3. Run A/B tests on retention campaigns informed by the model.

---

## 8. Links & Assets
- **Tableau Public Dashboard:** _[Link to be added]_  
- **GitHub Repository:** [NimbusHR RevOps 
Dashboard](https://github.com/romanlicursi/nimbushr-revops-dashboard)  
- **Loom Walkthrough Video:** _[Link to be added]_  

---

## 9. Author
**Roman Licursi**  
[LinkedIn](https://www.linkedin.com/in/romanlicursi) | 
[GitHub](https://github.com/romanlicursi)

