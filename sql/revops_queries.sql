-- revops_queries.sql
-- Project: NimbusHR RevOps Dashboard (Funnel + Churn + CAC/LTV/Payback)
-- Author: Roman Licursi
-- Notes: Run these queries against nimbushr_revops.db (SQLite). Each section is self-contained.
-- -----------------------------------------------------------------------------

/* 00. Quick peek at tables */
SELECT name FROM sqlite_master WHERE type='table';

/* 01. Overall funnel counts and conversion rates */
WITH base AS (
  SELECT
    COUNT(*) AS leads_total,
    SUM(CASE WHEN mql_date IS NOT NULL THEN 1 ELSE 0 END) AS mqls,
    SUM(CASE WHEN sql_date IS NOT NULL THEN 1 ELSE 0 END) AS sqls,
    SUM(CASE WHEN close_status = 'Closed Won' THEN 1 ELSE 0 END) AS closed_won,
    SUM(CASE WHEN close_status = 'Closed Lost' THEN 1 ELSE 0 END) AS closed_lost
  FROM leads
)
SELECT
  leads_total,
  mqls,
  ROUND(100.0 * mqls / leads_total, 1) AS pct_lead_to_mql,
  sqls,
  ROUND(100.0 * sqls / NULLIF(mqls,0), 1) AS pct_mql_to_sql,
  closed_won,
  ROUND(100.0 * closed_won / NULLIF(sqls,0), 1) AS pct_sql_to_won,
  ROUND(100.0 * closed_won / leads_total, 1) AS pct_full_funnel
FROM base;

/* 02. Funnel by lead source */
SELECT
  lead_source,
  COUNT(*) AS leads_total,
  SUM(CASE WHEN mql_date IS NOT NULL THEN 1 ELSE 0 END) AS mqls,
  ROUND(100.0 * SUM(CASE WHEN mql_date IS NOT NULL THEN 1 ELSE 0 END) / COUNT(*), 1) AS pct_lead_to_mql,
  SUM(CASE WHEN sql_date IS NOT NULL THEN 1 ELSE 0 END) AS sqls,
  ROUND(100.0 * SUM(CASE WHEN sql_date IS NOT NULL THEN 1 ELSE 0 END) / NULLIF(SUM(CASE WHEN mql_date IS NOT NULL THEN 1 ELSE 0 END),0), 1) AS pct_mql_to_sql,
  SUM(CASE WHEN close_status = 'Closed Won' THEN 1 ELSE 0 END) AS closed_won,
  ROUND(100.0 * SUM(CASE WHEN close_status = 'Closed Won' THEN 1 ELSE 0 END) / NULLIF(SUM(CASE WHEN sql_date IS NOT NULL THEN 1 ELSE 0 END),0), 1) AS pct_sql_to_won,
  ROUND(100.0 * SUM(CASE WHEN close_status = 'Closed Won' THEN 1 ELSE 0 END) / COUNT(*), 1) AS pct_full_funnel
FROM leads
GROUP BY lead_source
ORDER BY leads_total DESC;

/* 03. CAC by lead source */
WITH won AS (
  SELECT lead_id, lead_source, marketing_spend
  FROM leads
  WHERE close_status = 'Closed Won'
)
SELECT
  lead_source,
  COUNT(*) AS new_customers,
  SUM(marketing_spend) AS total_marketing_spend,
  ROUND(1.0 * SUM(marketing_spend) / NULLIF(COUNT(*),0), 2) AS cac_per_customer
FROM won
GROUP BY lead_source
ORDER BY cac_per_customer;

/* 04. Overall churn */
SELECT
  COUNT(*) AS customers_total,
  SUM(CASE WHEN churned = 1 THEN 1 ELSE 0 END) AS churned_customers,
  ROUND(100.0 * SUM(CASE WHEN churned = 1 THEN 1 ELSE 0 END) / COUNT(*), 1) AS churn_rate_pct
FROM subscriptions;

/* 05. Churn by contract type & payment method */
SELECT
  contract_type,
  payment_method,
  COUNT(*) AS customers,
  SUM(CASE WHEN churned = 1 THEN 1 ELSE 0 END) AS churned_customers,
  ROUND(100.0 * SUM(CASE WHEN churned = 1 THEN 1 ELSE 0 END) / COUNT(*), 1) AS churn_rate_pct,
  ROUND(AVG(monthly_revenue), 2) AS avg_mrr,
  ROUND(AVG(tenure_months), 1) AS avg_tenure_months
FROM subscriptions
GROUP BY contract_type, payment_method
ORDER BY churn_rate_pct DESC, avg_mrr DESC;

/* 06. Average LTV (assumes 80% gross margin) */
-- LTV ≈ Avg(MRR) * Gross Margin * Avg(Tenure in months)
WITH params AS (SELECT 0.80 AS gross_margin)
SELECT
  ROUND(AVG(monthly_revenue) * (SELECT gross_margin FROM params) * AVG(tenure_months), 2) AS avg_LTV
FROM subscriptions;

/* 07. Payback by lead source (months) */
WITH cust AS (
  SELECT s.*, l.lead_source
  FROM subscriptions s
  JOIN leads l ON l.lead_id = s.lead_id
),
cac AS (
  SELECT lead_source, ROUND(1.0 * SUM(marketing_spend) / NULLIF(COUNT(*),0), 2) AS cac_per_customer
  FROM leads
  WHERE close_status = 'Closed Won'
  GROUP BY lead_source
)
SELECT
  c.lead_source,
  ROUND(AVG(c.monthly_revenue), 2) AS avg_monthly_rev,
  cac.cac_per_customer,
  ROUND(cac.cac_per_customer / NULLIF(AVG(c.monthly_revenue),0), 2) AS payback_months_est
FROM cust c
JOIN cac ON cac.lead_source = c.lead_source
GROUP BY c.lead_source, cac.cac_per_customer
ORDER BY payback_months_est;

/* 08. (Placeholder) Joining churn risk scores when available
   After you run churn_model.py, a table 'subscriptions_scored' will exist.
   Use this to bring risk into your analysis. */
-- Example:
-- SELECT s.customer_id, s.monthly_revenue, ss.churn_risk_score
-- FROM subscriptions s
-- JOIN subscriptions_scored ss USING(customer_id);
