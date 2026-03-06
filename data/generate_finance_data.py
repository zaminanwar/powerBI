"""
Finance Data Generator for Power BI Dashboard Demo
Generates realistic sample financial data across multiple tables:
- FactTransactions: Revenue, expenses, and other financial transactions
- DimAccounts: Chart of accounts
- DimDepartments: Company departments
- DimDate: Date dimension table
- DimCostCenter: Cost centers
- FactBudget: Budget data for variance analysis
- FactCashFlow: Cash flow data
"""

import csv
import os
import random
from datetime import datetime, timedelta

random.seed(42)

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# =============================================================================
# Dimension: Accounts (Chart of Accounts)
# =============================================================================
ACCOUNTS = [
    # Revenue accounts
    {"AccountID": 4001, "AccountName": "Product Sales", "AccountType": "Revenue", "Category": "Operating Revenue", "SubCategory": "Product"},
    {"AccountID": 4002, "AccountName": "Service Revenue", "AccountType": "Revenue", "Category": "Operating Revenue", "SubCategory": "Service"},
    {"AccountID": 4003, "AccountName": "Subscription Revenue", "AccountType": "Revenue", "Category": "Operating Revenue", "SubCategory": "Recurring"},
    {"AccountID": 4004, "AccountName": "Consulting Revenue", "AccountType": "Revenue", "Category": "Operating Revenue", "SubCategory": "Service"},
    {"AccountID": 4005, "AccountName": "License Revenue", "AccountType": "Revenue", "Category": "Operating Revenue", "SubCategory": "Product"},
    {"AccountID": 4010, "AccountName": "Interest Income", "AccountType": "Revenue", "Category": "Non-Operating Revenue", "SubCategory": "Financial"},
    # COGS
    {"AccountID": 5001, "AccountName": "Cost of Goods Sold", "AccountType": "Expense", "Category": "COGS", "SubCategory": "Direct Cost"},
    {"AccountID": 5002, "AccountName": "Direct Labor", "AccountType": "Expense", "Category": "COGS", "SubCategory": "Direct Cost"},
    {"AccountID": 5003, "AccountName": "Manufacturing Overhead", "AccountType": "Expense", "Category": "COGS", "SubCategory": "Overhead"},
    # Operating expenses
    {"AccountID": 6001, "AccountName": "Salaries & Wages", "AccountType": "Expense", "Category": "Operating Expenses", "SubCategory": "Personnel"},
    {"AccountID": 6002, "AccountName": "Employee Benefits", "AccountType": "Expense", "Category": "Operating Expenses", "SubCategory": "Personnel"},
    {"AccountID": 6003, "AccountName": "Rent & Facilities", "AccountType": "Expense", "Category": "Operating Expenses", "SubCategory": "Facilities"},
    {"AccountID": 6004, "AccountName": "Utilities", "AccountType": "Expense", "Category": "Operating Expenses", "SubCategory": "Facilities"},
    {"AccountID": 6005, "AccountName": "Marketing & Advertising", "AccountType": "Expense", "Category": "Operating Expenses", "SubCategory": "Marketing"},
    {"AccountID": 6006, "AccountName": "Travel & Entertainment", "AccountType": "Expense", "Category": "Operating Expenses", "SubCategory": "G&A"},
    {"AccountID": 6007, "AccountName": "Professional Services", "AccountType": "Expense", "Category": "Operating Expenses", "SubCategory": "G&A"},
    {"AccountID": 6008, "AccountName": "Software & Technology", "AccountType": "Expense", "Category": "Operating Expenses", "SubCategory": "Technology"},
    {"AccountID": 6009, "AccountName": "Depreciation", "AccountType": "Expense", "Category": "Operating Expenses", "SubCategory": "Non-Cash"},
    {"AccountID": 6010, "AccountName": "Insurance", "AccountType": "Expense", "Category": "Operating Expenses", "SubCategory": "G&A"},
    {"AccountID": 6011, "AccountName": "Office Supplies", "AccountType": "Expense", "Category": "Operating Expenses", "SubCategory": "G&A"},
    {"AccountID": 6012, "AccountName": "Training & Development", "AccountType": "Expense", "Category": "Operating Expenses", "SubCategory": "Personnel"},
    # Tax
    {"AccountID": 7001, "AccountName": "Income Tax", "AccountType": "Expense", "Category": "Tax", "SubCategory": "Income Tax"},
]

