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

from .job_input import JobInput


class JobInputs(JobInput):
    """Describes a list of of inputs to a Job.

    All required parameters must be populated in order to send to Azure.

    :param odatatype: Required. Constant filled by server.
    :type odatatype: str
    :param inputs: List of inputs to a Job.
    :type inputs: list[~azure.mgmt.media.models.JobInput]
    """

    _validation = {
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
        'inputs': {'key': 'inputs', 'type': '[JobInput]'},
    }

    def __init__(self, **kwargs):
        super(JobInputs, self).__init__(**kwargs)
        self.inputs = kwargs.get('inputs', None)
        self.odatatype = '#Microsoft.Media.JobInputs'
