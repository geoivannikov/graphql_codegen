struct ExpectedExpenseView {
    let formId: String
    let formFieldValues: FormFieldValues?
    let formFieldControls: [FormFieldControls?]?
    let expenseType: String?
    let expenseTypeId: String?
    let transactionAmount: Double?
    let transactionDate: String?
    let currencyId: String?
    let comment: String?
    let vendor: String?
    let isTravelAllowance: Bool?
    let comments: [Comment?]?
    let mileageJourneyLog: MileageJourneyLog?
}