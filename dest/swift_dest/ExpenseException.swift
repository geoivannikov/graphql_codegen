struct ExpenseException {
    let expectedExpense: ExpectedExpense?
    let exceptions: [RequestException?]?
    let maxLevel: ExceptionLevel?
}