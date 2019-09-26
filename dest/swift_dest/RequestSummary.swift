struct RequestSummary {
    let id: String
    let name: String?
    let apsKey: String?
    let isClosed: Bool?
    let purpose: String?
    let startDate: String?
    let endDate: String?
    let currencyCode: String?
    let shortId: String?
    let key: String?
    let approver: Employee?
    let employee: Employee?
    let highestExceptionLevel: ExceptionLevel?
    let creationDate: String?
    let approvalStatus: String?
    let totalApprovedAmount: Double?
    let approvalLimitDate: String?
    let numberOfExceptions: Int?
    let submitDate: String?
    let totalPostedAmount: Double?
    let totalRemainingAmount: Double?
    let lastComment: String?
    let userPermissions: SummaryUserPermissions?
}