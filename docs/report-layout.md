# Power BI Report Layout Guide

## Dashboard Pages

---

## Page 1: Executive Summary

```
┌─────────────────────────────────────────────────────────────────────────┐
│  FINANCE DASHBOARD - Executive Summary              [Year ▼] [Dept ▼]  │
├──────────────┬──────────────┬──────────────┬───────────────────────────┤
│  Total Rev   │  Net Income  │  Gross       │  Revenue vs              │
│  $12.4M      │  $2.1M       │  Margin      │  Budget                  │
│  ▲ 15.2% YoY │  ▲ 8.3% YoY │  62.4%       │  103.2%                  │
│  (Card)      │  (Card)      │  (Gauge)     │  (KPI)                   │
├──────────────┴──────────────┴──────────────┴───────────────────────────┤
│                                                                        │
│  Revenue & Net Income Trend (Monthly)                                  │
│  ┌────────────────────────────────────────────────────────────┐        │
│  │  ████                                            ████      │        │
│  │  ████ ████                                 ████  ████      │        │
│  │  ████ ████ ████                      ████  ████  ████      │        │
│  │  ████ ████ ████ ████           ████  ████  ████  ████      │        │
│  │  ████ ████ ████ ████ ████ ████ ████  ████  ████  ████      │        │
│  │  ──── ──── ──── ──── ──── ──── ────  ────  ────  ────      │        │
│  │  Jan  Feb  Mar  Apr  May  Jun  Jul   Aug   Sep   Oct       │        │
│  │  ▓▓▓ Revenue (bars)  ─── Net Income (line)                │        │
│  └────────────────────────────────────────────────────────────┘        │
│                                                                        │
├────────────────────────────────┬───────────────────────────────────────┤
│  Revenue by Department         │  Expense Breakdown                    │
│  ┌────────────────────┐        │  ┌─────────────────────┐             │
│  │      ████████████  │ Sales  │  │  ██████  Personnel  │             │
│  │    ██████████      │ Mktg   │  │  ████    COGS       │             │
│  │   ████████         │ APAC   │  │  ███     Facilities │             │
│  │  ██████            │ EMEA   │  │  ██      Technology │             │
│  │  (Bar Chart)       │        │  │  █       Marketing  │             │
│  └────────────────────┘        │  │  (Donut Chart)      │             │
│                                │  └─────────────────────┘             │
└────────────────────────────────┴───────────────────────────────────────┘
```

### Visuals Used:
| Visual | Measure | Description |
|--------|---------|-------------|
| Card | `Total Revenue` | Total revenue with YoY growth |
| Card | `Net Income` | Net income with YoY growth |
| Gauge | `Gross Margin %` | Target: 60% |
| KPI | `Budget Attainment %` | Target: 100% |
| Combo Chart | `Total Revenue` + `Net Income` | Monthly trend, bars + line |
| Bar Chart | `Total Revenue` by `DepartmentName` | Horizontal bars |
| Donut Chart | `Total Expenses` by `SubCategory` | Expense composition |

---

## Page 2: Income Statement (P&L)

```
┌─────────────────────────────────────────────────────────────────────────┐
│  PROFIT & LOSS STATEMENT                    [Year ▼] [Quarter ▼]       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────┐        │
│  │  Matrix / Table Visual                                      │        │
│  │                                                             │        │
│  │  Account            │ Q1      │ Q2      │ Q3     │ Q4      │        │
│  │  ───────────────────┼─────────┼─────────┼────────┼─────────│        │
│  │  Revenue                                                    │        │
│  │    Product Sales     │ $1.2M   │ $1.3M   │ $1.1M  │ $1.5M  │        │
│  │    Service Revenue   │ $780K   │ $820K   │ $750K  │ $910K  │        │
│  │    Subscriptions     │ $520K   │ $540K   │ $560K  │ $580K  │        │
│  │  Total Revenue       │ $2.8M   │ $3.0M   │ $2.7M  │ $3.4M  │        │
│  │  ───────────────────                                        │        │
│  │  COGS               │ $980K   │ $1.0M   │ $920K  │ $1.2M  │        │
│  │  Gross Profit        │ $1.8M   │ $2.0M   │ $1.8M  │ $2.2M  │        │
│  │  ───────────────────                                        │        │
│  │  Operating Expenses                                         │        │
│  │    Salaries          │ $850K   │ $870K   │ $890K  │ $910K  │        │
│  │    ...               │ ...     │ ...     │ ...    │ ...    │        │
│  │  Total OpEx          │ $1.4M   │ $1.5M   │ $1.4M  │ $1.6M  │        │
│  │  ───────────────────                                        │        │
│  │  NET INCOME          │ $420K   │ $480K   │ $390K  │ $620K  │        │
│  └─────────────────────────────────────────────────────────────┘        │
│                                                                         │
│  ┌───────────────────────────────┐  ┌──────────────────────────┐       │
│  │  Waterfall: Revenue to       │  │  Net Margin % by Quarter │       │
│  │  Net Income breakdown        │  │  (Line Chart)            │       │
│  └───────────────────────────────┘  └──────────────────────────┘       │
└─────────────────────────────────────────────────────────────────────────┘
```

