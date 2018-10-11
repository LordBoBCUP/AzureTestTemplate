from plug.error import VerificationError


class NotEnoughMoneyError(VerificationError):
    fqdn = "plug.error.NotEnoughMoneyError"
    status_code = 400


class InvalidAmountError(VerificationError):
    fqdn = "plug.error.InvalidAmountError"
    status_code = 400