DEPARTMENTS = [
    {"DepartmentID": 1, "DepartmentName": "Sales", "DepartmentHead": "Sarah Johnson", "Region": "North America"},
    {"DepartmentID": 2, "DepartmentName": "Marketing", "DepartmentHead": "Michael Chen", "Region": "North America"},
    {"DepartmentID": 3, "DepartmentName": "Engineering", "DepartmentHead": "Priya Patel", "Region": "North America"},
    {"DepartmentID": 4, "DepartmentName": "Finance", "DepartmentHead": "David Kim", "Region": "North America"},
    {"DepartmentID": 5, "DepartmentName": "Human Resources", "DepartmentHead": "Lisa Rodriguez", "Region": "North America"},
    {"DepartmentID": 6, "DepartmentName": "Operations", "DepartmentHead": "James Wilson", "Region": "North America"},
    {"DepartmentID": 7, "DepartmentName": "Customer Support", "DepartmentHead": "Emma Davis", "Region": "Europe"},
    {"DepartmentID": 8, "DepartmentName": "Research & Development", "DepartmentHead": "Ahmed Hassan", "Region": "Europe"},
    {"DepartmentID": 9, "DepartmentName": "Sales - APAC", "DepartmentHead": "Yuki Tanaka", "Region": "Asia Pacific"},
    {"DepartmentID": 10, "DepartmentName": "Sales - EMEA", "DepartmentHead": "Oliver Brown", "Region": "Europe"},
]

COST_CENTERS = [
    {"CostCenterID": "CC-100", "CostCenterName": "Corporate HQ", "Location": "New York"},
    {"CostCenterID": "CC-200", "CostCenterName": "West Coast Office", "Location": "San Francisco"},
    {"CostCenterID": "CC-300", "CostCenterName": "London Office", "Location": "London"},
    {"CostCenterID": "CC-400", "CostCenterName": "Tokyo Office", "Location": "Tokyo"},
    {"CostCenterID": "CC-500", "CostCenterName": "Remote Operations", "Location": "Virtual"},
]


def generate_date_dimension(start_year=2023, end_year=2025):
    """Generate a date dimension table."""
    rows = []
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    current = start
    while current <= end:
        fiscal_month = ((current.month - 1 + 3) % 12) + 1  # fiscal year starts April
        fiscal_quarter = (fiscal_month - 1) // 3 + 1
        fiscal_year = current.year if current.month >= 4 else current.year - 1
        rows.append({
            "DateKey": int(current.strftime("%Y%m%d")),
            "Date": current.strftime("%Y-%m-%d"),
            "Year": current.year,
            "Quarter": f"Q{(current.month - 1) // 3 + 1}",
            "QuarterNumber": (current.month - 1) // 3 + 1,
            "Month": current.strftime("%B"),
            "MonthNumber": current.month,
            "MonthShort": current.strftime("%b"),
            "Week": current.isocalendar()[1],
            "DayOfWeek": current.strftime("%A"),
            "DayOfMonth": current.day,
            "IsWeekend": 1 if current.weekday() >= 5 else 0,
            "FiscalYear": f"FY{fiscal_year}",
            "FiscalQuarter": f"FQ{fiscal_quarter}",
            "YearMonth": current.strftime("%Y-%m"),
        })
        current += timedelta(days=1)
    return rows


