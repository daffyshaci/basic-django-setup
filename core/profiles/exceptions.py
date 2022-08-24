from rest_framework.exceptions import APIException


class NotYourProfile(APIException):
    status_code = 403
    default_detail = "you can't edit a profile. It's not you!"