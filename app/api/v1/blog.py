# -*- coding: utf8 -*-
from flask import jsonify, request

from app.libs.c_blueprint import CBlueprint
from app.libs.error_code import NotFound
from app.models.posts import Flposts
from app.models.term_texonomy import FltermTaxonomy

__author__ = 'Colorful'
__date__ = '2018/8/19 下午1:09'


api = CBlueprint('blog')


@api.route('/list', methods=['GET'])
def get_list():
    # TODO validate层解析json报错
    # form = BlogListForm().validate_for_api()
    # start = int(form.start.data)
    # count = int(form.count.data)
    args = request.args.to_dict()
    start = int(args['start'])
    count = int(args['count'])
    data = Flposts.paginate_data(start, count)
    return jsonify(data)


@api.route('/<int:id>', methods=['GET'])
def get_single(id):
    post = Flposts.query.filter(
        Flposts.post_title != '',
        Flposts.post_content != '',
        Flposts.post_status == 'publish',
        Flposts.ID == id
    ).first()
    if not post:
        raise NotFound()
    return jsonify(post)


@api.route('/<int:cid>/by_cate', methods=['GET'])
def by_category(cid):
    args = request.args.to_dict()
    start = int(args['start'])
    count = int(args['count'])
    taxonomy = FltermTaxonomy()
    taxonomy.cate_index(cid)
    cids = tuple(taxonomy.cate_ids)
    posts = Flposts.paginate_data_by_category(
        cids, start, count
    )
    return jsonify(posts)


@api.route('/<string:date>/by_date', methods=['GET'])
def by_date(date):
    args = request.args.to_dict()
    start = int(args['start'])
    count = int(args['count'])
    post_date = date.replace('年', '-').replace('月', '')
    data = Flposts.query.filter(
        Flposts.post_date.like(post_date + '%'),
        Flposts.post_title != '',
        Flposts.post_content != '',
        Flposts.post_status == 'publish'
    ).paginate(start, count)
    if not data:
        raise NotFound()
    return jsonify(data.items)


@api.route('/test')
def test():
    obj = FltermTaxonomy()
    obj.cate_index(21)
    ids = obj.cate_ids
    return jsonify(ids)
