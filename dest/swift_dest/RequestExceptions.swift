struct RequestExceptions {
    let header: [RequestException?]?
    let expense: [ExpenseException?]?
    let cashAdvance: [RequestException?]?
    let hasExceptions: Bool?
    let exceptionCount: Int?
    let maxLevel: ExceptionLevel?
}