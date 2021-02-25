vmSize = 'Standard_NC24rs_v3'
vmSize = 'Standard_NC24s_v3'

cluster_name = "dedicated-noIB"
cluster_name = "dedicated-24rs"
cluster_name = "dedictd-100-24rs"
cluster_name = "dedictd-100noIB"

max_nodes = 8 # 32 gpus
max_nodes = 16 # 64 gpus
max_nodes = 25 # 100 gpus

################################################

name = '3dgan-experiment-tf2'

use_curated_env = True
multi_node = True
worker_count=max_nodes # max_nodes
distributed_job_config = None
use_prepro = True # if True GPU_Version2_pp.py will be used instead
script = 'GPU_Version2.py'

region = "fr" # we us

################################################

use_cache = False
use_prefetch = False
use_autotune = False
nb_epochs = 10 #60 #Total Epochs
batch_size = 64 # 96 #batch size
