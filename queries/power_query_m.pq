// ============================================================================
// POWER QUERY M - Data Loading & Transformation Scripts
// Use in Power BI: Home > Transform Data > Advanced Editor
// ============================================================================

// --- DimDate ---
// Paste in Advanced Editor for DimDate query
let
    Source = Csv.Document(File.Contents("DimDate.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.None]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    ChangedTypes = Table.TransformColumnTypes(PromotedHeaders, {
        {"DateKey", Int64.Type},
        {"Date", type date},
        {"Year", Int64.Type},
        {"Quarter", type text},
        {"QuarterNumber", Int64.Type},
        {"Month", type text},
        {"MonthNumber", Int64.Type},
        {"MonthShort", type text},
        {"Week", Int64.Type},
        {"DayOfWeek", type text},
        {"DayOfMonth", Int64.Type},
        {"IsWeekend", Int64.Type},
        {"FiscalYear", type text},
        {"FiscalQuarter", type text},
        {"YearMonth", type text}
    }),
    SortedRows = Table.Sort(ChangedTypes, {{"DateKey", Order.Ascending}})
in
    SortedRows


// --- DimAccounts ---
let
    Source = Csv.Document(File.Contents("DimAccounts.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.None]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    ChangedTypes = Table.TransformColumnTypes(PromotedHeaders, {
        {"AccountID", Int64.Type},
        {"AccountName", type text},
        {"AccountType", type text},
        {"Category", type text},
        {"SubCategory", type text}
    })
in
    ChangedTypes


// --- DimDepartments ---
let
    Source = Csv.Document(File.Contents("DimDepartments.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.None]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    ChangedTypes = Table.TransformColumnTypes(PromotedHeaders, {
        {"DepartmentID", Int64.Type},
        {"DepartmentName", type text},
        {"DepartmentHead", type text},
        {"Region", type text}
    })
in
    ChangedTypes


// --- DimCostCenters ---
let
    Source = Csv.Document(File.Contents("DimCostCenters.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.None]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    ChangedTypes = Table.TransformColumnTypes(PromotedHeaders, {
        {"CostCenterID", type text},
        {"CostCenterName", type text},
        {"Location", type text}
    })
in
    ChangedTypes


// --- FactTransactions ---
let
    Source = Csv.Document(File.Contents("FactTransactions.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.None]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    ChangedTypes = Table.TransformColumnTypes(PromotedHeaders, {
        {"TransactionID", Int64.Type},
        {"DateKey", Int64.Type},
        {"AccountID", Int64.Type},
        {"DepartmentID", Int64.Type},
        {"CostCenterID", type text},
        {"Amount", type number},
        {"TransactionType", type text},
        {"Description", type text}
    })
in
    ChangedTypes


// --- FactBudget ---
let
    Source = Csv.Document(File.Contents("FactBudget.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.None]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    ChangedTypes = Table.TransformColumnTypes(PromotedHeaders, {
        {"BudgetID", Int64.Type},
        {"DateKey", Int64.Type},
        {"AccountID", Int64.Type},
        {"BudgetAmount", type number},
        {"BudgetVersion", type text},
        {"Year", Int64.Type},
        {"Month", Int64.Type}
    })
in
    ChangedTypes


// --- FactCashFlow ---
let
    Source = Csv.Document(File.Contents("FactCashFlow.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.None]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    ChangedTypes = Table.TransformColumnTypes(PromotedHeaders, {
        {"CashFlowID", Int64.Type},
        {"DateKey", Int64.Type},
        {"Activity", type text},
        {"LineItem", type text},
        {"Amount", type number},
        {"Year", Int64.Type},
        {"Month", Int64.Type}
    })
in
    ChangedTypes
