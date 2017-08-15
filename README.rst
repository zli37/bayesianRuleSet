Bayesian Rule Set Mining

Find the rule set from the data
The input data should follow the following format:
X has to be a pandas DataFrame
all the column names can not contain '_' or '<'
and the column names can not be pure numbers
The categorical data should be represented in string
(For example, gender needs to be 'male'/'female',
 or '0'/'1' to represent male and female respectively.)
The parser will only recognize this format of data.
So transform the data set first before using the
functions.
y hass to be a numpy.ndarray

reference:
Wang, Tong, et al. "Bayesian rule sets for interpretable classification." 
Data Mining (ICDM), 2016 IEEE 16th International Conference on. IEEE, 2016.

The program is very picky on the input data format
X needs to be a pandas DataFrame,
y needs to be a nd.array

    Parameters
    ----------
    max_rules : int, default 5000
        Maximum number of rules when generating rules

    max_iter : int, default 200
        Maximun number of iteratations to find the rule set

    chians : int, default 1
        Number of chains that run in parallel

    support : int, default 5
        The support is the percentile threshold for the itemset
        to be selected.

    maxlen : int, default 3
        The maximum number of items in a rule

    #note need to replace all the alpha_1 to alpha_+
    alpha_1 : float, default 100
        alpha_+

    beta_1 : float, default 1
        beta_+

    alpha_2 : float, default 100
        alpha_-

    beta_2 : float, default 1
        beta_-

    alpha_l : float array, shape (maxlen+1,)
        default all elements to be 1

    beta_l : float array, shape (maxlen+1,)
        default corresponding patternSpace

    level : int, default 4
        Number of intervals to deal with numerical continous features

    neg : boolean, default True
        Negate the features

    add_rules : list, default empty
        User defined rules to add
        it needs user to add numerical version of the rules

    criteria : str, default 'precision'
        When there are rules more than max_rules,
        the criteria used to filter rules

    greedy_initilization : boolean, default False
        Wether start the rule set using a greedy
        initilization (according to accuracy)

    greedy_threshold : float, default 0.05
        Threshold for the greedy algorithm
        to find the starting rule set

    propose_threshold : float, default 0.1
        Threshold for a proposal to be accepted

    method : str, default 'fpgrowth'
        The method used to generate rules.
        Can be 'fpgrowth' or 'forest'
        Notice that if there are potentially many rules
        then fpgrowth is not a good method as it will
        have memory issue (because the rule screening is
        after rule generations).


Sample usage:

import ruleset as rs
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


df = pd.read_csv('data/adult.dat', header=None, sep=',', names=['age', 'workclass', 'fnlwgt', 'education', 'educationnum', 'matritalstatus', 'occupation', 'relationship', 'race', 'sex', 'capitalgain', 'capitalloss', 'hoursperweek', 'nativecountary', 'income'])
y = (df['income'] == '>50K').as_matrix()
df.drop('income', axis=1, inplace=True)

X_train, X_test, y_train, y_test = train_test_split(
    df, y, test_size=0.3)

model = rs.BayesianRuleSet(method='forest')
model.fit(X_train, y_train)
yhat = model.predict(X_test)
TP, FP, TN, FN = rs.get_confusion(yhat, y_test)
