#!/usr/bin/env python
# Copyright (c) 2016, Intel Corporation.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of Intel Corporation nor the names of its contributors
#       may be used to endorse or promote products derived from this software
#       without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
import shlex

DOCUMENTATION = '''
---
module: write_string
short_description: write a string to a file
description:
    - write a string to a file without using temp files
options:
  path: path to write to
  val: string to write
  mode: python file mode (w, wb, a, ab)
'''


def main():
    module = AnsibleModule(
        argument_spec={
            'path': {'required': True, 'type': 'path', 'aliases': ['dest']},
            'fact_name': {'required': True},
        }
    )
    params = module.params
    path = params['path']
    fact_name = params['fact_name']
    with open(path) as file_object:
        script = file_object.read()
    variables = dict(l.split('=') for l in shlex.split(script) if '=' in l)
    module.exit_json(changed=True, ansible_facts={fact_name: variables})


# <<INCLUDE_ANSIBLE_MODULE_COMMON>>
from ansible.module_utils.basic import *  # noqa

if __name__ == '__main__':
    main()
