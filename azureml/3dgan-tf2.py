import os
from azureml.core import Workspace
from azureml.core import Experiment
from azureml.core import Environment
from azureml.core import ScriptRunConfig
from azureml.core import Dataset
from azureml.core.runconfig import TensorflowConfiguration
from configs import *

if region is "fr":
    wsCfgPath = ".azureml/config.json"

elif region is "us":
    wsCfgPath = ".azureml_us/config.json"

elif region is "we":
    wsCfgPath = ".azureml_we/config.json"

ws = Workspace.from_config(path=wsCfgPath)
datastore = ws.get_default_datastore()
datapath = Dataset.File.from_files(path=(datastore, ''))

experiment = Experiment(workspace=ws, name=name)

if use_curated_env:
    curated_env_name = 'AzureML-TensorFlow-2.3-GPU'
    env = Environment.get(workspace=ws, name=curated_env_name)
else:
    env = Environment.from_conda_specification(
        name='3dgan-tf2-env',
        file_path='.azureml/curated_custom_tf23.yml')

arguments = [
    '--datapath', datapath.as_named_input('input').as_mount(),
    '--nbepochs', nb_epochs,
    '--batchsize', batch_size
]

if multi_node:
    distributed_job_config = TensorflowConfiguration(
        worker_count=worker_count,
        parameter_server_count=0)
    arguments.append('--multi_node')

if use_prepro:
    script = 'GPU_Version2_pp.py'

config = ScriptRunConfig(
    source_directory=pathToScript,
    script=script,
    arguments=arguments,
    compute_target=cluster_name,
    environment=env,
    distributed_job_config=distributed_job_config)

run = experiment.submit(config)
print(run.get_portal_url())
