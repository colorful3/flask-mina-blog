# -*- coding: utf8 -*-
from sqlalchemy import Column, Integer,\
    BigInteger, Text, String, DateTime, orm

from app.models.base import Base

__author__ = 'Colorful'
__date__ = '2018/8/23 下午12:34'


class Flcomments(Base):
    comment_ID = Column(BigInteger, nullable=False, primary_key=True)
    comment_post_ID = Column(BigInteger, nullable=False, default=0)
    comment_author = Column(Text, nullable=False)
    comment_author_email = Column(String(100), nullable=False, default='')
    comment_author_url = Column(String(200), nullable=False, default='')
    comment_author_IP = Column(String(100), nullable=False, default='')
    comment_date = Column(DateTime, nullable=False, default='0000-00-00 00:00:00')
    comment_date_gmt = Column(DateTime, nullable=False, default='0000-00-00 00:00:00')
    comment_content = Column(Text, nullable=False)
    comment_karma = Column(Integer, nullable=False, default=0)
    comment_approved = Column(String(20), nullable=False, default=0, comment='状态')
    comment_agent = Column(String(255), nullable=False, default='')
    comment_type = Column(String(20), nullable=False, default='')
    comment_parent = Column(BigInteger, nullable=False, default=0)
    user_id = Column(BigInteger, nullable=False, default=0)

    @orm.reconstructor
    def __init__(self):
        self.fields = [
            'comment_ID', 'comment_post_ID', 'comment_author',
            'comment_author_email', 'comment_author_url', 'comment_author_IP',
            'comment_date', 'comment_content', 'user_id', 'comment_approved'
        ]
