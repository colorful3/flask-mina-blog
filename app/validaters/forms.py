# -*- coding: utf8 -*-
from flask import request
from wtforms import IntegerField, StringField
from wtforms.validators import length, DataRequired, Length

from app.libs.enums import ClientTypeEnum
from app.validaters.base import BaseForm as Form

__author__ = 'Colorful'
__date__ = '2018/8/19 下午4:36'


class ClientForm(Form):
    ac = StringField()
    se = StringField()
    type = IntegerField(validators=[
        DataRequired()
    ])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class MinaLoginForm(ClientForm):
    code = StringField(validators=[
        DataRequired(message='excuse me. Do you want to login? code is required!!!')
    ])


class BlogListForm(Form):
    start = IntegerField(validators=[], default=1)
    count = IntegerField(validators=[])

    def validate_start(self, value):
        start = int(value.data)
        start = start if start else 1
        self.start.data = start

    def validate_count(self, value):
        if value.data:
            count = int(value.data)
            count = 20 if count > 20 else count
            self.count.data = count
        else:
            self.count.data = 20


class CommentForm(Form):
    post_id = IntegerField(validators=[
        DataRequired(message='blog ID must be positive')
    ])
    content = StringField(validators=[
        DataRequired(message='content is required')
    ])
    comment_parent = IntegerField(validators=[
    ], default=0)
    comment_author_IP = StringField(validators=[
    ])
    comment_agent = StringField(validators=[
    ])

    def validate_comment_author_IP(self, value):
        ip = request.remote_addr
        self.comment_author_IP.data = ip

    def validate_comment_agent(self, value):
        agent = request.user_agent.string
        self.comment_agent.data = agent


class CommentListForm(BlogListForm):

    pass
