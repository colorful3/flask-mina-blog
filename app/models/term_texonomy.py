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

    @staticmethod
    def get_category():
        categorys = FltermTaxonomy.query.join(
            Flterms,
            FltermTaxonomy.term_id == Flterms.term_id
        ).filter(
            FltermTaxonomy.taxonomy == 'category',
        ).with_entities(
            Flterms.name, FltermTaxonomy.term_id,
            FltermTaxonomy.parent, FltermTaxonomy.count
        ).all()
        ret = [dict(zip(category.keys(), category)) for category in categorys]
        return ret


class FltermRelationships(Base):
    object_id = Column(BigInteger, default=0, primary_key=True)
    term_taxonomy_id = Column(BigInteger, default=0, primary_key=True)
    term_order = Column(Integer, default=0)
