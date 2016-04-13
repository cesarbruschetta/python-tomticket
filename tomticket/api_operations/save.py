# -*- coding: utf-8 -*-

from tomticket import utils


class Save(object):

    def from_dict(self, pdict):
        for key, value in list(pdict.items()):
            setattr(self, key, value)

    @property
    def to_dict(self):
        a_dict = {}
        for name in list(self.__dict__.keys()):
            if name == "changed_attributes":
                continue
            a_dict[name] = self.__dict__[name]  # direct access
        return a_dict

    @classmethod
    def from_api(cls, response):
        obj = cls()
        obj.from_response(response)
        return obj

    def from_response(self, response):
        self.from_dict(response)
        return self

    def save(self):
        from tomticket import Tomticket
        collection = utils.resource_class_to_name(self.__class__)
        params = self.attributes

        response = Tomticket.post('/{0}/%(token)s'.format(collection), **params)

        if response:
            return self.from_response(response)

    @property
    def identity_hash(self):
        identity_vars = getattr(self, 'identity_vars', [])
        parts = {}
        for var in identity_vars:
            id_var = getattr(self, var, None)
            if id_var:  # only present id var if it is not blank or None
                parts[var] = id_var
        return parts
