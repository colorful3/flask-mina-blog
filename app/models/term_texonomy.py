# -*- coding: utf8 -*-
from sqlalchemy import Column, Text, BigInteger, String, orm, ForeignKey, Integer

from app.models.base import Base, db
from app.models.terms import Flterms

__author__ = 'Colorful'
__date__ = '2018/8/21 下午6:36'


class FltermTaxonomy(Base):
    term_taxonomy_id = Column(BigInteger, nullable=False, primary_key=True)
    term_id = Column(BigInteger, nullable=False, default=0)
    taxonomy = Column(String(32), nullable=False, default='')
    description = Column(Text, nullable=False)
    parent = Column(BigInteger, nullable=False, default=0)
    count = Column(BigInteger, nullable=False, default=0)

    @orm.reconstructor
    def __init__(self):
        self.fields = [
            'term_taxonomy_id', 'term_id', 'taxonomy',
            'parent', 'count'
        ]
        self.cate_ids = []
        # 对外开放的分类
        self.open_cate = [
            '日常', '网络博客', '数据库',
            '算法', '前端', '后端', '运维'
        ]

    def cate_index(self, cid):
        self.cate_ids.append(cid)
        categorys = FltermTaxonomy.query.filter_by(parent=cid).all()
        [self.cate_ids.append(cate.term_taxonomy_id) for cate in categorys]
        if categorys:
            for id in self.cate_ids:
                categorys = FltermTaxonomy.query.filter_by(parent=id).all()
                [self.cate_ids.append(cate.term_taxonomy_id) for cate in categorys]
        self.cate_ids = list(set(self.cate_ids))
        pass

    def get_parent_category(self):
        categorys = FltermTaxonomy.query.join(
            Flterms,
            FltermTaxonomy.term_id == Flterms.term_id
        ).filter(
            FltermTaxonomy.taxonomy == 'category',
            FltermTaxonomy.parent == 0
        ).with_entities(
            Flterms.name, FltermTaxonomy.term_id,
            FltermTaxonomy.parent, FltermTaxonomy.count
        ).all()
        ret = [dict(zip(category.keys(), category)) for category in categorys]
        new_ret = []
        for item in ret:
            if item['name'] in self.open_cate:
                new_ret.append(item)
        new_ret.insert(0, {
            "count": 0,
            "name": "全部",
            "parent": 0,
            "term_id": 0
        })
        return new_ret


class FltermRelationships(Base):
    object_id = Column(BigInteger, default=0, primary_key=True)
    term_taxonomy_id = Column(BigInteger, default=0, primary_key=True)
    term_order = Column(Integer, default=0)
