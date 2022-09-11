import os

def set_env_vars() -> None:
#Set the environment variable for Fablib
    os.environ['FABRIC_BASTION_HOST'] = 'bastion-1.fabric-testbed.net'
    os.environ['FABRIC_CREDMGR_HOST'] = 'cm.fabric-testbed.net'
    os.environ['FABRIC_ORCHESTRATOR_HOST'] = 'orchestrator.fabric-testbed.net'
    os.environ['FABRIC_PROJECT_ID']= <PROJECT_ID>
    os.environ['FABRIC_BASTION_USERNAME']= <BASTION_USERNAME>
    os.environ['FABRIC_BASTION_KEY_LOCATION']=os.environ['HOME']+ <BASTION_PRIVATE_KEY_PATH>

    os.environ['FABRIC_SLICE_PRIVATE_KEY_FILE']=os.environ['HOME']+ <FABRIC_SLIVER_PRIVATE_KEY>
    os.environ['FABRIC_SLICE_PUBLIC_KEY_FILE']=os.environ['HOME']+ <FABRIC_SLIVER_PUBLIC_KEY>

    os.environ['FABRIC_LOG_LEVEL'] = 'INFO'

    os.environ['FABRIC_TOKEN_LOCATION'] = os.environ['HOME']+ <FARBIC_TOKENS>
    os.environ['FABRIC_LOG_FILE'] = os.environ['HOME']+ <FABRIC_LOG_FILE>
