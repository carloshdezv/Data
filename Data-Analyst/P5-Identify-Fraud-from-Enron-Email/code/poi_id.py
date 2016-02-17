#!/usr/bin/python

import sys
import pickle
import pandas as pd
import numpy as np
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi',
                 'salary',
                 'deferral_payments',
                 'total_payments',
                 'loan_advances',
                 'bonus',
                 'restricted_stock_deferred',
                 'deferred_income',
                 'total_stock_value',
                 'expenses',
                 'exercised_stock_options',
                 'other',
                 'long_term_incentive',
                 'total_compensation'] # You will need to use more features

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

### Task 2: Remove outliers

item_to_remove = ['TOTAL', 'THE TRAVEL AGENCY IN THE PARK']
for item in item_to_remove:
    data_dict.pop(item)
    
### Task 3: Create new feature(s)

for key in data_dict:
    #Convert 'NaN' values to 0
    if data_dict[key]['salary'] == 'NaN':
        data_dict[key]['salary'] = 0  
    if data_dict[key]['deferral_payments'] == 'NaN':
        data_dict[key]['deferral_payments'] = 0
    if data_dict[key]['total_payments'] == 'NaN':
        data_dict[key]['total_payments'] = 0  
    if data_dict[key]['loan_advances'] == 'NaN':
        data_dict[key]['loan_advances'] = 0
    if data_dict[key]['bonus'] == 'NaN':
        data_dict[key]['bonus'] = 0 
    if data_dict[key]['restricted_stock_deferred'] == 'NaN':
        data_dict[key]['restricted_stock_deferred'] = 0
    if data_dict[key]['deferred_income'] == 'NaN':
        data_dict[key]['deferred_income'] = 0
    if data_dict[key]['total_stock_value'] == 'NaN':
        data_dict[key]['total_stock_value'] = 0
    if data_dict[key]['expenses'] == 'NaN':
        data_dict[key]['expenses'] = 0
    if data_dict[key]['exercised_stock_options'] == 'NaN':
        data_dict[key]['exercised_stock_options'] = 0
    if data_dict[key]['other'] == 'NaN':
        data_dict[key]['other'] = 0
    if data_dict[key]['long_term_incentive'] == 'NaN':
        data_dict[key]['long_term_incentive'] = 0
    if data_dict[key]['restricted_stock'] == 'NaN':
        data_dict[key]['restricted_stock'] = 0
    if data_dict[key]['director_fees'] == 'NaN':
        data_dict[key]['director_fees'] = 0        
    #Adding total_compensation new feature
    data_dict[key]['total_compensation'] = data_dict[key]['total_payments'] + data_dict[key]['total_stock_value']

### Store to my_dataset for easy export below.
my_dataset = data_dict

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.

#Naive_bayes
#from sklearn.naive_bayes import GaussianNB
#clf = GaussianNB()

#KNeighbors
#from sklearn.neighbors import KNeighborsClassifier
#clf = KNeighborsClassifier(algorithm = 'auto')

#DecisionTree
from sklearn import tree
clf = tree.DecisionTreeClassifier(random_state = 0)



### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

#GridSearchCV
from sklearn import grid_search
parameters = {'criterion': ('entropy','gini'),
              'min_samples_split':[2, 4],
              'splitter': ('random','best'),
              'random_state': (None, 0, 1)
              }
clf2 = grid_search.GridSearchCV(tree.DecisionTreeClassifier(), parameters).fit(features, labels)
print 'best estimator:'
print clf2.best_estimator_

# Tunned DecisionTree
clf = tree.DecisionTreeClassifier(criterion = "entropy", splitter = "random", min_samples_split=2, random_state=0)

# Example starting point. Try investigating other evaluation techniques!
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)
