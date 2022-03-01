## LandCoverNet Data Exploration

<img src='https://radiant-assets.s3-us-west-2.amazonaws.com/PrimaryRadiantMLHubLogo.png' alt='Radiant MLHub Logo' width='300'/>

This tutorial delves into building a scalable model on the LandCoverNet dataset.

The tutorial is split into three notebooks:

### 1. Data Exploration
In this notebook, a portion of the tutorial:

1. We will authenticate to MLHub via the API key to make requests on the LandCoverNet label collection

2. We will download the label collection into PC

3. We will perform some exploratory data analysis on these labels to get a better understanding of the LandCoverNet data

### 2. Data Preparation

This portion of the tutorial is focused on preparing the data for training a semantic segmentation model for LandCoverNet data.
Here:

1. We will inspect the source imagery for the labels we have

2. We will process the source imagery in parallel using Dask

3. We will select the labels and filtered source images from Dask to be loaded

4. We will save the images and associated labels data as a pickle file ('.pkl') on our directory to be loaded for model training

### 3. Model Training

This portion of the tutorial is focused on developing a semantic segmentation model for LandCoverNet data.
Here:

1. We will load the prepared data as training, test and validation data

2. We will build a segmentation model, train it on the training data, inspect the results on the validation data and make predictions on the test data

## How To Get Started

1. Login to Planetary Computer's JupyterLab hub.
2. CD to the directory you're working on
3. Run the command: `pip install -r requirements.txt`
4. Use the `1. Data Exploration` notebook and follow the instructions
5. Use the `2. Data Preparation` notebook and follow the instructions 
6. Use the `3. Model Training` notebook and follow the instructions (preferably use the Tensorflow GPU server for faster training results)
