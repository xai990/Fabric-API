# Fabric-API

This repository contains the code for construct [Fabric-testbed](https://fabric-testbed.net/) environment on local desktops/[Palmetto](https://www.palmetto.clemson.edu/palmetto/). 

## Install the FABRIC Python API

The FABRIC API is available in the following [github repo] (https://github.com/fabric-testbed/fabric-cli)
Please refer more information at [Fabric document] (https://learn.fabric-testbed.net/knowledge-base/install-the-python-api/)

```bash
# create conda environment named fabrictestbed
conda env create -f environment.yml

# activate the conda environment 
conda activate fabrictestbed
```

## Bastion Key and sliver key
Download your Bastion SSH key and Sliver key from the [Fabric Portal](https://portal.fabric-testbed.net/)
## Tokens
Download your tokens from the [Fabric Portal](https://portal.fabric-testbed.net/)

## Run the experiment
### Jupyter Notebook
If your shell support Jupyter Notebook to launch, it could install Jupyter in the conda environment using pip3.

```bash
pip3 install jupyter
# Clone the github repo that include the example notebooks.
git clone https://github.com/fabric-testbed/jupyter-examples.git
# Some of the examples use bash. You can install the Jupyter bash kernel if you want to use these notebooks.
pip3 install bash_kernel
python -m bash_kernel.install
# Run the FABRIC table of contents notebook.
jupyter-notebook jupyter-examples/start_here.ipynb
```
The data transfer can be achieved by the example Jupyter Notebook [upload_and_execute.ipynb](https://github.com/fabric-testbed/jupyter-examples/blob/master/fabric_examples/fablib_api/upload_and_execute/upload_and_execute.ipynb)

### Terminal
If your shell only can run python scripts, please refer the python scripts under [bin](https://github.com/xai990/Fabric-API/tree/main/bin) floders.
Please fill up the required information in [env_set](https://github.com/xai990/Fabric-API/blob/main/bin/set_env.py)

