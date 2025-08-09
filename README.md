# NimbusHR RevOps Dashboard (Portfolio Project)

**Owner:** Roman Licursi  
**Stack:** SQL (SQLite), Python (pandas, scikit-learn), Tableau

## What this shows
- End-to-end RevOps/GTM analytics on CRM + subscription data
- KPIs: funnel conversion, CAC, churn, LTV, payback
- Applied AI: simple churn-risk scoring integrated back into the dataset

## Project structure
```
/data
  nimbushr_revops.db
/sql
  revops_queries.sql
/python
  churn_model.py
/notebooks
  (optional) exploratory notebooks
/tableau
  (placeholder for .twbx or link)
/docs
  case_study.md (export from Notion)
```

## Quick start
1) Open `/data/nimbushr_revops.db` with DB Browser for SQLite (or Python)  
2) Run `/sql/revops_queries.sql` to compute core metrics  
3) (Optional) Run churn model:
```bash
cd python
python churn_model.py ../data/nimbushr_revops.db
```
This creates a table `subscriptions_scored` with a `churn_risk_score` (0–1).

4) Connect Tableau to the SQLite DB and build:
- Executive Overview (churn %, CAC, LTV, payback)
- Funnel View (conversion by stage & source)
- Churn Analysis (segments + risk score)
- Revenue Attribution (source ROI & payback)

## Business framing (for case study)
- Problem: High churn and unclear funnel performance limit revenue growth
- Solution: Unified RevOps dashboard (SQL + Python + Tableau) with AI churn scoring
- Results (modeled): Potential 15% churn reduction and 12% lift in MQL→SQL conversion
- Impact: Prioritize at-risk cohorts and channels with fastest CAC payback

## Notes
- Data is synthetic but structured like real CRM/billing data.
- Replace channel names, pricing, or segments as needed.
