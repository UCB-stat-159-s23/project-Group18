import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
import sklearn
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn import tree
from sklearn.metrics import roc_curve, roc_auc_score
from tools.utils import ohe;


df = pd.read_csv('../../data/CitieSHealth_BCN_DATA_PanelStudy_20220414_Clean.csv')
numerical = list((df.dtypes[df.dtypes == 'float64'].index) | (df.dtypes[df.dtypes == 'int64'].index))
categorical = list((df.dtypes[df.dtypes != 'float64'].index) & (df.dtypes[df.dtypes != 'int64'].index))


def test_ohe():
    ohe_df = pd.concat([df[numerical], ohe(df[categorical], categorical)], axis=1)
    assert ohe_df.shape [1] == 24