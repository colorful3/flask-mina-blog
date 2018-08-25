# -*- coding: utf8 -*-
from flask import Blueprint
from app.api.v1 import blog, token, comment, banner, taxonomy

__author__ = 'Colorful'
__date__ = '2018/8/19 下午1:04'


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    banner.api.register(bp_v1)
    blog.api.register(bp_v1)
    token.api.register(bp_v1)
    comment.api.register(bp_v1)
    taxonomy.api.register(bp_v1)
    return bp_v1
