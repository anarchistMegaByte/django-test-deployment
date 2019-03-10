##################################
########### Training #############
##################################

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib

from sklearn.metrics import accuracy_score, recall_score, f1_score, roc_auc_score, make_scorer
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import precision_score
from sklearn.model_selection import cross_val_score
import logging

#logging level
logging.basicConfig(level=logging.INFO)
Logger = logging.getLogger('RandomClf.stdout')
Logger.setLevel("INFO")


#Age
# number of sexual partners
# number of pregnancies
# Smokes
# Hormonal Cnoteceptives
# First sexual inrercourse
# STD's number of diagnoses
# Cytology
# STD's: Condylomatosis
def clev_main():

    df_cancer = pd.read_csv('kag_risk_factors_cervical_cancer.csv')
    df_cancer = df_cancer.replace('?', np.nan)
    # df_cancer = df_cancer.drop(DROP_COLUMNS, axis = 1)
    df_cancer = df_cancer.rename(columns={'Biopsy': 'Cancer'})
    df_cancer = df_cancer.apply(pd.to_numeric)
    df_cancer = df_cancer.fillna(df_cancer.mean().to_dict())

    list_all = list(df_cancer)
    list_needed = ['Age', 'Number of sexual partners', 'Num of pregnancies', 'Smokes', 'Hormonal Contraceptives', 'First sexual intercourse', 'STDs: Number of diagnosis', 'Citology', 'STDs:condylomatosis', 'Cancer']
    list_to_drop = [x for x in list_all if x not in list_needed]

    final_df = df_cancer.drop(list_to_drop, axis=1)

    X = final_df.drop('Cancer', axis=1)
    y = final_df['Cancer']

    print(df_cancer.head())

    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True, test_size = 0.25,random_state=2019)
    # random_forest = RandomForestClassifier(n_estimators=500, random_state=2019).fit(X_train, y_train)

    Logger.info ("Gonna perform classification with C-RandomForest")

    # Assuming RandomForest is the only classifier we are gonna try, we will set the n_estimators parameter as follows.
    Parameters = {'n_estimators': [10,50,100,200,500,1000], 'bootstrap': [True, False], 'criterion': ['gini', 'entropy']}
    my_scorer = make_scorer(f1_score, greater_is_better=True, average='micro')
    Clf = GridSearchCV(RandomForestClassifier(), Parameters,  cv=5, scoring = my_scorer, n_jobs=-1)
    RFmodels = Clf.fit(X_train, y_train)

    BestModel = RFmodels.best_estimator_
    filename = 'clev_model.sav'
    joblib.dump(BestModel, filename)
    Logger.info('CV done - Best model selected: {}'.format(BestModel))
    y_pred = BestModel.predict(X_test)
    print('Accuracy score: ' + str(accuracy_score(y_test, y_pred)))
    return 'Accuracy score: ' + str(accuracy_score(y_test, y_pred))


#random input
# input_data = {
#         "Age": [24.0],
#         "Number of sexual partners": [3.0],
#         "First sexual intercourse": [26.0],
#         "Num of pregnancies": [4.0],
#         "Smokes": [5.0],
#         "Hormonal Contraceptives": [1.0],
#         "STDs:condylomatosis": [0.0],
#         "STDs: Number of diagnosis": [0.0],
#         "Citology": [1.0]
#         # "Cancer": [0.0],
#     }
# input from csv
# input_data = {
#         "Age": [44.0],
#         "Number of sexual partners": [3.0],
#         "First sexual intercourse": [26.0],
#         "Num of pregnancies": [4.0],
#         "Smokes": [0.0],
#         "Hormonal Contraceptives": [1.0],
#         "STDs:condylomatosis": [0.0],
#         "STDs: Number of diagnosis": [0.0],
#         "Citology": [0.0]
#         # "Cancer": [0.0],
#     }

def clev_can_pred(input_data):
    # list_needed = ['Age', 'Number of sexual partners', 'Num of pregnancies', 'Smokes', 'Hormonal Contraceptives', 'First sexual intercourse', 'STDs: Number of diagnosis', 'Citology', 'STDs:condylomatosis', 'Cancer']
    pred = pd.DataFrame(input_data, index=[0])
    # pred = pred.drop('Cancer', axis=1)
    filename = 'clev_model.sav'
    rfc = joblib.load(filename)

    YPred = rfc.predict_proba(pred)
    print(rfc.classes_)
    print("Result - " , YPred)
    data = {
            "percentage": YPred[0][1]*100
        }
    return data