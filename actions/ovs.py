#!/usr/bin/python
#
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

import subprocess
import os
import sys
from charmhelpers.core.hookenv import (
    log
)

sys.path.append('hooks/')

from charmhelpers.core.hookenv import (
    action_fail,
    action_set,
)


def list_br():
    ''' List existing OVS bridges '''
    log('Listing bridges')
    cmd = ["ovs-vsctl", "--", "list-br"]
    #subprocess.check_call(cmd)
    cmd = "set -x; ovs-vsctl list-br"
    subprocess.check_call(cmd, shell=True)

# A dictionary of all the defined actions to callables (which take
# parsed arguments).
ACTIONS = {"list-br": list_br}


def main(args):
    action_name = os.path.basename(args[0])
    try:
        action = ACTIONS[action_name]
    except KeyError:
        s = "Action {} undefined".format(action_name)
        action_fail(s)
        return s
    else:
        try:
            action(args)
        except Exception as e:
            action_fail("Action {} failed: {}".format(action_name, str(e)))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
