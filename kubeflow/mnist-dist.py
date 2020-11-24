#!/usr/bin/env python
# coding: utf-8

# In[121]:


import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
from tensorflow.keras.models import load_model
import json

print(tf.__version__)


# In[122]:


nodes_number = 8
learning_rate = 0.0001


# # MNIST classification

# In[123]:


(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train, x_test = x_train[..., np.newaxis]/255.0, x_test[..., np.newaxis]/255.0

def filter_36(x, y):
    keep = (y == 3) | (y == 6)
    x, y = x[keep], y[keep]
    y = y == 3
    
    return x, y

print("Number of unfiltered training examples:", len(x_train))
print("Number of unfiltered test examples:", len(x_test))

x_train, y_train = filter_36(x_train, y_train)
x_test, y_test = filter_36(x_test, y_test)

print("Number of filtered training examples:", len(x_train))
print("Number of filtered test examples:", len(x_test))


# In[125]:


strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy(tf.distribute.experimental.CollectiveCommunication.NCCL)
print ('Number of devices: {}'.format(strategy.num_replicas_in_sync))

batch_size = 1024
print('batch_size', batch_size)

BATCH_SIZE_PER_REPLICA = batch_size

print('BATCH_SIZE_PER_REPLICA', str(BATCH_SIZE_PER_REPLICA))
print('strategy.num_replicas_in_sync', str(strategy.num_replicas_in_sync))

batch_size = batch_size * strategy.num_replicas_in_sync
print('batch_size', batch_size)

batch_size_per_replica=BATCH_SIZE_PER_REPLICA
print('batch_size_per_replica', batch_size_per_replica)

dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train)).batch(batch_size)

strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy(tf.distribute.experimental.CollectiveCommunication.NCCL)
print ('Number of devices: {}'.format(strategy.num_replicas_in_sync))

batch_size = 4
print('batch_size', batch_size)

BATCH_SIZE_PER_REPLICA = batch_size

print('BATCH_SIZE_PER_REPLICA', str(BATCH_SIZE_PER_REPLICA))
print('strategy.num_replicas_in_sync', str(strategy.num_replicas_in_sync))

batch_size = batch_size * strategy.num_replicas_in_sync
print('batch_size', batch_size)

batch_size_per_replica=BATCH_SIZE_PER_REPLICA
print('batch_size_per_replica', batch_size_per_replica)

dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train)).batch(batch_size)

"""with strategy.scope():
    image=Input(shape=(28, 28, 1))
    
    out = tf.keras.layers.Conv2D(32, [5, 5], activation='relu', input_shape=(28,28,1))(image)
    out = tf.keras.layers.Conv2D(32, [5, 5], activation='relu')(out)
    out = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))(out)
    out = tf.keras.layers.Dropout(0.25)(out)
    out = tf.keras.layers.Flatten()(out)
    
    out = tf.keras.layers.Dense(nodes_number, activation='relu')(out)
    out = tf.keras.layers.Flatten()(out)
    out = tf.keras.layers.Dense(1)(out)
    
    model = Model(image, out)

    model.compile(loss='binary_crossentropy', optimizer=tf.keras.optimizers.Adam())

model.summary()"""

with strategy.scope():
    model = load_model('/eos/user/d/dgolubov/distr/debug-0-worker-0.h5')
    model.compile(loss='binary_crossentropy', optimizer=tf.keras.optimizers.Adam())

#tf_config_str = str(os.getenv('TF_CONFIG'))
#tfconfig_dict = dict(json.loads(tf_config_str))
#tfconfig_dict = {"cluster":{"worker":["gan3d-workers-debugging-g8pk4wwj-worker-0.dejan-golubovic.svc:2222","gan3d-workers-debugging-g8pk4wwj-worker-1.dejan-golubovic.svc:2222"]},"task":{"type":"worker","index":0},"environment":"cloud"}
#worker_id = str(tfconfig_dict['task']['index'])

#print(x_train.shape, y_train.shape)
for batch_ind, batch in enumerate(dataset):
    print('Batch ' + str(batch_ind))
    print(batch[0].shape)
    print(batch[1].shape)
    
    #with open('/eos/user/d/dgolubov/distr/debug-' + str(batch_ind) + '-worker-' + worker_id + '.txt', 'w') as fd:
    #    fd.write('Worker ' + worker_id + ' processing batch ' + str(batch_ind) + ', shape ' + str(batch[0].shape))
    #    fd.write('\nWeights:\n')
    #for weight in model.get_weights():
        #print(str(weight.flatten()[:10]))
    
    
    #model.save('/eos/user/d/dgolubov/distr/debug-' + str(batch_ind) + '-worker-' + worker_id + ".h5")
    #model.train_on_batch(batch[0], batch[1])
    
    predictions = model.predict_on_batch(batch[0])
    print('predictions.shape' + str(predictions.shape))
    print('predictions' + str(predictions.flatten()))
    
    break