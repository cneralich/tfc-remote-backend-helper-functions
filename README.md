# TFC Remote-backend Helper Functions

## STEPS:
### 1. Install the Python Dependencies
```
pip3 install terrasnek
```

### 2. Set Required Environment Variables and create your TFC Client
```
# NEW ORG
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
