#!/usr/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '0.0.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: netscaler_raw

short_description: Simplified module to manage a Citrix NetScaler via NITRO API.

version_added: "2.4"

description:
    - "Simplified module to manage a Citrix NetScaler via NITRO API."

options:
    name:
        description:
            - This is the message to send to the sample module
        required: true
    new:
        description:
            - Control to demo if the result of this module is changed or not
        required: false

extends_documentation_fragment:
    - azure

author:
    - Simon Lauger <simon@lauger.de>
'''

EXAMPLES = '''
# Pass in a message
- name: Test with a message
  netscaler_raw:
    name: hello world

# pass in a message and have changed true
- name: Test with a message and changed output
  netscaler_raw:
    name: hello world
    new: true

# fail the module
- name: Test failure of the module
  netscaler_raw:
    name: fail me
'''

RETURN = '''
original_message:
    description: The original name param that was passed in
    type: str
message:
    description: The output message that the sample module generates
'''

from ansible.module_utils.basic import AnsibleModule
import requests
import json
import ast

def run_module():
    module_args = dict(
        url=dict(type='str', required=True),
        username=dict(type='str', required=False, default='nsroot'),
        password=dict(type='str', required=False, default='nsroot'),
        method=dict(type='str', required=False, default='post'),
        ssl=dict(type='bool', required=False, default=True),
        verify=dict(type='bool', required=False, default=False),
        objectname=dict(type='str', required=False, default=None),
        objecttype=dict(type='str', required=True),
        data=dict(type='json', required=False, default=None),
        params=dict(type='dict', required=False, default=None),
        endpoint=dict(type='str', required=False, default='config'),
        onerror=dict(type='str', required=False, default=None)
    )

    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    headers = {
      'X-NITRO-USER': module.params['username'],
      'X-NITRO-PASS': module.params['password'],
      'Accept': 'application/json',
    }

    # if defined, set error handler
    if module.params['onerror'] != None:
      headers['X-NITRO-ONERROR'] = module.params['onerror']

    # build url
    url = module.params['url'] + '/nitro/v1/' + module.params['endpoint'] + '/' + module.params['objecttype']

    # filter to a specific objectname
    if module.params['objectname'] != None:
      url += '/' + module.params['objectname']

    # append params directly to the url var
    # this is requried because the param "params" will be 
    # urlencoded requests by default. this will break things.
    if module.params['params'] != None:
        url += '?'
        if isinstance(module.params['params'], dict):
          for param in module.params['params']:
            url += param + '=' + module.params['params'][param]
        else:
            url += module.params['params']

    # Set Content-Type if required
    if module.params['data'] != None:
      headers['Content-Type'] = 'application/json'

    # do request via requests
    try:
      method_callback = getattr(requests, module.params['method'])
      response = method_callback(
        url,
        headers=headers,
        data=module.params['data'],
        verify=module.params['verify']
      )
    except requests.exceptions.HTTPError as error:
        module.fail_json(msg='NITRO API request to ' + url + ' failed (' + str(error) + ')', **result)
    except requests.exceptions.ConnectionError as error:
        module.fail_json(msg='NITRO API request to ' + url + ' failed (' + str(error) + ')', **result)
    except requests.exceptions.Timeout as error:
        module.fail_json(msg='NITRO API request to ' + url + ' failed (' + str(error) + ')', **result)
    except requests.exceptions.RequestException as error:
        module.fail_json(msg='NITRO API request to ' + url + ' failed (' + str(error) + ')', **result)
    except:
      module.fail_json(msg='NITRO API request to ' + url + ' failed' + url, **result)
    
    try:
      response_json = response.json()
      message = response_json['severity'] + ': ' + response_json['message']

      if response_json['severity'] == 'ERROR':
        module.fail_json(msg=message, **result)
    except:
      message = "NITRO API returned HTTP status code " + str(response.status_code)
      
    result['original_message'] = response.text
    result['message'] = message
    result['changed'] = True

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
