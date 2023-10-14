import pydantic as p


class BusinessError(Exception):
    pass


class NoContentError(Exception):
    pass


class NotFoundError(Exception):
    pass


class TaskHasAlreadyBeenStartedError(Exception):
    pass


class TokenRequiredError(Exception):
    pass


class TokenInvalidError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


class ValidationError(Exception):
    pass


ValidationErrors = (p.ValidationError, ValidationError)


class OauthTokenError(Exception):
    pass


class GraphQLError(Exception):
    pass


class ParceiroNotFoundError(Exception):
    pass


class UserNotFoundError(Exception):
    pass
