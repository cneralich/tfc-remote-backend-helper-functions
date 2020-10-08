# TFC Remote-backend Helper Functions

## STEPS:
### 1. Install Python Dependencies
```
pip3 install terrasnek
```

### 2. Set Required Environment Variables and create your TFC Client
```
TFE_TOKEN = os.getenv("TFE_TOKEN", None)
TFE_URL = os.getenv("TFE_URL", None)
TFE_ORG = os.getenv("TFE_ORG", None)

api_new = TFC(TFE_TOKEN, url=TFE_URL)
api_new.set_org(TFE_ORG)
```
Note:
* The Token(s) used above must be either a Team or User Token and have the appropriate level of permissions to interact with state
* The URL(s) used above must follow a format of `https://app.terraform.io`

### 3. Import Functions
```
from taint_functions import *
from import_functions import *
```

### 4. Call Functions and Pass Required Arguments
**IMPORT FUNCTIONS:**
* import_to_state_by_ws_id
  * **Description:** This function allows Users to pass a workspace_id, resource_name, and resource_id and will import that resource into their state in TFC/E
  * **Example:** `import_to_state_by_ws_id(api, 'ws-abcdefgh12345678', 'aws_eip.example', 'eipalloc-xxxxxxxxxxx')`
* import_to_state_by_ws_name
  * **Description:** This function allows Users to pass a workspace_name, resource_name, and resource_id and will import that resource into their state in TFC/E
  * **Example:** `import_to_state_by_ws_name(api, 'my-workspace', 'aws_eip.example', 'eipalloc-xxxxxxxxxxx')`
* import_list_to_state_by_ws_id
  * **Description:** This function allows Users to pass a workspace_id and a dictionary of resource_names/resource_ids and will import those resources into their state in TFC/E
  * **Example:** `import_list_to_state_by_ws_id(api, 'ws-abcdefgh12345678', {'aws_eip.example':'eipalloc-xxxxxxxxxxx', 'aws_eip.example_two': 'eipalloc-yyyyyyyyy'})`
* import_list_to_state_by_ws_name
  * **Description:** This function allows Users to pass a workspace_name and a dictionary of resource_names/resource_ids and will import those resources into their state in TFC/E
  * **Example:** `import_list_to_state_by_ws_name(api, 'my-workspace', {'aws_eip.example':'eipalloc-xxxxxxxxxxx', 'aws_eip.example_two': 'eipalloc-yyyyyyyyy'})`
* **NOTE:** 
  * Import commands will be executed locally, so any variables needed to perform the import operation will either need to be set as Env variables (ex. `export TF_VAR_myvariable=xxxxxxx`), passed as CLI arguments, or included in a terraform.tfvars file in the same directory
  * By default, the import functions expect the [remote_backend configuration](https://www.terraform.io/docs/backends/types/remote.html#example-configurations) to be contained in a separate file named `backend.tf`, but if Users have different file naming conventioins, they can simply update the default values used in [import_functions.py](import_functions.py)

**TAINT FUNCTIONS:**
* taint_state_by_ws_id
  * **Description:** This function allows Users to pass a workspace_id a list of resources, and those resources will be tainted in that state file in TFC/E
  * **Example:** `taint_state_by_ws_id(api, 'ws-abcdefgh12345678', ['aws_eip.example', 'aws_eip.example_two'])`
* taint_state_by_ws_name
  * **Description:** This function allows Users to pass a workspace_id a list of resources, and those resources will be tainted in that state file in TFC/E
  * **Example:** `taint_state_by_ws_name(api, 'my-workspace', ['aws_eip.example', 'aws_eip.example_two'])`
