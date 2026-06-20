# Catmon Image Classifier

## Introduction

The *Catmon Image Classifier* (aka *Catmonic*) classifies a *Catmon* image
with the cat's name and a probability.
The classifier returns a label and a probability; there are 3 possible labels:
'boo', 'simba' or 'unknown'.

It uses a pre-built LandingLens ConvNext-\[29M\] model trained with the 
catmon dataset and deployed on the LandingLens cloud.
This model is more accurate than the previous MobileNetv2 model. 

*Catmonic* uses the LandingLens API, thereby avoiding the needs to run the 
classification model locally.
This is particularly useful on a Raspberry Pi, the target compute hardware of 
*Catmon*.

## Catmonic Deployment

The *Catmonic* module is used by the *Catmon* app to classify cat images.
The app is deployed on a raspberry pi 3B+ and runs continuously, applying
the *Catmonic* deep learning CNN model to the *Catmon* images via an API call 
to the model's deployed cloud endpoint.

The app's classification is tweeted on social media and therefore available for 
viewing.
Here is an example automatic tweet from *Catmon* with the LandingLens
ConvNext-[29M] model:  
<img src="https://raw.githubusercontent.com/terrydolan/catmonic-landinglens/main/images/catmonic_landinglens_classification_example_2026-06-18_115835.jpg](images/catmonic_landinglens_classification_example_2026-06-18_115835.jpg)" width="300">

## Catmonic's Test App

The catmonic cli app, in the *catmonic-app* folder, uses *Catmonic* to
classify a given image.
There are some example images in the *images* folder.

## Datasets

The *catmon_input* folder containing the image data is available on Kaggle
for download.
See the *./datasets/DATASETS_README.md* file for more information on the
structure of the image data and how to download and split the data.

## Key Project Files

The './catmonic/catmonic.py' is the main python implementation, a simple class
that wrappers the catmon image classifier.

The './catmonic-app/catmonic_cli_app.py' is a simple python command line app
that
classifies a given catmon image file using catmonic.

## Usage

### Run The Catmonic Test App
Run the app from the catmonic-app folder:
```
$python catmonic_cli_app.py image_path
```
Run one of the app's test scripts from the catmonic-app folder for your 
operating system e.g.:
```
./catmonic-app/catmonic_cli_app_test_boo.sh
```

### Use The Catmonic Classifier
Example usage snippet:
```
import catmonic.catmonic as catmonic
# Instantiate the catmonic classifier object and classify the image
catmonic_clf = catmonic.Catmonic()
label, probability, model_name = (catmonic_clf.predict_catmon_image(pil_image))
```

## Installation of Catmonic as a package
*Catmonic* with LandingLens can also be installed as a package. 
It is used this way in the *Catmon* app.  
To install catmonic-landinglens as a package:
- git clone the catmonic-landinglens repo to say project-catmonic-landinglens
- cd project-catmon (or whatever your sibling project is that is using the 
  *Catmonic* classifier)
- activate your virtual environment (recommended)
- install the package in the venv:
```
pip install -e ../project-catmonic-landinglens
```
- use the catmonic classifier as described above


## Related Catmon Projects
See the [Catmon repo](https://github.com/terrydolan/catmon) for a 
description of *Catmon* and the related projects.

Terry Dolan  
June 2026