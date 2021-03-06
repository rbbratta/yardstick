# Copyright 2013 IBM Corp
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

# yardstick comment: this is a modified copy of
# ceilometer/ceilometer/dispatcher/file.py

from __future__ import absolute_import

from yardstick.dispatcher.base import Base as DispatchBase
from yardstick.common import constants as consts
from yardstick.common import utils


class FileDispatcher(DispatchBase):
    """Dispatcher class for recording data to a file.
    """

    __dispatcher_type__ = "File"

    def __init__(self, conf, config):
        super(FileDispatcher, self).__init__(conf)
        self.result = []

    def record_result_data(self, data):
        self.result.append(data)

    def flush_result_data(self):
        file_path = self.conf.get('file_path', consts.DEFAULT_OUTPUT_FILE)

        res = utils.read_json_from_file(file_path).get('result')
        res.extend(self.result)

        data = {'status': 0, 'result': res}
        utils.write_json_to_file(file_path, data)