def generate_transactions(start_year=2023, end_year=2025):
    """Generate realistic financial transactions."""
    rows = []
    txn_id = 1

    revenue_accounts = [a for a in ACCOUNTS if a["AccountType"] == "Revenue"]
    expense_accounts = [a for a in ACCOUNTS if a["AccountType"] == "Expense"]
    revenue_depts = [1, 2, 9, 10]  # Sales & marketing depts
    all_depts = [d["DepartmentID"] for d in DEPARTMENTS]

    for year in range(start_year, end_year + 1):
        # Year-over-year growth factor
        growth = 1 + (year - start_year) * 0.15

        for month in range(1, 13):
            # Seasonality: higher in Q4, lower in Q1
            season = {1: 0.85, 2: 0.88, 3: 0.95, 4: 1.0, 5: 1.02, 6: 1.05,
                      7: 0.98, 8: 0.92, 9: 1.05, 10: 1.10, 11: 1.20, 12: 1.30}
            seasonal_factor = season[month]

            # Revenue transactions
            for acct in revenue_accounts:
                base = {4001: 450000, 4002: 280000, 4003: 180000,
                        4004: 120000, 4005: 95000, 4010: 15000}
                base_amount = base.get(acct["AccountID"], 100000)

                for dept_id in revenue_depts:
                    amount = base_amount * growth * seasonal_factor * random.uniform(0.85, 1.15) / len(revenue_depts)
                    cc = random.choice(COST_CENTERS)
                    date_day = random.randint(1, 28)
                    date_key = int(f"{year}{month:02d}{date_day:02d}")

                    rows.append({
                        "TransactionID": txn_id,
                        "DateKey": date_key,
                        "AccountID": acct["AccountID"],
                        "DepartmentID": dept_id,
                        "CostCenterID": cc["CostCenterID"],
                        "Amount": round(amount, 2),
                        "TransactionType": "Revenue",
                        "Description": f"{acct['AccountName']} - {DEPARTMENTS[dept_id-1]['DepartmentName']}",
                    })
                    txn_id += 1

            # Expense transactions
            for acct in expense_accounts:
                base_expenses = {
                    5001: 180000, 5002: 95000, 5003: 45000,
                    6001: 320000, 6002: 85000, 6003: 55000,
                    6004: 12000, 6005: 75000, 6006: 25000,
                    6007: 35000, 6008: 45000, 6009: 22000,
                    6010: 18000, 6011: 8000, 6012: 15000,
                    7001: 65000,
                }
                base_amount = base_expenses.get(acct["AccountID"], 20000)
                expense_growth = 1 + (year - start_year) * 0.10  # expenses grow slower

                # Distribute across 2-4 departments
                dept_sample = random.sample(all_depts, min(random.randint(2, 4), len(all_depts)))
                for dept_id in dept_sample:
                    amount = base_amount * expense_growth * random.uniform(0.80, 1.20) / len(dept_sample)
                    cc = random.choice(COST_CENTERS)
                    date_day = random.randint(1, 28)
                    date_key = int(f"{year}{month:02d}{date_day:02d}")

                    rows.append({
                        "TransactionID": txn_id,
                        "DateKey": date_key,
                        "AccountID": acct["AccountID"],
                        "DepartmentID": dept_id,
                        "CostCenterID": cc["CostCenterID"],
                        "Amount": round(amount, 2),
                        "TransactionType": "Expense",
                        "Description": f"{acct['AccountName']} - {DEPARTMENTS[dept_id-1]['DepartmentName']}",
                    })
                    txn_id += 1

    return rows


