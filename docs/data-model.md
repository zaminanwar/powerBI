# Power BI Finance Dashboard - Data Model

## Star Schema Overview

```
                    ┌──────────────┐
                    │   DimDate    │
                    │──────────────│
                    │ DateKey (PK) │
                    │ Date         │
                    │ Year         │
                    │ Quarter      │
                    │ Month        │
                    │ FiscalYear   │
                    │ FiscalQtr    │
                    └──────┬───────┘
                           │
    ┌──────────────┐       │       ┌─────────────────┐
    │ DimAccounts  │       │       │ DimDepartments  │
    │──────────────│       │       │─────────────────│
    │ AccountID(PK)│       │       │ DeptID (PK)     │
    │ AccountName  │       │       │ DeptName        │
    │ AccountType  │       │       │ DeptHead        │
    │ Category     │       │       │ Region          │
    │ SubCategory  │       │       └────────┬────────┘
    └──────┬───────┘       │                │
           │               │                │
           │    ┌──────────┴────────────┐   │
           ├────┤  FactTransactions     ├───┤
           │    │───────────────────────│   │
           │    │ TransactionID (PK)    │   │     ┌───────────────┐
           │    │ DateKey (FK)          │   │     │ DimCostCenter │
           │    │ AccountID (FK)        │   │     │───────────────│
           │    │ DepartmentID (FK)     │   │     │ CostCtrID(PK) │
           │    │ CostCenterID (FK)     ├───┼─────┤ Name          │
           │    │ Amount                │   │     │ Location      │
           │    │ TransactionType       │   │     └───────────────┘
           │    └───────────────────────┘   │
           │                                │
           │    ┌───────────────────────┐   │
           ├────┤  FactBudget           │   │
           │    │───────────────────────│   │
           │    │ BudgetID (PK)         │   │
           │    │ DateKey (FK)          │   │
           │    │ AccountID (FK)        │   │
           │    │ BudgetAmount          │   │
           │    │ BudgetVersion         │   │
           │    └───────────────────────┘   │
           │                                │
                ┌───────────────────────┐
                │  FactCashFlow         │
                │───────────────────────│
                │ CashFlowID (PK)       │
                │ DateKey (FK)          │
                │ Activity              │
                │ LineItem              │
                │ Amount                │
                └───────────────────────┘
```

## Relationships

| From Table          | From Column    | To Table        | To Column      | Cardinality |
|---------------------|----------------|-----------------|----------------|-------------|
| FactTransactions    | DateKey        | DimDate         | DateKey        | Many-to-One |
| FactTransactions    | AccountID      | DimAccounts     | AccountID      | Many-to-One |
| FactTransactions    | DepartmentID   | DimDepartments  | DepartmentID   | Many-to-One |
| FactTransactions    | CostCenterID   | DimCostCenters  | CostCenterID   | Many-to-One |
| FactBudget          | DateKey        | DimDate         | DateKey        | Many-to-One |
| FactBudget          | AccountID      | DimAccounts     | AccountID      | Many-to-One |
| FactCashFlow        | DateKey        | DimDate         | DateKey        | Many-to-One |

## Setting Up Relationships in Power BI

1. Open **Power BI Desktop** > **Model View**
2. Drag `DateKey` from each Fact table to `DimDate.DateKey`
3. Drag `AccountID` from FactTransactions/FactBudget to `DimAccounts.AccountID`
4. Drag `DepartmentID` from FactTransactions to `DimDepartments.DepartmentID`
5. Drag `CostCenterID` from FactTransactions to `DimCostCenters.CostCenterID`
6. Ensure all relationships are **Single direction** and **Many-to-One**
