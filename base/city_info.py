# -*- coding: utf-8 -*-

"""
@Author: Kevin
@Software: PyCharm
@File: city_info.py
@Time: Nov 19:31
"""

import json


class CityInfo:
    def __init__(self, name="UNNAMED", population=-1, operator="SYSTEM", district_list=[]):
        self.city_info = {"name": name,
                          "population": population,
                          "operator": operator,
                          "district_list": district_list,
                          "hash": hash(name)}

    def save_to_json(self, path):
        json_str = json.dumps(self.city_info)
        with open(path, "w") as f:
            f.write(json_str)
        return True

    def load_from_json(self, path):
        with open(path, "r") as f:
            self.city_info = json.loads(f.read())
        return True
