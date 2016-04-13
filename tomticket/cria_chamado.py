# -*- coding: utf-8 -*-

from tomticket.api_operations.save import Save
from tomticket.traits.api_resource import Resource


class Criar_Chamado(Resource, Save):

    def save(self):
        from tomticket import Tomticket
        params = self.attributes
        url = '/cria_chamado/%(token)s/' + self.identificador_cliente

        response = Tomticket.post(url, **params)

        if response:
            return self.from_response(response)
