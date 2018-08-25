# -*- coding: utf8 -*-
from app.libs.error import APIException

__author__ = 'Colorful'
__date__ = '2018/8/19 下午6:09'


class Success(APIException):
    code = 201
    msg = 'OK'
    error_code = 0


class DeleteSuccess(APIException):
    code = 202
    msg = 'OK'
    error_code = 0


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class WXException(APIException):
    code = 500
    msg = 'It\'s none of our business, is the error of WeChat'
    error_code = 8000


class AuthFailed(APIException):
    code = 401
    msg = 'authorization failed'
    error_code = 1005
    
    
class ServerError(APIException):
    code = APIException.code
    msg = APIException.msg
    error_code = APIException.error_code


class NotFound(APIException):
    code = 404
    msg = 'resource is not found'
    error_code = 1007
