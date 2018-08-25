# -*- coding: utf8 -*-
import json

from flask import request
from werkzeug.exceptions import HTTPException

__author__ = 'Colorful'
__date__ = '2018/8/19 下午6:44'


class APIException(HTTPException):
    code = 500
    msg = "Life can't always be colorful ￣□￣｜｜"
    error_code = 999

    def __init__(self, msg=None, code=None,
                 error_code=None, headers=None):
        if msg:
            self.msg = msg
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            error_code=self.error_code,
            request=request.method + ' ' + self.get_url_path()
        )
        return json.dumps(body)

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_path():
        full_path = request.full_path
        main_path = full_path.split('?')
        return main_path[0]
