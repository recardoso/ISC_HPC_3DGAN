from azureml.core import Workspace

# france central
name='ws3dgan-tf2'
resource_group='ws3dgan-tf2'
location='francecentral'
cfgDir = "azureml"

# east us 2
name='ws3dgan-tf2-us'
resource_group='ws3dgan-tf2.us'
location='eastus2'
cfgDir = "azureml_us"

# west europe
name='ws3dgan-tf2-we'
resource_group='ws3dgan-tf2-we'
location='westeurope'
cfgDir = "azureml_we"

ws = Workspace.create(name=name,
                      subscription_id='e53421f6-39d4-43d7-8ae4-3c80af669e2d',
                      resource_group=resource_group,
                      create_resource_group=True,
                      location=location)

# write out the workspace details to a configuration file: .azureml/config.json
ws.write_config(path='.%s/config.json' % cfgDir)
