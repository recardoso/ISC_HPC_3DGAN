from azureml.core import Workspace
from azureml.core.compute import ComputeTarget, AmlCompute
from azureml.core.compute_target import ComputeTargetException
from configs import *

if region is "fr":
    wsCfgPath = ".azureml/config.json"

elif region is "us":
    wsCfgPath = ".azureml_us/config.json"

elif region is "we":
    wsCfgPath = ".azureml_we/config.json"

ws = Workspace.from_config(path=wsCfgPath)

# Verify that the cluster does not exist already
try:
    compute_cluster = ComputeTarget(workspace=ws, name=cluster_name)
    print('Found existing cluster, use it.')

except ComputeTargetException:
    # When the cluster is created, it will have 0 nodes provisioned. The cluster does not incur costs until you submit a job
    compute_config = AmlCompute.provisioning_configuration(vm_size=vmSize,
                                                           idle_seconds_before_scaledown=1200,
                                                           min_nodes=0,
                                                           max_nodes=max_nodes)
    compute_cluster = ComputeTarget.create(ws, cluster_name, compute_config)

compute_cluster.wait_for_completion(show_output=True)
