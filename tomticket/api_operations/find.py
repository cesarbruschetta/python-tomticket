# -*- coding: utf-8 -*-

from tomticket import HttpError
from tomticket import utils


class Find(object):

    @classmethod
    def find(cls, **params):
        from tomticket import Tomticket
        collection = utils.resource_class_to_collection_name(cls)
        if 'id' in params:
            response = Tomticket.get("/%s/%s" % (collection, params['id']))
        else:
            response = Tomticket.get("/%s" % (collection), **params)

        if response is None:
            raise HttpError('Http Error - No response entity returned')

        return cls(**response)
