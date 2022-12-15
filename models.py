from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LogisticRegressionCV
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score

sgd=SGDClassifier(n_jobs=-1,random_state=42,max_iter=500)
lgr=LogisticRegression(random_state=42,max_iter=500)
lgrcv=LogisticRegressionCV(cv=2,random_state=42,max_iter=1000)
svm=LinearSVC(random_state=42,max_iter=500)
rfc=RandomForestClassifier(random_state=42,n_jobs=-1,n_estimators=500)

clf={ 'SGD':sgd,
      'LGR':lgr,
      'LGRCV':lgrcv,
      'SVM':svm,
      'RF':rfc }
