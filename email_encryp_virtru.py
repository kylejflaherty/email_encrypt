# Encryption example - HTML format
import os
from virtru_tdf3_python import Client, Policy, EncryptFileParams

# Load email and appId from environment variables
VIRTRU_SDK_EMAIL = "pluvi1044@gmail.com"
VIRTRU_SDK_APP_ID = "342513eb-c725-4b39-9d3d-370f87c7951d"
if not (VIRTRU_SDK_EMAIL and VIRTRU_SDK_APP_ID):
    raise EnvironmentError("An environment variable is not set:\n- VIRTRU_SDK_EMAIL\n- VIRTRU_SDK_APP_ID")

# Authenticate
client = Client(owner=VIRTRU_SDK_EMAIL, app_id=VIRTRU_SDK_APP_ID)

# Create a default policy and share
policy = Policy()
policy.share_with_users(["kylejflaherty@gmail.com"])
unprotected_file = "sensitive.txt"
protected_file = unprotected_file + ".tdf.html"
param = EncryptFileParams(in_file_path=unprotected_file,
                          out_file_path=protected_file)
param.set_policy(policy)

# Encrypt
client.encrypt_file(encrypt_file_params=param)
print(f"Encrypted file {protected_file}")