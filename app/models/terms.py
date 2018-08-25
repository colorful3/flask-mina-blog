# -*- coding: utf8 -*-
from sqlalchemy import Column, BigInteger, String, orm

from app.models.base import Base

__author__ = 'Colorful'
__date__ = '2018/8/21 下午6:30'


class Flterms(Base):
    term_id = Column(BigInteger, primary_key=True, nullable=False)
    name = Column(String(200), nullable=False, default='')
    slug = Column(String(200), nullable=False, default='')
    term_group = Column(BigInteger, nullable=False, default=0)

    @orm.reconstructor
    def __init__(self):
        self.fields = [
             'name', 'slug', 'term_group'
        ]
