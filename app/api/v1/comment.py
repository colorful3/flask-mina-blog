# -*- coding: utf8 -*-
from datetime import date, datetime
from flask import g, request, jsonify

from app.libs.c_blueprint import CBlueprint
from app.libs.error_code import Success, NotFound
from app.models.base import db
from app.models.comment import Flcomments
from app.validaters.forms import CommentForm, CommentListForm

__author__ = 'Colorful'
__date__ = '2018/8/20 下午1:06'
from app.libs.auth_token import auth


api = CBlueprint('comment')


@api.route('', methods=['POST'])
@auth.login_required
def post():
    form = CommentForm().validate_for_api()
    with db.auto_commit():
        comment = Flcomments()
        comment.comment_post_ID = form.post_id.data
        comment.comment_content = form.content.data
        comment.comment_parent = form.comment_parent.data
        comment.comment_author_IP = form.comment_author_IP.data
        comment.comment_agent = form.comment_agent.data
        comment.user_id = g.user.uid
        comment.comment_author = '123'
        comment.comment_date = datetime.now()
        db.session.add(comment)
    return Success()


@api.route('/<int:id>', methods=['GET'])
def comment_list(id):
    form = CommentListForm().validate_for_api()
    comments = Flcomments.query.filter_by(
        comment_post_ID=id,
        # comment_approved=1
    ).order_by(
        Flcomments.comment_date.desc()
    ).paginate(form.start.data, form.count.data)
    if not comments.items:
        raise NotFound(msg='no comments')
    return jsonify(comments.items)
