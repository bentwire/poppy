# Copyright (c) 2016 Rackspace, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from poppy.metrics import base


class ServicesController(base.ServicesController):

    def __init__(self, driver):
        super(ServicesController, self).__init__(driver)

        self.driver = driver

    def read(self, metric_name, from_timestamp, to_timestamp, resolution):
        """read metrics from metrics driver.

        """
        pass
