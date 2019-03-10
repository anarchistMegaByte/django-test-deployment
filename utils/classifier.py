import os
import shutil
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
manav = []
def construct_net(num_features, model_dir):
    """Constructs a 3 layer Deep Neural Net with 10, 20, 10 units"""

    feature_cols = [tf.contrib.layers.real_valued_column("", dimension=num_features)]

    classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_cols,
                                                hidden_units=[10, 20, 10],
                                                n_classes=2,
                                                model_dir=model_dir)

    return classifier

def ret_ans(x):
    return x
def predict_class_new(model, binary_mappings,x):
    """Predict classification for new data"""
    print(x)
    print(type(x))
    binary_prediction = list(model.predict_classes(input_fn=lambda: ret_ans(x)))

    print("\nClass Prediction: %s\n" % binary_mappings[binary_prediction[0]])
    
    binary_prediction = list(model.predict_proba(x))
    print(binary_prediction[0])
    benign = binary_prediction[0][0]*100
    malignant = binary_prediction[0][1]*100
    cancer_type = {}
    if (benign > malignant):
        cancer_type["type"] = "benign"
        cancer_type["probability"] = benign
    else:
        if benign < malignant:
            cancer_type["type"] = "malignant"
            cancer_type["probability"] = malignant
        else:
            cancer_type["type"] = "malignant"
            cancer_type["probability"] = malignant
    # return binary_mappings[binary_prediction[0]]
    return cancer_type
