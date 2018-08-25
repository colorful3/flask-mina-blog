# -*- coding: utf8 -*-
from flask import jsonify

from app.libs.c_blueprint import CBlueprint
from app.models.banner import Flbanner

__author__ = 'Colorful'
__date__ = '2018/8/21 上午9:35'


api = CBlueprint('banner')


@api.route('', methods=['GET'])
def get_banner():
    banners = Flbanner.get_banner()
    return jsonify(banners)
