# Catmon Image Classifier App: Datasets
This folder stores the *catmon_input* dataset, containing the image data that 
was used to train the catmonic model on landinglens.

This input is split into the *catmon* dataset, one folder for each label, 
ready for model training.

## Create the *catmonic_input* folder
1. Set-up
 - cd to the *root* folder containing the *catmon-img-classifier* project files
2. Download the dataset to the root folder
 - method 1: using the Kaggle CLI:  
```
kaggle datasets download terrydolan/catmon-cats-dataset
```
 - method 2: using Kaggle UI:
     - log on to Kaggle
     - select Datasets
     - search for 'Catmon Cats Dataset'
     - select the 'Download' option
   
3. Extract the images
 - extract contents of *catmon-cats-dataset.zip* to *./datasets/*
4. Verify
 - you should now have a folder *./datasets/catmon_input* containing 
 3 folders:  
```
boo, simba, unknown
```

 - the *boo* folder contains 1000 images of Boo
 - the *simba* folder contains 1000 images of Simba
 - the *unknown* folder contains 793 images in which Boo or Simba cannot be 
   identified

## Dataset structure
The *catmon_input* dataset structure, sources and collection methodology 
are described on the [Kaggle catmon-cats-dataset](https://www.kaggle.com/datasets/terrydolan/catmon-cats-dataset).

## Loading the (reduced) dataset
The current version of the LandingLens model uses the landing Lend free tier. 
The free tier is restricted to 1000 credits. 
It is therefore necessary to use a reduced data set in the training
in order to leave sufficient credits for testing and ongoing classification.

Therefore, a reduced dataset containing the most recent 20% of each class 
data set were uploaded to landinglens.
That is 200 boo images, 200 simba images and 160 unknown images.

Work is ongoing to tailor this dataset to make it more effective, 
particularly for the unkown class.

## Splitting the data ready for training
The LandingLens build was configured to split the train, val and 
test datasets in the ratio: 80, 10, 10.

## Deploying the model
The model, after testing, was deployed to the LandingLens cloud endpoint for 
further evaluation in *Catmon* using live image captures.

Catmon was updated to use the catmonic with LandingLens in February 2025. 
The interface to catmonic is unchanged so this was simple a matter of replacing
the existing Mobilenetv2 catmonic module with the LandingLens catmonic module.

Work is also ongoing to compare the accuracy (etc) of the models.
