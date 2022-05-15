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

def ml_model(data):
    resumeDataSet = pd.read_csv('data/UpdatedResumeDataSet.csv', encoding='utf-8')

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

    categories = resumeDataSet["Category"].unique()
    print(categories)

    var_mod = ['Category']

    le = LabelEncoder()
    for i in var_mod:
        resumeDataSet[i] = le.fit_transform(resumeDataSet[i])

    requiredText = resumeDataSet['cleaned_resume'].values
    requiredText1 = data['cleaned_resume']

    requiredTarget = resumeDataSet['Category'].values

    word_vectorizer = TfidfVectorizer(
        sublinear_tf=True,
        stop_words='english',
        max_features=80)
    word_vectorizer.fit(requiredText)
    WordFeatures = word_vectorizer.transform(requiredText)


    word_vectorizer1 = TfidfVectorizer(
        sublinear_tf=True,
        stop_words='english',
        max_features=80)
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

    prediction_new = clf.predict(WordFeatures1)

    print(f"prediction: {categories[prediction_new]}")

    return categories[prediction_new]