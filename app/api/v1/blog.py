# -*- coding: utf8 -*-
from flask import jsonify, request

from app.libs.c_blueprint import CBlueprint
from app.libs.error_code import NotFound
from app.models.posts import Flposts
from app.models.term_texonomy import FltermTaxonomy
from app.validaters.forms import BlogListForm

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


@api.route('/<int:id>')
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


@api.route('/<int:cid>/by_cate')
def by_category(cid):
    args = request.args.to_dict()
    start = int(args['start'])
    count = int(args['count'])
    posts = Flposts.paginate_data_by_category(cid, start, count)
    return jsonify(posts)


@api.route('/test')
def test():
    info = FltermTaxonomy().cate_index(30)
    print(info)
    return 'success'
