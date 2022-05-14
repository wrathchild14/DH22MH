#Loading Libraries
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.gridspec import GridSpec
import re
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack
from sklearn.multiclass import OneVsRestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

#Loading Data
resumeDataSet = pd.read_csv('data/UpdatedResumeDataSet.csv' ,encoding='utf-8')


#Data Preprocessing
def cleanResume(resumeText):
    resumeText = re.sub('httpS+s*', ' ', resumeText)  # remove URLs
    resumeText = re.sub('RT|cc', ' ', resumeText)  # remove RT and cc
    resumeText = re.sub('#S+', '', resumeText)  # remove hashtags
    resumeText = re.sub('@S+', '  ', resumeText)  # remove mentions
    resumeText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[]^_`{|}~"""), ' ', resumeText)  # remove punctuations
    resumeText = re.sub(r'[^x00-x7f]',r' ', resumeText) 
    resumeText = re.sub('s+', ' ', resumeText)  # remove extra whitespace
    return resumeText
resumeDataSet['cleaned_resume'] = resumeDataSet.Resume.apply(lambda x: cleanResume(x))
d = {
    "Category": ["Data Science"],
    "cleaned_resume": ["Skills: Microsoft Office package: Microsoft Word, Excel, Access  Statistical operation: SPSS, STATA Programming Languages:  Java, Python, C"]
}

cv_data = pd.DataFrame(d)

print(cv_data.head(5))

var_mod = ['Category']
klasi = resumeDataSet['Category'].values

le = LabelEncoder()
for i in var_mod:
    resumeDataSet[i] = le.fit_transform(resumeDataSet[i])



requiredText = resumeDataSet['cleaned_resume'].values
requiredText1 = cv_data['cleaned_resume'].values


requiredTarget = resumeDataSet['Category'].values
requiredTarget1 = cv_data['Category'].values

#print(f"CLASES: {klasi}")

word_vectorizer = TfidfVectorizer(
    sublinear_tf=True,
    stop_words='english',
    max_features=15)
word_vectorizer.fit(requiredText)
WordFeatures = word_vectorizer.transform(requiredText)


word_vectorizer1 = TfidfVectorizer(
    sublinear_tf=True,
    stop_words='english',
    max_features=15)
word_vectorizer1.fit(requiredText1)
WordFeatures1 = word_vectorizer1.transform(requiredText1)


#Model Building
X_train,X_test,y_train,y_test = train_test_split(WordFeatures,requiredTarget,random_state=2, test_size=0.3)

# print(X_train.shape)
# print(X_test.shape)
# print(X_test)
clf = OneVsRestClassifier(KNeighborsClassifier())
clf.fit(X_train, y_train)
prediction = clf.predict(X_test)




prediction_please = clf.predict(WordFeatures1)

print(f"prediction: {prediction_please}")

# 

#Results
print('Accuracy of KNeighbors Classifier on training set: {:.2f}'.format(clf.score(X_train, y_train)))
print('Accuracy of KNeighbors Classifier on test set: {:.2f}'.format(clf.score(X_test, y_test)))
print("n Classification report for classifier %s:n%sn" % (clf, metrics.classification_report(y_test, prediction)))

