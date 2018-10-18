# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class Query(Resource):
    """Query.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :param next_link:
    :type next_link: str
    :param columns: Array of columns
    :type columns: list[~azure.mgmt.costmanagement.models.QueryColumn]
    :param rows:
    :type rows: list[list[object]]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'tags': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'next_link': {'key': 'properties.nextLink', 'type': 'str'},
        'columns': {'key': 'properties.columns', 'type': '[QueryColumn]'},
        'rows': {'key': 'properties.rows', 'type': '[[object]]'},
    }

    def __init__(self, **kwargs):
        super(Query, self).__init__(**kwargs)
        self.next_link = kwargs.get('next_link', None)
        self.columns = kwargs.get('columns', None)
        self.rows = kwargs.get('rows', None)
