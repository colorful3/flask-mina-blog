# -*- coding: utf8 -*-
from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException

__author__ = 'Colorful'
__date__ = '2018/8/19 下午7:03'


class BaseForm(Form):
    def __init__(self, data=None):
        if data is None:
            data = request.json
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self
