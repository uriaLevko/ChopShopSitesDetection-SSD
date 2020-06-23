## detecting chop shops in aerial imagery using SSD Network Architecture

# Contents

[***Objective***](https://github.com/uriaLevko/ChopShopSitesDetection-SSD-#objective)

[***Concepts***](https://github.com/uriaLevko/ChopShopSitesDetection-SSD-#concepts)

[***Overview***](https://github.com/uriaLevko/ChopShopSitesDetection-SSD-#overview)

[***Implementation***](https://github.com/sgrvinod/a-PyTorch-Tutorial-to-Image-Captioning#implementation)

[***Training***](https://github.com/sgrvinod/a-PyTorch-Tutorial-to-Image-Captioning#training)

[***Inference***](https://github.com/sgrvinod/a-PyTorch-Tutorial-to-Image-Captioning#inference)

[***Frequently Asked Questions***](https://github.com/sgrvinod/a-PyTorch-Tutorial-to-Image-Captioning#faqs)

# Objective
Detecting chop-shops sites(also known as car slaghter sites) from aeriel imagery, Using single shot detector

# concepts

* **SSD**. a method for detecting objects in images using a single deep neural network, by discretizes the output space of bounding boxes into a set of default boxes over different aspect ratios and scales per feature map location. At prediction time, the network generates scores for the presence of each object category in each default box and produces adjustments to the box to better match the object shape. 

* **Transfer Learning**. This is when you borrow from an existing model by using parts of it in a new model. This is almost always better than training a new model from scratch (i.e., knowing nothing). As you will see, you can always fine-tune this second-hand knowledge to the specific task at hand. Using pretrained word embeddings is a dumb but valid example. For our image captioning problem, we will use a pretrained Encoder, and then fine-tune it as needed.

# Overview

In this project iv'e Trained a Single-Shot-Detector and feature detection model to detect chop shops in aerial imagery.
The whole process was made using arcgis.learn library, developed by esri, and is based on fast.ai. 


*Below is an example of a 2D robot world with landmarks (purple x's) and the robot (a red 'o') located and found using *only* sensor and motion data collected by that robot. This is just one example for a 50x50 grid world; in your work you will likely generate a variety of these maps.*

<p align="center">
<img src="images/robot_world.png" width=50% height=50% >
</p>

Project Instructions
The project will be broken up into three Python notebooks; the first two are for exploration of provided code, and a review of SLAM architectures, only Notebook 3 and the robot_class.py file will be graded:

[__Notebook 1__](.SSD_FINAL.ipynb) : SSD

[__Notebook 2__](./FeatureC_presentation.ipynb) : feature classifier

[__Notebook 3__](./3.%20Landmark%20Detection%20and%20Tracking%20(2).ipynb) : Landmark Detection and Tracking 

You can also view the helper files writen as part of this project.

[__helper__](./helpers.py) : Init module for robot control

[__Robot__](./robot_class.py): Init module for robot sensing 

LICENSE: This project is licensed under the terms of the MIT license.
