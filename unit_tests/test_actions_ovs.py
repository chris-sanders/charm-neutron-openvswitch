# Copyright 2016 Canonical Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from mock import patch
import sys
import ovs

sys.path.append('actions/')
from test_utils import (
    CharmTestCase
)

TO_PATCH = [
    'subprocess',
]

class TestNeutronOVSCtlActions(CharmTestCase):

    def setUp(self):
        super(TestNeutronOVSCtlActions, self).setUp(ovs, TO_PATCH)

    @patch.object(ovs, 'action_set')
    @patch.object(ovs, 'action_fail')
    def test_list_br(self, action_fail, action_set):
        ovs.list_br()
        self.subprocess.check_call.assert_called_once_with(
            ['ovs-vsctl', '--', 'list-br'])
        self.assertFalse(action_set.called)
        self.assertFalse(action_fail.called)
