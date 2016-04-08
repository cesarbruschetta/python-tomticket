# -*- coding: utf-8 -*-

from tomticket import utils


class Delete(object):

    def delete(self):
        from tomticket import Intercom
        collection = utils.resource_class_to_collection_name(self.__class__)
        Intercom.delete("/%s/%s/" % (collection, self.id))
        return self
