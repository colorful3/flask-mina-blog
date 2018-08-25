# -*- coding: utf8 -*-
import datetime
from flask import current_app
from sqlalchemy import Column, BigInteger, String, DateTime, Integer, SmallInteger, orm

from app.libs.c_http import HTTP
from app.libs.error_code import WXException
from app.models.base import Base, db

__author__ = 'Colorful'
__date__ = '2018/8/19 下午5:18'


class Flusers(Base):
    ID = Column(BigInteger, nullable=False, primary_key=True)
    user_login = Column(String(60), nullable=False, default='')
    user_pass = Column(String(255), nullable=False, default='')
    user_nicename = Column(String(50), nullable=False, default='')
    user_email = Column(String(100), nullable=False, default='')
    user_url = Column(String(100), nullable=False, default='')
    user_registered = Column(DateTime, nullable=False, default='0000-00-00 00:00:00')
    user_activation_key = Column(String(100), nullable=False, default='')
    user_status = Column(Integer, nullable=False, default='0')
    display_name = Column(String(250), nullable=False, default='')
    mina_openid = Column(String(100), nullable=False, default='', comment='小程序openid')
    from_mina = Column(SmallInteger, nullable=False, default=0, comment='1 小程序用户， 0 普通用户')
    auth = Column(SmallInteger, nullable=False, default=1, comment='1 普通用户 2 管理员用户')

    @orm.reconstructor
    def __init__(self):
        self.fields = [
            'ID', 'user_login', 'user_nicename', 'user_email',
            'user_registered', 'user_status', 'display_name',
            'mina_openid', 'from_mina', 'auth'
        ]
        pass

    @staticmethod
    def get_openid(code):
        mina_appid = current_app.config['MINA_APPID']
        mina_se = current_app.config['MINA_SECRET']
        mina_login_url = current_app.config['MINA_LOGIN_URL'].format(mina_appid, mina_se, code)
        wx_result = HTTP.get(mina_login_url)
        login_failed = 'errcode' in wx_result.keys()
        if login_failed:
            # TODO 写入日志
            raise WXException(msg=wx_result['errmsg'], error_code=wx_result['errcode'])
        if wx_result is None:
            raise WXException()
        return wx_result

    @staticmethod
    def verify():
        pass

    @staticmethod
    def mina_verify(code):
        user = Flusers()
        wx_result = user.get_openid(code)
        openid = wx_result['openid']
        user_info = Flusers.query.filter_by(mina_openid=openid).first()
        if user_info is None:
            with db.auto_commit():
                user.mina_openid = openid
                user.from_mina = 1
                user.user_registered = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # user.display_name = ''
                db.session.add(user)
                db.session.flush()
                uid = user.ID
                auth = user.auth
        else:
            uid = user_info.ID
            auth = user_info.auth
        scope = 'AdminScope' if auth == 2 else 'UserScope'
        return {'uid': uid, 'scope': scope}

    @staticmethod
    def wx_verify():
        pass

