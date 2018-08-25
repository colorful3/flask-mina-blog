# -*- coding: utf8 -*-
from sqlalchemy import BigInteger, Column, String, SmallInteger, DateTime, orm

from app.libs.error_code import NotFound
from app.models.base import Base

__author__ = 'Colorful'
__date__ = '2018/8/21 上午9:49'


class Flbanner(Base):
    ID = Column(BigInteger, nullable=False, primary_key=True)
    banner_name = Column(String(100), nullable=False, default='', comment='banner名称')
    image = Column(String(255), nullable=False, default='', comment='轮播图地址')
    jump_type = Column(SmallInteger, nullable=False, default=1, comment='跳转类型，0，无导向；1：导向博客;2:导向分类')
    key_word = Column(BigInteger, nullable=False, default=1, comment='执行关键字，根据不同的type含义不同')
    post_date = Column(DateTime, nullable=False, default='0000-00-00 00:00:00')
    banner_status = Column(String(20), nullable=False, default='1', comment='状态 1: 正常，trash:删除')

    @orm.reconstructor
    def __init__(self):
        self.fields = [
            'ID', 'banner_name', 'image', 'jump_type',
            'key_word'
        ]

    @staticmethod
    def get_banner():
        result = Flbanner.query.filter_by(banner_status=1).order_by(
            Flbanner.post_date.desc()
        ).limit(5).all()
        if not result:
            raise NotFound(msg='no banner!', error_code=2001)
        return result
