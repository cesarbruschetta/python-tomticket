# -*- coding: utf-8 -*-

from tomticket import utils


class Count(object):

    @classmethod
    def count(cls):
        from tomticket import Tomticket
        response = Tomticket.get("/counts/")
        return response[utils.resource_class_to_name(cls)]['count']
