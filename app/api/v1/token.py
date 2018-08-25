# -*- coding: utf8 -*-
from flask import current_app, jsonify
from itsdangerous import \
    TimedJSONWebSignatureSerializer as Serializer

from app.libs.c_blueprint import CBlueprint
from app.libs.enums import ClientTypeEnum
from app.models.users import Flusers
from app.validaters.forms import MinaLoginForm

__author__ = 'Colorful'
__date__ = '2018/8/19 下午9:21'


api = CBlueprint('token')


@api.route('', methods=['POST'])
def get_token():
    form = MinaLoginForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: Flusers.verify,
        ClientTypeEnum.USER_MINA: Flusers.mina_verify,
        ClientTypeEnum.USER_WX: Flusers.wx_verify
    }

    identify = promise[ClientTypeEnum(form.type.data)](
        form.code.data
    )
    expires_in = current_app.config['EXPIRES_IN']
    token = generate_auth_token(identify['uid'], form.type.data,
                                identify['scope'], expires_in)
    t = {
        'token': token.decode('ascii')
    }
    return jsonify(t), 201


def generate_auth_token(uid, ac_type,
                        scope=None, expires_in=7200):
    s = Serializer(current_app.config['SECRET_KEY'],
                   expires_in=expires_in)
    return s.dumps({
        'uid': uid,
        'type': ac_type.value,
        'scope': scope
    })
