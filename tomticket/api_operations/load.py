# -*- coding: utf-8 -*-

from tomticket import HttpError
from tomticket import utils


class Load(object):

    def load(self):
        from tomticket import Tomticket
        cls = self.__class__
        collection = utils.resource_class_to_collection_name(cls)
        if hasattr(self, 'id'):
            response = Tomticket.get("/%s/%s" % (collection, self.id))
        else:
            raise Exception(
                "Cannot load %s as it does not have a valid id." % (cls))

        if response is None:
            raise HttpError('Http Error - No response entity returned')

        return cls(**response)
