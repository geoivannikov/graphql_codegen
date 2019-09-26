struct Policy {
    let id: String
    let key: String
    let label: String?
    let type: String?
    let isActive: Bool?
    let isDefault: Bool?
    let noCreation: Bool?
    let expenseTypeCategories: [ExpenseTypeCategory?]?
    let confirmIdSubmit: String?
    let confirmIdApprove: String?
    let manageCashAdvances: Bool?
    let cashAdvancesLimit: Int?
}