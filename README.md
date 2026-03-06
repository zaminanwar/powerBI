# Power BI Finance Dashboard Demo

A complete, ready-to-use Power BI finance dashboard with sample data, DAX measures, custom theme, and step-by-step setup instructions.

## What's Included

```
powerBI/
├── data/                          # Sample finance data
│   ├── generate_finance_data.py   # Python script to generate/refresh data
│   ├── DimAccounts.csv            # Chart of accounts
│   ├── DimDepartments.csv         # Department hierarchy
│   ├── DimCostCenters.csv         # Cost centers
│   ├── DimDate.csv                # Date dimension (2023-2025)
│   ├── FactTransactions.csv       # Revenue & expense transactions
│   ├── FactBudget.csv             # Budget data for variance analysis
│   └── FactCashFlow.csv           # Cash flow data
├── measures/
│   └── dax_measures.dax           # 35+ DAX measures ready to paste
├── theme/
│   └── FinanceDashboardTheme.json # Custom Power BI theme
└── docs/
    ├── data-model.md              # Star schema & relationship guide
    └── report-layout.md           # Page layouts with visual specs
```

## Dashboard Pages

| Page | Description | Key Visuals |
|------|-------------|-------------|
| **Executive Summary** | High-level KPIs and trends | Cards, combo chart, donut, bar chart |
| **Income Statement** | Full P&L with quarterly breakdown | Matrix, waterfall chart |
| **Budget Variance** | Actual vs budget comparison | Grouped bars, conditional formatting |
| **Cash Flow** | Operating, investing, financing flows | Waterfall, stacked bar, area chart |
| **Department Deep Dive** | Performance by department & region | Treemap, table, bar charts |

## Quick Start

### 1. Generate Sample Data

```bash
python3 data/generate_finance_data.py
```

This creates 7 CSV files with 3 years (2023-2025) of realistic financial data including seasonality, YoY growth, and variance from budget.

### 2. Open Power BI Desktop

1. **Get Data** > **Text/CSV** > Load all 7 CSV files from the `data/` folder
2. For each file, click **Transform Data** to verify column types:
   - `Amount`, `BudgetAmount` → Decimal Number
   - `DateKey` → Whole Number
   - `Date` → Date
   - IDs → Whole Number

### 3. Apply Custom Theme

1. Go to **View** > **Themes** > **Browse for themes**
2. Select `theme/FinanceDashboardTheme.json`

### 4. Set Up Data Model

1. Switch to **Model View**
2. Create relationships as documented in [`docs/data-model.md`](docs/data-model.md):
   - `FactTransactions[DateKey]` → `DimDate[DateKey]`
   - `FactTransactions[AccountID]` → `DimAccounts[AccountID]`
   - `FactTransactions[DepartmentID]` → `DimDepartments[DepartmentID]`
   - `FactTransactions[CostCenterID]` → `DimCostCenters[CostCenterID]`
   - `FactBudget[DateKey]` → `DimDate[DateKey]`
   - `FactBudget[AccountID]` → `DimAccounts[AccountID]`
   - `FactCashFlow[DateKey]` → `DimDate[DateKey]`

### 5. Add DAX Measures

1. Select a fact table in **Data View**
2. Go to **Modeling** > **New Measure**
3. Copy measures from [`measures/dax_measures.dax`](measures/dax_measures.dax)

**Key measures to add first:**
- `Total Revenue` / `Total Expenses` / `Net Income`
- `Gross Margin %` / `Net Profit Margin %`
- `Revenue Budget` / `Revenue Variance %`
- `Revenue YoY Growth %` / `Revenue YTD`
- `Operating Cash Flow` / `Free Cash Flow`

### 6. Build Report Pages

Follow the detailed layout guide in [`docs/report-layout.md`](docs/report-layout.md) for each page, including visual types, field mappings, and formatting.

## Sample Data Overview

| Table | Rows | Description |
|-------|------|-------------|
| DimAccounts | 22 | Revenue (6) + Expense (16) accounts |
| DimDepartments | 10 | Across 3 regions |
| DimCostCenters | 5 | Physical + virtual locations |
| DimDate | 1,096 | Calendar + fiscal year attributes |
| FactTransactions | ~2,600 | Monthly transactions by account/dept |
| FactBudget | 792 | Monthly budget by account |
| FactCashFlow | 396 | Monthly cash flow by activity |

## Customization

### Regenerate Data
Edit `data/generate_finance_data.py` to:
- Change date ranges (default: 2023-2025)
- Adjust growth rates and seasonality
- Add/remove accounts or departments
- Modify base amounts

### Extend the Model
- Add `FactForecast` for forecasting scenarios
- Add `DimProducts` for product-level analysis
- Add `DimCustomers` for customer segmentation

## Requirements

- **Power BI Desktop** (free download from Microsoft)
- **Python 3.6+** (for data generation only)
