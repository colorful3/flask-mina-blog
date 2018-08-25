# -*- coding: utf8 -*-
from flask import jsonify

from app.libs.c_blueprint import CBlueprint
from app.models.term_texonomy import FltermTaxonomy

__author__ = 'Colorful'
__date__ = '2018/8/21 下午6:47'


api = CBlueprint('taxonomy')


@api.route('/category')
def get_category():
    data = FltermTaxonomy.get_category()
    return jsonify(data)
