from models import clf
from Data_processing import *
from sklearn.metrics import accuracy_score
import pickle
import os 
def get_max_ac(d):
  return max(d, key = d.get)

Models_name={'SGD':'SGD(Classifier)',
             'LGR':'LogisticRegression',
             'LGRCV':'Logistic RegressionCV',
             'SVM':'LinearSupport Vector Machine',
             'RF':'RandomForest Classifier'}
main_dir='/media/sahitya/OS/10_sec'

def train_model(f):
    accuracy_dict={}
    "train->(model,f)"
    x_train,x_test,y_train,y_test=split(f)
    y_train=y_train.values.ravel()
    y_test=y_test.values.ravel()
    for key in clf.keys():
         print(f'Training--------------------->{Models_name[key]}')
         clf[key].fit(x_train,y_train)
         y_pred=clf[key].predict(x_test)
         print(f'Models : {Models_name[key]}{(key)},===>,Accuracy : {accuracy_score(y_test,y_pred)}')
         accuracy_dict[key]=accuracy_score(y_test,y_pred)
    best_model=get_max_ac(accuracy_dict)
    print(f'Best Model: {Models_name[best_model]}, Accuracy : {accuracy_dict[best_model]}')
    ins=input('Save the best_model(yes/no):')
    print('Saving the best model------------------------->')
    m=0
    if ins=='yes':
        m=1
        with open('/media/sahitya/OS/10_sec/best_models/best_model.pkl', 'wb') as files:
                pickle.dump(clf[key], files)
    return m




