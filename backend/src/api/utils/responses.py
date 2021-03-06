from flask import make_response, jsonify

def response_with(response, value=None,
                  error=None, headers={}, pagination=None):
    result = {}
    if value is not None:
        result.update(value)

    if response.get("message", None) is not None:
        result.update({
            "message": response["message"]
        })

    result.update({
        "code": response["code"]
    })

    if error is not None:
        result.update({
            "errors": error
        })

    if pagination is not None:
        result.update({
            "pagination": pagination
        })

    headers.update({
        "Access-Control-Allow-Origin": "*"
    })
    headers.update({
        "server": "Flask REST API"
    })

    return result, response["status"], headers

INVALID_FIELD_NAME_SENT_422 = {
    "status": 422,
    "code": "invalidField",
    "message": "Invalid fields found"
}

INVALID_INPUT_422 = {
    "status": 422,
    "code": "invalidInput",
    "message": "Invalid input"
}

MISSING_PARAMETERS_422 = {
    "status": 422,
    "code": "missingParameter",
    "message": "Missing parameters."
}

BAD_REQUEST_400 = {
    "status": 400,
    "code": "badRequest",
    "message": "Bad request"
}

SERVER_ERROR_500 = {
    "status": 500,
    "code": "serverError",
    "message": "Server error"
}

SERVER_ERROR_404 = {
    "status": 404,
    "code": "notFound",
    "message": "Resource not found"
}

FORBIDDEN_403 = {
    "status": 403,
    "code": "notAuthorized",
    "message": "You are not authorised to execute this."
}
UNAUTHORIZED_401 = {
    "status": 401,
    "code": "notAuthorized",
    "message": "Invalid authentication."
}

NOT_FOUND_HANDLER_404 = {
    "status": 404,
    "code": "notFound",
    "message": "route not found"
}

SUCCESS_200 = {
    'status': 200,
    'code': 'success',
}

SUCCESS_201 = {
    'status': 201,
    'code': 'success'
}

SUCCESS_204 = {
    'status': 204,
    'code': 'success'
}