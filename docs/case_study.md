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
- Consolidates CRM, subscription, and marketing data into one source of truth.
- Visualizes KPIs in a self-serve dashboard.
- Predicts churn risk for proactive retention strategies.

---

## 3. Solution Overview
This project was built as a **simulation of a real RevOps/GTM Analytics role**, covering:

1. **Data Engineering (SQL):**  
   - Joins across CRM, subscription, and campaign tables.  
   - Aggregations for funnel conversion rates, CAC, payback, LTV.  

2. **Data Science (Python):**  
   - Logistic regression churn model using:  
     `monthly_revenue`, `tenure_months`, `contract_type`, `payment_method`, `lead_source`.  
   - Outputs churn risk probabilities and interpretable model drivers.  

3. **Data Visualization (Tableau):**  
   - Single-page dashboard with: Funnel, CAC & Payback KPIs, CAC Trend, Cohort Retention, and Churn Risk Distribution + High-Risk Accounts.  
   - Captions for business context and recruiter readability.

---

## 4. Results (Current Metrics)
- **CAC per Customer:** Avg ≈ **$1,015**; Payback ≈ **3.3 months**.  
- **By Source:** Organic & Email efficient; LinkedIn high CAC + long payback.  
- **Trend:** CAC spiked in **Aug (~$1.4k)** vs ~$850–$920 earlier months.  
- **Retention:** Early cohorts (Feb–Mar) retained >45% at 3 months; later cohorts <15% by 3 months.  
- **Churn Model:** Logistic regression achieved **AUC = X.XXX, Accuracy = X.XXX** (replace with your output).  
  - ~15% of customers flagged ≥60% churn risk.

---

## 5. Technical Highlights
- **SQL:** Funnel conversion queries, CAC by source, churn summaries, LTV, payback.  
- **Python:** pandas for prep, scikit-learn logistic regression for churn scoring, feature coefficients for explainability.  
- **Tableau:** Integrated dashboard for CAC efficiency, funnel performance, cohort retention, churn risk.  
- **Automation Ready:** Workflow outputs to CSV/SQLite, making it easy to integrate into CRM or BI pipelines.

---

## 6. Business Impact (Simulated)
If implemented at a real SaaS company, this workflow would:  
- Improve **retention** by targeting at-risk customers before they churn.  
- Increase **marketing efficiency** by reallocating spend from high-CAC/long payback channels.  
- Provide **executive visibility** into funnel health, efficiency, and customer stickiness.  

---

## 7. Next Steps (If Live)
1. Integrate with live CRM and billing data.  
2. Automate churn risk score refreshes (scheduled jobs or API).  
3. Layer on A/B tests for targeted retention campaigns.

---

## 8. Links & Assets
- **Tableau Public Dashboard:** [NimbusHR RevOps Dashboard](https://public.tableau.com/views/RealNimbus/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link))  
- **GitHub Repository:** [NimbusHR RevOps Dashboard](https://github.com/romanlicursi/nimbushr-revops-dashboard)  

---

## 9. Author
**Roman Licursi**  
[LinkedIn](https://www.linkedin.com/in/romanlicursi) | [GitHub](https://github.com/romanlicursi)
