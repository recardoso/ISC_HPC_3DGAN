# 3DGAN Results Microsoft Azure

These runs were performed using Azure's [Machine Learning service](https://azure.microsoft.com/en-us/services/machine-learning/).

#### Batch Size 64 with InfiniBand

The times do not include testing times, only training times.

Using Standard_NC24rs_v3 (InfiniBand, 4 x NVIDIA V100, 24 vCPU, 448 mem.):

| Run | Nodes | Total GPUs | Total Epochs | AUTOTUNE | Logs | Epoch 1 | Epoch 2 | Epoch 3 | Epoch 4 | Epoch 5 |
| ------- | ------- | ------- | ------- | ------ | ------------------------------------------------ | ------- | ------- | ------- | ------- | ------ | ------ | ------ | ----- | ----- | ----- | ----- |
| 1       | 2       | 8       |         | No     | [Logs](https://s3.cern.ch/swift/v1/mlogs/run24)  | 568.91  | 496.91  | 496.83  |         |        |        |        |       |       |       |       |
| 2       | 4       | 16      |         | No     | [Logs](https://s3.cern.ch/swift/v1/mlogs/run27)  | 322.49  | 248.47  | 248.54  |         |        |        |        |       |       |       |       |
| 3       | 8       | 32      |         | No     | [Logs](https://s3.cern.ch/swift/v1/mlogs/run28)  | 200.84  | 126.81  | 126.21  |         |        |        |        |       |       |       |       |
| 4       | 8       | 32      |         | No     | [Logs](https://s3.cern.ch/swift/v1/mlogs/run42)  | 214.19  | 138.51  | 141.33  | 138.16  | 138.04 |        |        |       |       |       |       |
| 5       | 8       | 32      |         | No     | [Logs](https://s3.cern.ch/swift/v1/mlogs/run43)  | 201.20  | 125.12  | 126.29  | 127.03  | 127.21 | 128.30 | 128.64 |       |       |       |       |
| 6       | 8       | 32      |         | No     | [Logs](https://s3.cern.ch/swift/v1/mlogs/run44)  | 221.23  | 141.45  | 140.37  | 139.80  | 139.53 | 139.46 | 144.05 |       |       |       |       |
| 7       | 8       | 32      |         | No     | [Logs](https://s3.cern.ch/swift/v1/mlogs/run45)  | 223.29  | 153.24  | 147.85  | 145.78  | 145.90 | 145.85 | 145.70 |       |       |       |       |
| 8       | 16      | 64      |         | No     | [Logs](https://s3.cern.ch/swift/v1/mlogs/run85)  | 189.46  | 61.90   | 61.68   | 61.66   | 61.69  | 62.12  | 61.75  | 62.46 | 64.36 | 62.81 |       |
| 9       | 16      | 64      |         | Yes    | [Logs](https://s3.cern.ch/swift/v1/mlogs/run86)  | 350.96  | 61.65   | 61.61   | 63.69   | 61.95  | 62.35  | 61.83  | 62.45 | 61.53 | 62.04 |       |
| 10      | 25      | 100     | 120     | No     | [Logs](https://s3.cern.ch/swift/v1/mlogs/run111) | 193.82  | 51.28   | 58.73   | 60.96   | 61.70  | 59.55  | 60.76  | 63.01 | 58.94 | 62.09 | 63.57 |
| 11      | 16      | 64      | 120     | No     | [Logs](https://s3.cern.ch/swift/v1/mlogs/run112) | 186.20  | 79.93   | 81.18   | 80.67   | 80.66  | 80.35  | 80.33  | 81.64 | 80.72 | 81.60 | 80.94 |

* Losses and generator weights
    * Run 10: https://cernbox.cern.ch/index.php/s/SVtfwUBdCBhqnZB
    * Run 11: https://cernbox.cern.ch/index.php/s/RrVIJdYmEWt95oD


#### Batch Size 64 without InfiniBand

The times do not include testing times, only training times.

Using Standard_NC24s_v3 (4 x NVIDIA V100, 24 vCPU, 448 mem.):

Run | Nodes | Total GPUs | AUTOTUNE | Logs | Epoch 1 | Epoch 2 | Epoch 3 | Epoch 4 | Epoch 5 | Epoch 6 | Epoch 7 | Epoch 8 | Epoch 9 | Epoch 10 |
| ------- | ------- | ------- | ------- | ------------------------------------------------ | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ----- | ----- | ----- |
| 1       | 2       | 8       | No      | [Logs](https://s3.cern.ch/swift/v1/mlogs/run25)  | 560.05  | 488.20  | 488.02  |         |         |         |         |       |       |       |
| 2       | 4       | 16      | No      | [Logs](https://s3.cern.ch/swift/v1/mlogs/run26)  | 325.59  | 251.95  | 252.22  |         |         |         |         |       |       |       |
| 3       | 8       | 32      | No      | [Logs](https://s3.cern.ch/swift/v1/mlogs/run33)  | 205.78  | 127.67  | 127.57  |         |         |         |         |       |       |       |
| 4       | 8       | 32      | No      | [Logs](https://s3.cern.ch/swift/v1/mlogs/run34)  | 217.75  | 140.97  | 141.16  |         |         |         |         |       |       |       |
| 5       | 8       | 32      | No      | [Logs](https://s3.cern.ch/swift/v1/mlogs/run35)  | 217.97  | 140.49  | 141.19  |         |         |         |         |       |       |       |
| 6       | 8       | 32      | No      | [Logs](https://s3.cern.ch/swift/v1/mlogs/run36)  | 224.69  | 146.46  | 146.24  |         |         |         |         |       |       |       |
| 7       | 8       | 32      | No      | [Logs](https://s3.cern.ch/swift/v1/mlogs/run37)  | 224.60  | 147.95  | 147.82  | 147.71  | 148.72  | 147.71  | 148.72  |       |       |       |
| 8       | 16      | 64      | No      | [Logs](https://s3.cern.ch/swift/v1/mlogs/run83)  | 186.34  | 63.57   | 63.78   | 63.28   | 64.69   | 65.42   | 63.68   | 63.55 | 63.60 | 66.41 |
| 9       | 16      | 64      | Yes     | [Logs](https://s3.cern.ch/swift/v1/mlogs/run84)  | 345.76  | 63.79   | 63.21   | 63.34   | 63.48   | 63.41   | 64.11   | 63.33 | 63.47 | 63.40 |
| 10      | 25      | 100     | No      | [Logs](https://s3.cern.ch/swift/v1/mlogs/run113) | 186.78  | 50.73   | 51.76   | 55.46   | 53.91   | 54.65   | 53.40   | 54.34 | 53.95 | 53.65 |


#### Batch Size 96 with InfiniBand

The times do not include testing times, only training times.

Using Standard_NC24rs_v3 (InfiniBand, 4 x NVIDIA V100, 24 vCPU, 448 mem.):

Run  | Nodes | Total GPUs | Total Epochs | AUTOTUNE | prefetch or cache | Logs | Epoch 1 | Epoch 2 | Epoch 3 | Epoch 4 | Epoch 5 | Epoch 6 | Epoch 7 | Epoch 8 | Epoch 9 | Epoch 10 | Epoch 11 |
| ------- | ------- | ------- | ------- | ------- | ------- | ----------------------------------------------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| 1       | 6       | 24      |         | No      | No      | [Logs](https://s3.cern.ch/swift/v1/mlogs/run67) | 257.33  | 181.04  | 178.15  | 178.20  | 177.99  | 177.57  | 178.38  | 178.37  | 177.83  | 177.98  |         |
| 2       | 8       | 32      |         | No      | No      | [Logs](https://s3.cern.ch/swift/v1/mlogs/run46) | 199.90  | 119.04  | 118.81  | 119.55  | 118.73  | 119.39  | 119.59  |         |         |         |         |
| 3       | 8       | 32      | 60      | No      | No      | [Logs](https://s3.cern.ch/swift/v1/mlogs/run47) | 200.29  | 118.98  | 119.15  | 119.02  | 119.50  | 119.09  | 119.14  | 119.04  | 119.17  | 119.12  | 119.02  |
| 4       | 8       | 32      | 60      | No      | No      | [Logs](https://s3.cern.ch/swift/v1/mlogs/run48) | 202.94  | 126.17  | 125.88  | 126.20  | 125.88  | 125.74  | 124.46  | 125.96  | 125.55  | 125.80  | 123.52  |
| 5       | 8       | 32      |         | No      | No      | [Logs](https://s3.cern.ch/swift/v1/mlogs/run68) | 199.51  | 120.14  | 120.46  | 120.54  | 119.32  | 119.91  | 119.49  | 120.08  | 120.16  | 120.22  |         |
| 6       | 16      | 64      | 60      | Yes     | No      | [Logs](https://s3.cern.ch/swift/v1/mlogs/run78) | 351.46  | 61.70   | 60.37   | 59.94   | 60.64   | 60.15   | 59.83   | 61.28   | 60.45   | 59.84   | 62.24   |
| 7       | 16      | 64      | 60      | No      | No      | [Logs](https://s3.cern.ch/swift/v1/mlogs/run80) | 181.74  | 59.90   | 60.08   | 60.01   | 59.89   | 59.65   | 59.52   | 60.92   | 60.82   | 63.31   | 59.62   |
| 8       | 25      | 100     | 120     | No      | No      | [Logs](https://s3.cern.ch/swift/v1/mlogs/run93) | 196.66  | 66.44   | 56.22   | 56.34   | 57.24   | 55.15   | 55.29   | 56.45   | 55.76   | 55.23   | 55.10   |
| 9       | 16      | 64      | 120     | No      | No      | [Logs](https://s3.cern.ch/swift/v1/mlogs/run94) | 175.92  | 60.47   | 59.89   | 59.88   | 60.66   | 66.57   | 59.72   | 60.17   | 60.02   | 60.37   | 60.55   |
| 10      | 8       | 32      | 120     | No      | No      | [Logs](https://s3.cern.ch/swift/v1/mlogs/run95) | 204.11  | 120.73  | 120.61  | 120.57  | 120.77  | 120.62  | 120.86  | 120.74  | 120.65  | 120.88  | 120.42  |

* Losses and generator weights
    * Run 8: https://cernbox.cern.ch/index.php/s/1qhtlT9nlGCEVIB
    * Run 9: https://cernbox.cern.ch/index.php/s/uTUm4lxicvP1dtL
    * Run 10: https://cernbox.cern.ch/index.php/s/xXeY8HTDgCoo2un


#### Batch Size 96 without InfiniBand

The times do not include testing times, only training times.

Using Standard_NC24s_v3 (4 x NVIDIA V100, 24 vCPU, 448 mem.):

Run  | Nodes | Total GPUs | Total Epochs | AUTOTUNE | Logs | Epoch 1 | Epoch 2 | Epoch 3 | Epoch 4 | Epoch 5 | Epoch 6 | Epoch 7 | Epoch 8 | Epoch 9 | Epoch 10 | Epoch 11 |
| ------- | ------- | ------- | ------- | ----------- | ----------------------------------------------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------ |
| 1       | 8       | 32      |         | No          | [Logs](https://s3.cern.ch/swift/v1/mlogs/run52) | 200.70  | 120.72  | 120.16  | 120.09  | 120.88  | 120.81  | 120.25  | 121.05  | 120.75  | 120.64  | 120.93 |
| 2       | 8       | 32      |         | No          | [Logs](https://s3.cern.ch/swift/v1/mlogs/run53) | 203.47  | 120.45  | 122.69  | 120.95  | 120.62  | 120.31  | 120.76  | 120.21  | 120.38  | 120.95  |        |
| 3       | 8       | 32      |         | No          | [Logs](https://s3.cern.ch/swift/v1/mlogs/run54) | 217.15  | 130.88  | 130.74  | 128.73  | 131.00  | 128.83  | 129.75  | 128.79  | 129.77  | 127.73  |        |
| 4       | 8       | 32      |         | No          | [Logs](https://s3.cern.ch/swift/v1/mlogs/run56) | 205.27  | 127.27  | 129.81  | 130.55  | 128.61  | 128.94  | 129.57  | 130.52  | 127.17  | 185.97  |        |
| 5       | 16      | 64      | 60      | Yes         | [Logs](https://s3.cern.ch/swift/v1/mlogs/run81) | 349.58  | 61.67   | 61.20   | 61.65   | 61.95   | 61.20   | 61.64   | 61.49   | 61.07   | 60.95   | 61.47  |
| 6       | 16      | 64      | 60      | No          | [Logs](https://s3.cern.ch/swift/v1/mlogs/run82) | 185.10  | 61.30   | 61.76   | 61.24   | 61.05   | 60.85   | 61.18   | 62.12   | 61.20   | 61.00   | 61.11  |



#### Batch Size 32 with InfiniBand

The times do not include testing times, only training times.

Using Standard_NC24rs_v3 (InfiniBand, 4 x NVIDIA V100, 24 vCPU, 448 mem.):

Run  | Nodes | Total GPUs | Total Epochs | AUTOTUNE | prefetch or cache | Logs | Epoch 1 | Epoch 2 | Epoch 3 | Epoch 4 | Epoch 5 | Epoch 6 | Epoch 7 | Epoch 8 | Epoch 9 | Epoch 10 | Epoch 11 |
| ------- | ------- | ------- | ------- | ------- | ------- | ----------------------------------------------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| 1       | 25      | 100     | 120     | No      | No      | [Logs](https://s3.cern.ch/swift/v1/mlogs/run96) | 193.95  | 69.37   | 69.45   | 69.95   | 69.57   | 70.02   | 70.16   | 69.73   | 69.93   | 69.61   | 69.53   |
| 2       | 16      | 64      | 120     | No      | No      | [Logs](https://s3.cern.ch/swift/v1/mlogs/run98) | 188.40  | 108.16  | 107.97  | 111.05  | 107.88  | 108.10  | 107.97  | 109.76  | 108.27  | 108.02  | 108.09  |

* Losses and generator weights
    * Run 1: https://cernbox.cern.ch/index.php/s/qiQdx2PP4jw0USP
    * Run 2: https://cernbox.cern.ch/index.php/s/DySXYSE8DcZI43U


#### Batch Size 16 with InfiniBand

The times do not include testing times, only training times.

Using Standard_NC24rs_v3 (InfiniBand, 4 x NVIDIA V100, 24 vCPU, 448 mem.):

Run  | Nodes | Total GPUs | Total Epochs | AUTOTUNE | prefetch or cache | Logs | Epoch 1 | Epoch 2 | Epoch 3 | Epoch 4 | Epoch 5 | Epoch 6 | Epoch 7 | Epoch 8 | Epoch 9 | Epoch 10 | Epoch 11 |
| ------- | ------- | ------- | ------- | ------- | ------- | ------------------------------------------------ | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| 1       | 25      | 100     | 120     | No      | No      | [Logs](https://s3.cern.ch/swift/v1/mlogs/run102) | 277.64  | 64.59   | 63.68   | 63.47   | 63.78   | 64.45   | 63.69   | 65.16   | 64.11   | 64.65   | 64.33   |
| 2       | 16      | 64      | 120     | No      | No      | [Logs](https://s3.cern.ch/swift/v1/mlogs/run99)  | 199.39  | 91.92   | 92.01   | 91.67   | 91.92   | 92.31   | 92.22   | 92.16   | 91.98   | 91.95   | 92.04   |

* Losses and generator weights
    * Run 1: https://cernbox.cern.ch/index.php/s/DdDPmTTdPciqLem
    * Run 2: https://cernbox.cern.ch/index.php/s/PQRorVusUrpMAJw