def generate_budget(start_year=2023, end_year=2025):
    """Generate budget data for variance analysis."""
    rows = []
    budget_id = 1

    for year in range(start_year, end_year + 1):
        growth = 1 + (year - start_year) * 0.12

        for month in range(1, 13):
            for acct in ACCOUNTS:
                if acct["AccountType"] == "Revenue":
                    base = {4001: 440000, 4002: 270000, 4003: 175000,
                            4004: 115000, 4005: 90000, 4010: 14000}
                    amount = base.get(acct["AccountID"], 95000) * growth
                else:
                    base = {
                        5001: 175000, 5002: 90000, 5003: 43000,
                        6001: 310000, 6002: 82000, 6003: 54000,
                        6004: 11500, 6005: 72000, 6006: 24000,
                        6007: 33000, 6008: 43000, 6009: 22000,
                        6010: 17500, 6011: 7500, 6012: 14000,
                        7001: 60000,
                    }
                    amount = base.get(acct["AccountID"], 18000) * (1 + (year - start_year) * 0.08)

                date_key = int(f"{year}{month:02d}01")
                rows.append({
                    "BudgetID": budget_id,
                    "DateKey": date_key,
                    "AccountID": acct["AccountID"],
                    "BudgetAmount": round(amount, 2),
                    "BudgetVersion": "Final",
                    "Year": year,
                    "Month": month,
                })
                budget_id += 1

    return rows


def generate_cashflow(start_year=2023, end_year=2025):
    """Generate cash flow data."""
    rows = []
    cf_id = 1

    categories = [
        ("Operating", "Cash from Customers", 1, 800000),
        ("Operating", "Cash Paid to Suppliers", -1, 350000),
        ("Operating", "Cash Paid to Employees", -1, 320000),
        ("Operating", "Interest Received", 1, 15000),
        ("Operating", "Taxes Paid", -1, 65000),
        ("Investing", "Capital Expenditures", -1, 85000),
        ("Investing", "Asset Sales", 1, 12000),
        ("Investing", "Acquisitions", -1, 25000),
        ("Financing", "Debt Repayment", -1, 45000),
        ("Financing", "Dividends Paid", -1, 30000),
        ("Financing", "Share Issuance", 1, 20000),
    ]

    for year in range(start_year, end_year + 1):
        growth = 1 + (year - start_year) * 0.12
        for month in range(1, 13):
            for activity, item, sign, base in categories:
                amount = base * growth * random.uniform(0.85, 1.15)
                date_key = int(f"{year}{month:02d}15")
                rows.append({
                    "CashFlowID": cf_id,
                    "DateKey": date_key,
                    "Activity": activity,
                    "LineItem": item,
                    "Amount": round(amount * sign, 2),
                    "Year": year,
                    "Month": month,
                })
                cf_id += 1

    return rows


def write_csv(filename, rows, fieldnames):
    """Write rows to a CSV file."""
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"  Written {len(rows):,} rows to {filename}")


def main():
    print("Generating Finance Data for Power BI Dashboard Demo...")
    print("=" * 55)

    # Dimension tables
    write_csv("DimAccounts.csv", ACCOUNTS,
              ["AccountID", "AccountName", "AccountType", "Category", "SubCategory"])

    write_csv("DimDepartments.csv", DEPARTMENTS,
              ["DepartmentID", "DepartmentName", "DepartmentHead", "Region"])

    write_csv("DimCostCenters.csv", COST_CENTERS,
              ["CostCenterID", "CostCenterName", "Location"])

    dates = generate_date_dimension()
    write_csv("DimDate.csv", dates,
              ["DateKey", "Date", "Year", "Quarter", "QuarterNumber", "Month",
               "MonthNumber", "MonthShort", "Week", "DayOfWeek", "DayOfMonth",
               "IsWeekend", "FiscalYear", "FiscalQuarter", "YearMonth"])

    # Fact tables
    transactions = generate_transactions()
    write_csv("FactTransactions.csv", transactions,
              ["TransactionID", "DateKey", "AccountID", "DepartmentID",
               "CostCenterID", "Amount", "TransactionType", "Description"])

    budget = generate_budget()
    write_csv("FactBudget.csv", budget,
              ["BudgetID", "DateKey", "AccountID", "BudgetAmount",
               "BudgetVersion", "Year", "Month"])

    cashflow = generate_cashflow()
    write_csv("FactCashFlow.csv", cashflow,
              ["CashFlowID", "DateKey", "Activity", "LineItem",
               "Amount", "Year", "Month"])

    print("=" * 55)
    print("Data generation complete!")


if __name__ == "__main__":
    main()
