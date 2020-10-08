import os
from terrasnek.api import TFC
import urllib.request
import hashlib
import base64
import json
import subprocess

# Method for tainting resources when workspace_id is passed
def taint_state_ws_id(api, workspace_id, taint_list):
    current_version = api.state_versions.get_current(workspace_id)[
        'data']
    
    state_url = current_version['attributes']['hosted-state-download-url']
    pull_state = urllib.request.urlretrieve(state_url, 'terraform.tfstate')

    for resource in taint_list:
        subprocess.call(["terraform", "taint", "%s" % (resource)]) 

    state_file = open("terraform.tfstate", "r")
    state_data = state_file.read()
    state_encoded = state_data.encode("utf8")
    state_serial = json.loads(state_data)['serial']
    state_lineage = json.loads(state_data)['lineage']

    state_hash = hashlib.md5()
    state_hash.update(state_encoded)
    state_md5 = state_hash.hexdigest()
    state_b64 = base64.b64encode(state_encoded).decode("utf-8")

    # Build the new state payload
    create_state_version_payload = {
        "data": {
            "type": "state-versions",
            "attributes": {
                "serial": state_serial,
                "lineage": state_lineage,
                "md5": state_md5,
                "state": state_b64
            }
        }
    }

    # Migrate state to the new Workspace
    api.workspaces.lock(workspace_id, {
                            "reason": "taint script"})
    api.state_versions.create(
        workspace_id, create_state_version_payload)
    api.workspaces.unlock(workspace_id)

    os.remove('terraform.tfstate')
    os.remove('terraform.tfstate.backup')

    return


# Method for tainting resources when workspace_name is passed
def taint_state_ws_name(api, workspace_name, taint_list):
    workspace_id = api.workspaces.show(workspace_name=workspace_name)['data']['id']
    
    current_version = api.state_versions.get_current(workspace_id)[
        'data']
    
    state_url = current_version['attributes']['hosted-state-download-url']
    pull_state = urllib.request.urlretrieve(state_url, 'terraform.tfstate')

    for resource in taint_list:
        subprocess.call(["terraform", "taint", "%s" % (resource)]) 

    state_file = open("terraform.tfstate", "r")
    state_data = state_file.read()
    state_encoded = state_data.encode("utf8")
    state_serial = json.loads(state_data)['serial']
    state_lineage = json.loads(state_data)['lineage']

    state_hash = hashlib.md5()
    state_hash.update(state_encoded)
    state_md5 = state_hash.hexdigest()
    state_b64 = base64.b64encode(state_encoded).decode("utf-8")

    # Build the new state payload
    create_state_version_payload = {
        "data": {
            "type": "state-versions",
            "attributes": {
                "serial": state_serial,
                "lineage": state_lineage,
                "md5": state_md5,
                "state": state_b64
            }
        }
    }

    # Migrate state to the new Workspace
    api.workspaces.lock(workspace_id, {
                            "reason": "taint script"})
    api.state_versions.create(
        workspace_id, create_state_version_payload)
    api.workspaces.unlock(workspace_id)

    os.remove('terraform.tfstate')
    os.remove('terraform.tfstate.backup')

    return
