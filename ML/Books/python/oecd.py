import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn

# *Hands-on Machine Learning with Scikit-Learn & TensorFlow by Aurelien Geron(O'Reilly). Copyright 2017 Aurelien Geron, 978-1-491-96229-9* #

def prepare_country_stats(oecd_bli, gdp_per_capita):
    oecd_bli = oecd_bli[oecd_bli["INEQUALITY"]=="TOT"]
    oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value")
    gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)
    gdp_per_capita.set_index("Country", inplace=True)
    full_country_stats = pd.merge(left=oecd_bli, right=gdp_per_capita,
                                  left_index=True, right_index=True)
    full_country_stats.sort_values(by="GDP per capita", inplace=True)
    remove_indices = [0, 1, 6, 8, 33, 34, 35]
    keep_indices = list(set(range(36)) - set(remove_indices))
    return full_country_stats[["GDP per capita", 'Life satisfaction']].iloc[keep_indices]


oecd = pd.read_csv("../data/OECD.csv", thousands=',')
gdp = pd.read_csv("../data/GDP.csv", thousands=',', delimiter='\t', encoding='latin1', na_values="n/a")

country_stats = prepare_country_stats(oecd, gdp)
X = np.c_[country_stats["GDP per capita"]]
y = np.c_[country_stats["Life satisfaction"]]
country_stats.plot(kind='scatter', x="GDP per capita", y='Life satisfaction')
plt.show()

model = sklearn.linear_model.LinearRegression()
model.fit(X, y)