### Visuals Used:
| Visual | Details |
|--------|---------|
| Matrix | Rows: `AccountType` > `Category` > `AccountName`, Columns: `Quarter`, Values: `Amount` |
| Waterfall Chart | Revenue → COGS → Gross Profit → OpEx → Net Income |
| Line Chart | `Net Profit Margin %` by `Quarter` |

---

## Page 3: Budget Variance Analysis

```
┌─────────────────────────────────────────────────────────────────────────┐
│  BUDGET VARIANCE ANALYSIS                   [Year ▼] [Account ▼]      │
├──────────────┬──────────────┬──────────────┬───────────────────────────┤
│  Actual Rev  │  Budget Rev  │  Variance    │  Attainment              │
│  $12.4M      │  $12.0M      │  +$400K      │  103.2%                  │
│  (Card)      │  (Card)      │  (Card)      │  (Gauge)                 │
├──────────────┴──────────────┴──────────────┴───────────────────────────┤
│                                                                        │
│  Actual vs Budget by Month                                             │
│  ┌────────────────────────────────────────────────────────────┐        │
│  │  ████ Budget (light)                                       │        │
│  │  ████ Actual (dark)                                        │        │
│  │  Grouped bar chart showing monthly comparison              │        │
│  └────────────────────────────────────────────────────────────┘        │
│                                                                        │
├────────────────────────────────┬───────────────────────────────────────┤
│  Variance by Account           │  Variance by Department              │
│  (Bar chart, conditional       │  (Bar chart, conditional             │
│   colors: green=favorable,     │   colors: green=favorable,           │
│   red=unfavorable)             │   red=unfavorable)                   │
└────────────────────────────────┴───────────────────────────────────────┘
```

---

## Page 4: Cash Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│  CASH FLOW ANALYSIS                         [Year ▼] [Activity ▼]     │
├──────────────┬──────────────┬──────────────┬───────────────────────────┤
│  Operating   │  Investing   │  Financing   │  Net Cash                │
│  $3.2M       │  -$1.1M      │  -$680K      │  $1.4M                   │
│  (Card)      │  (Card)      │  (Card)      │  (Card)                  │
├──────────────┴──────────────┴──────────────┴───────────────────────────┤
│                                                                        │
│  ┌───────────────────────────────┐  ┌──────────────────────────┐      │
│  │  Cash Flow Waterfall          │  │  Monthly Cash Flow Trend │      │
│  │  Operating → Investing →      │  │  Stacked Bar Chart       │      │
│  │  Financing → Net              │  │  by Activity type        │      │
│  └───────────────────────────────┘  └──────────────────────────┘      │
│                                                                        │
│  ┌─────────────────────────────────────────────────────────────┐      │
│  │  Free Cash Flow Trend (Area Chart)                          │      │
│  │  Shows FCF over time with cumulative line                   │      │
│  └─────────────────────────────────────────────────────────────┘      │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Page 5: Department Deep Dive

```
┌─────────────────────────────────────────────────────────────────────────┐
│  DEPARTMENT ANALYSIS                [Dept ▼] [Region ▼] [Year ▼]      │
├─────────────────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────────────────┐      │
│  │  Treemap: Revenue by Region > Department                     │      │
│  └──────────────────────────────────────────────────────────────┘      │
│                                                                        │
│  ┌───────────────────────────────┐  ┌──────────────────────────┐      │
│  │  Revenue by Department (bar)  │  │  Expenses by Department  │      │
│  │  Sorted descending            │  │  (bar, sorted)           │      │
│  └───────────────────────────────┘  └──────────────────────────┘      │
│                                                                        │
│  ┌──────────────────────────────────────────────────────────────┐      │
│  │  Table: Department Details                                    │      │
│  │  Dept | Head | Revenue | Expenses | Net | Margin% | vs Budget│      │
│  └──────────────────────────────────────────────────────────────┘      │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Theme & Formatting

### Color Palette
| Use | Color | Hex |
|-----|-------|-----|
| Primary / Revenue | Dark Blue | `#2C3E50` |
| Secondary / Accent | Teal | `#1ABC9C` |
| Positive / Favorable | Green | `#27AE60` |
| Negative / Unfavorable | Red | `#E74C3C` |
| Neutral / Budget | Gray | `#95A5A6` |
| Background | Off-White | `#ECF0F1` |
| Card Background | White | `#FFFFFF` |

### Formatting Guidelines
- **Title font**: Segoe UI Semibold, 16pt
- **KPI values**: Segoe UI Bold, 28pt
- **Card subtitles**: Segoe UI, 10pt, gray
- **Number format**: `$#,##0` for amounts, `#,##0.0%` for percentages
- **Conditional formatting**: Green for positive variance, Red for negative
