#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Catmon image classifier module.

    Provide a simple class that wrappers the catmon image classifier, also
    known as catmonic.


    Catmonic calls the pre-trained landinglens catmonic classification model endpoint,
    deployed on the landinglens cloud, and provides a predict_catmon_image() method to
    classify the given catmon image.

    The classifier returns the label, the probability and the model name.

    The landinglens catmonic project trained a ConvNext-[29M] model using labelled catmon
    images.

    The classifier identifies 3 class names / labels:
    'boo', 'simba' or 'unknown'.

    Author: Terry Dolan

    Note:
    1. catmonic (with MobileNetV2 model) was originally embedded within a
    standalone tweet handler application. It was moved to a module to make
    it more maintainable and to allow it to be included in other apps.
    2. this latest beta version modifies the Catmonic class to use a more
    powerful model deployed in the landinglens cloud

    References:
    - For more information on the catmon* solution see the associated GitHub
    projects.

    To Do:

    Changes:
    1. 11th February 2024: Cloned catmonic (gitHub: terrydolan/catmon-img-classifier) and modified
    to use landinglens model.

"""

# ----------------------------------------------------------------------------
# define code meta data
__author__ = "Terry Dolan"
__maintainer__ = "Terry Dolan"
__copyright__ = "Terry Dolan"
__license__ = "MIT"
__email__ = "terry8dolan@gmail.com"
__status__ = "Beta"
__version__ = "0.1.0"
__updated__ = "February 2025"

# ----------------------------------------------------------------------------
# define imports
import os
from dotenv import load_dotenv
from landingai.predict import Predictor

# ----------------------------------------------------------------------------
# define Catmonic class


class Catmonic:

    def __init__(self):
        # define the classification model
        self.model_name = "LandingLens ConvNext-[29M]"

        # load the environment variables from the .env file
        load_dotenv()

        # define the landinglens model endpoint id and api key
        self.landinglens_api_key = os.getenv("LANDINGLENS_API_KEY")
        self.model_endpoint_id = os.getenv("MODEL_ENDPOINT_ID")

    def predict_catmon_image(
            self,
            pil_image):
        """Apply classification model and return the
        predicted label, probability and model name."""

        # classify the image
        predictor = Predictor(self.model_endpoint_id, api_key=self.landinglens_api_key)
        prediction = predictor.predict(pil_image)[0]
        label = prediction.label_name  # labels: 'boo', 'simba' or 'unknown'
        probability = prediction.score

        return label, probability, self.model_name
