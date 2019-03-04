import os
import shutil
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

def construct_net(num_features, model_dir):
    """Constructs a 3 layer Deep Neural Net with 10, 20, 10 units"""

    feature_cols = [tf.contrib.layers.real_valued_column("", dimension=num_features)]

    classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_cols,
                                                hidden_units=[10, 20, 10],
                                                n_classes=2,
                                                model_dir=model_dir)

    return classifier

def predict_class(model, binary_mappings, predict_data):
    """Predict classification for new data"""
    binary_prediction = list(model.predict(predict_data))
    return binary_mappings[binary_prediction[0]]
