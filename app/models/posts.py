# -*- coding: utf8 -*-
from sqlalchemy import Column, BigInteger, DateTime, Text, String, Integer, orm
import re

from app.models.base import Base
from app.models.term_texonomy import FltermRelationships

__author__ = 'Colorful'
__date__ = '2018/8/19 下午3:37'


class Flposts(Base):
    ID = Column(BigInteger, nullable=False, primary_key=True)
    post_author = Column(BigInteger, nullable=False, default='0')
    post_date = Column(DateTime, nullable=False, default='0000-00-00 00:00:00')
    post_date_gmt = Column(DateTime, nullable=False, default='0000-00-00 00:00:00')
    post_content = Column(Text, nullable=False)
    post_title = Column(Text, nullable=False)
    post_excerpt = Column(Text, nullable=False)
    post_status = Column(String(20), nullable=False, default='publish')
    comment_status = Column(String(20), nullable=False, default='open')
    ping_status = Column(String(20), nullable=False, default='open')
    post_password = Column(String(255), nullable=False, default='')
    post_name = Column(String(200), nullable=False, default='')
    to_ping = Column(Text, nullable=False)
    pinged = Column(Text, nullable=False)
    post_modified = Column(DateTime, nullable=False, default='0000-00-00 00:00:00')
    post_modified_gmt = Column(DateTime, nullable=False, default='0000-00-00 00:00:00')
    post_content_filtered = Column(Text, nullable=False)
    post_parent = Column(BigInteger, nullable=False, default='0')
    guid = Column(String(255), nullable=False, default='')
    menu_order = Column(Integer, nullable=False, default='0')
    post_type = Column(String(20), nullable=False, default='post')
    post_mime_type = Column(String(100), nullable=False, default='')
    comment_count = Column(BigInteger, nullable=False, default='0')

    @orm.reconstructor
    def __init__(self):
        self.fields = [
            'ID', 'post_author', 'image',
            'post_date', 'post_content',
            'post_description', 'post_title',
            'comment_count', 'post_modified',
            'post_status', 'comment_status',
            'post_parent', 'guid',
            'menu_order', 'post_type'
        ]

    @property
    def post_description(self):
        import re
        dr = re.compile(r'<[^>]+>', re.S)
        post_content = dr.sub('', self.post_content)
        if post_content and len(post_content) > 100:
            return post_content.replace(
                "\n", "").replace(
                "\r", "")[0:100] + '...'
        else:
            return post_content

    @property
    def image(self):
        attachment = Flposts.query.filter_by(
            post_parent=self.ID,
            post_type='attachment'
        ).first()
        return '' if not attachment else attachment['guid']

    @staticmethod
    def paginate_data(start=1, count=20):
        fliters = {
            Flposts.post_title != '',
            Flposts.post_content != '',
            Flposts.post_status == 'publish'
        }

        posts = Flposts.query.filter(*fliters).order_by(
            Flposts.ID.desc()).paginate(start, count)
        items = [item.hide(
            'post_author', 'guid',
            'menu_order', 'post_status',
            'post_type', 'comment_status',
            'post_parent'
        ) for item in posts.items]
        return dict(
            blogs=items,
            count=count,
            start=start,
            total=posts.total
        )

    @staticmethod
    def paginate_data_by_category(cid, start=1, count=20):
        query = Flposts.query.join(
            FltermRelationships,
            Flposts.ID == FltermRelationships.object_id
        ).filter(
            Flposts.post_title != '',
            Flposts.post_content != '',
            Flposts.post_status == 'publish',
            FltermRelationships.term_taxonomy_id == cid
        ).with_entities(
            Flposts.ID, Flposts.comment_count, Flposts.post_content,
            Flposts.post_date, Flposts.post_modified,
            Flposts.post_title, FltermRelationships.term_taxonomy_id
        ).order_by(
            Flposts.post_date.desc()
        )

        result = query.paginate(start, count)
        ret = [
            Flposts.process_cate_data(dict(zip(post.keys(), post)))
            for post in result.items
        ]
        return dict(
            blogs=ret,
            count=count,
            start=start,
            total=result.total
        )

    @staticmethod
    def process_cate_data(row):
        """受wordpress数据库设计的限制，我的代码只能暂时这么设计，
        （可能会有新能问题，不过对于并发量小的博客不至于有性能问题），
        以后有好的方案会修改这里的代码"""
        attachment = Flposts.query.filter_by(
            post_parent=row['ID'],
            post_type='attachment'
        ).first()
        image = '' if not attachment else attachment['guid']
        row['image'] = image

        dr = re.compile(r'<[^>]+>', re.S)
        post_content = dr.sub('', row['post_content'])
        if post_content and len(post_content) > 100:
            post_description = post_content.replace(
                "\n", "").replace(
                "\r", "")[0:100] + '...'
        else:
            post_description = post_content
        row['post_description'] = post_description
        return row
