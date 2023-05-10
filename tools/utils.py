import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def ohe(data, column):
    ##one hot encoded function##
    enc = OneHotEncoder()
    enc.fit(data[column])
    encoded_data = pd.DataFrame(enc.transform(data[column]).toarray().astype(int))
    encoded_data.columns = enc.get_feature_names_out()
    encoded_data = encoded_data.set_index(data.index)
    return encoded_data

def plot(data, x, kde = True):
    sns.histplot(data = data, x = 'x, hue = 'access_greenblue_spaces', kde = kde,stat = "density", common_norm = False);