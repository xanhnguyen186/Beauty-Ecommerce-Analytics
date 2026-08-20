# Global Skincare & Beauty E-Store — Findings Report

**FY2020–2023 · Global Direct-to-Consumer Beauty E-Commerce · Values in USD**

---

## 1. Project Overview

This project turns a raw global beauty e-commerce export into a decision-ready analytics product. The dataset covers **transaction-line records across 2020–2023**, each row capturing one product within one order — its financials, customer, geography, and product hierarchy.

The goal was to answer three questions a commercial leader actually asks: **how is the business performing, what makes money versus what loses it, and which customers are worth keeping?** The output is a three-page Power BI dashboard — Overview, Product, and Customer — built on a SQL-prepared dataset, following a business-health → profitability → customer-value arc.

---

## 2. Dataset Summary

- **Grain:** transaction-line level — one row per product per order
- **Period:** 2020–2023
- **Currency:** USD
- **Key feature groups:**
  - *Order & customer* — order ID, customer ID, order date, customer segment
  - *Geography* — city, state, country, latitude/longitude, region, market
  - *Product* — category, subcategory, product name
  - *Financials* — quantity, sales, discount, profit
- **Data quality:** the dataset proved internally consistent with no missing values, so preparation focused on validation and type correctness rather than imputation.

The financial columns are trustworthy — profit reconciles against sales and discount across rows — so the margin and discount analysis rests on solid figures.

---

## 3. Data Preparation & Analysis

**Preparation (Python + PostgreSQL).** The source sheet was profiled in pandas, column names standardised to snake_case, and date fields parsed to proper datetimes. Duplicates were dropped and validation checks run on key ranges (ages, non-negative money, discount bounds) and on profit sign. A notable type issue was caught and fixed: the discount field imported as whole numbers — rounding decimal rates like 0.4 and 0.6 to 0 and 1 — which was corrected to decimal so discount bands could be analysed. The cleaned table was loaded into PostgreSQL.

**Segmentation (SQL).** Customers were scored with an RFM model built directly in SQL: each customer's Recency (days since last order), Frequency (distinct orders), and Monetary value (total sales) were scored 1–4 using `NTILE(4)` window functions, then mapped to named segments — Champions, Loyal, New/Promising, At Risk, Needs Attention, and Lost. The segmentation was exported and joined back to the transaction data in Power BI on customer ID, driving the customer-value analysis.

**Analysis.** Aggregation queries and DAX measures answered the core questions: sales/profit/margin trends with prior-year comparison; profit and margin by category and subcategory; the relationship between discount depth and profit; loss-making product counts; RFM segment sizes and their revenue share; and sales/profit by market and country.

---

## 4. Dashboard — Key Findings

### Page 1 · Overview — *how the business is performing* (2022 → 2023)

**Headline:** 2.19M sales (+23.82%) · 279.93K profit (−12.16%) · 12.77% margin (−5.23 pts) · 93.6K units (+24.21%).

On the surface 2023 was a strong growth year — sales and quantity both rose roughly 24% over 2022. **But profit moved the opposite way**, falling 12% while margin dropped over five points to 12.77%.

This is the year's defining tension: **the business grew volume while losing profitability.** Selling more but keeping less of each dollar is the signature of margin erosion — the growth is being bought, not earned. The remaining two pages diagnose why, and the answer is discounting.

### Page 2 · Product — *what makes money and what loses it*

**Headline:** Body care most profitable · Home & Accessories loss-making · 561 loss-making products (+130) · profit turns negative past 20% discount.

Two findings carry this page, and together they explain the Overview's margin drop.

First, **profitability is uneven and one category is underwater.** Face care (30.1% margin), Make up (25.1%), and Body care (16.8%) are healthy earners, but **Home & Accessories runs a negative −4.60% margin** — the single biggest drag on overall profit.

Second, **discounting is the mechanism of the losses.** Average profit by discount band shows a clean cliff: orders at 0% discount earn +34 on average and 1–20% earn +15, but profit turns **negative beyond 20%** — −14 at 21–40%, −35 at 41–60%, and −44 at 61–80%. **Orders discounted above roughly 20% lose money on average**, and the bulk of the loss concentrates in Home & Accessories, where deep discounting is heaviest. With **561 products now loss-making — up 130 year over year** — the leakage is spreading, not shrinking.

### Page 3 · Customer — *who to keep, and where* (2022 → 2023)

**Headline:** growing customer base · repeat rate rising to 13.94% · Champions ~26–36% of customers but ~51% of revenue · Europe the most profitable market.

The customer base is **highly concentrated in value.** Champions — the top RFM segment — make up roughly a third of customers but drive **around half of all revenue**, and their per-customer value dwarfs the lower segments. Retaining this group is therefore the highest-leverage lever in the business, and the concentration is also a risk: losing a few Champions costs far more than losing many low-value buyers.

**Loyalty is improving** — repeat purchase rate climbed from 9.62% to 11.25% to 13.94% across the years — though it remains low in absolute terms, marking retention as an open opportunity.

Geographically, **revenue leaders and profit leaders differ.** Asia Pacific and Europe lead on sales, but **Europe is the most profitable market at ~18% margin** versus Asia Pacific's thinner ~7% despite its higher volume — a signal about where profitable growth actually lives.

---

## 5. Business Recommendations

1. **Cap discounts near 20%.** Profit turns negative beyond that threshold; deep discounts are the primary driver of the year-over-year margin decline and buy volume at the expense of profit. Introduce approval gates above the cap.

2. **Fix or reposition Home & Accessories.** It is the only loss-making category and absorbs the heaviest discounting — review its pricing and promotion strategy before it drags profitability further.

3. **Protect the Champions segment.** With roughly half of revenue concentrated in the top segment, targeted retention and loyalty investment defends the majority of the business and mitigates concentration risk.

4. **Grow the profitable markets, not just the biggest.** Europe's superior margin makes it a stronger growth target than higher-volume, lower-margin Asia Pacific.

5. **Convert one-time buyers.** Repeat rate is rising but low; win-back campaigns aimed at recently-lapsed, high-value customers (surfaced in the Top Customers table) could lift retention and lifetime value.

---

*Prepared from the 2020–2023 beauty e-commerce dataset and the accompanying three-page Power BI dashboard. Prior-year comparisons reference 2022 versus 2023 unless otherwise noted.*
