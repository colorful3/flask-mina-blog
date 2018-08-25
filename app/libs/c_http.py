# -*- coding: utf8 -*-
import requests

__author__ = 'Colorful'
__date__ = '2018/8/20 上午8:37'


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        else:
            return r.json() if return_json else r.text
