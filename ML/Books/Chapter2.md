# Hands-on ML with Scikit-Learn & TensorFlow by Aurelien Geron  Chapter 2 #

## List of Open Source Datasets ##

- UC Irvine Machine Learning
- Kaggle Datasets
- Amazon AWS datasets
- Dataportals
- Opendatamonitor
- quandl

## Look at the Big Picture ##

In the book, they give us the objective to build a model to predict the price of house in a district.

How does the co;pany expect to use and to benefit the model is the first question to ask ourself.

It will also determine the amount of resources to allocate to the project.

The answer is that the model's output will be fed to another Machine Learning system, along with many other signals. This downstream system will determine whether it is worth investing in a given area or not. => important task because others model depends on it.

This is a ML Pipeline : With the district Data, the model should predict the district prices. With this and the other signal, the investment analysis system will determine whether it is worth investing in a given area or not.

**What is a Pipeline** : A sequence of data processing components is called a data pipeline. Pipelines are very common in Machine Learning systems, since there is a lot of data to manipulate and many data transformations to apply.

Components are asynchronous : Like they can check the district price twice a month but only run the investment analysis one a months. Different teams can work on each component of the pipeline as long as the data is proprely communicated.

This also can be a problem if not enough monitoring is done. Since a bad component can go unnoticed for a long period of time and the whole pipeline will be affected.

Then you think about the problem, you have the district data and you need to analyze the price for the futures => This is a supervised learning task since you are given labeled training data. Since you are given the task to predict a value => This is a regression task. More specifically, this is a multivariate regression problem since the system will use multiple features to make a prediction.

The data is also not continuous so a simple batch learning should do just fine since there is no need to adjust to rapidly changing data.

## Select a Performance Measure ##

A typical performance measure for regression problems is the Root Mean Square Error (RMSE). It gives an idea of how much error the system typically makes in its predictions, with a higher weight for large errors.

``` math
RMSE (X,h) = sqrt(1/m * sum(h(x^i) - y^i)^2)
```

m = the number pf instances in the dataset you are measuring the RMSE on.
x^i = a vector of all the feature values (excluding the label) of the ith instance in the dataset, and y^i is its label (the desired output value for that instance).
X is a matrix containing all the feature values (excluding labels) of all instances in the dataset.
h is your system's prediction function, also called a hypothesis.

If there is many outliers district for example, we could choose the MEA = Mean Absolute Error.

``` math
MAE (X,h) = 1/m * sum(abs(h(x^i) - y^i))
```

Both RMSE and MAE are ways to measure the distance between two vectors: the vector of predictions and the vector of target values.

## Check the Assumptions ##

We need to check the Assumptions. Like in this case , i can tell ;yself = Maybe i just need to say if this is low, mid or high price for this district. But if i talk to the team responsible for the next component of the pipelinem, they would tell me the exact price is required.

## Create the workspace ##

``` bash

pip3 install --user --upgrade virtualenv
sudo apt-get install python3.11-dev python3.11-venv
python3.11 -m venv $PWD
source ./bin/activate
pip3.11 install --upgrade jupyter matplotlib numpy pandas scipy scikit-learn imbalanced-learn
python3.11 -c "import jupyter, matplotlib, numpy, pandas, scipy, sklearn, imblearn" # to check if all the packages are installed
jupyter notebook # to start the notebook
ipython kernel install --user --name=venv
deactivate # to exit the virtualenv

```

Notebook is ./notebook/housing.ipynb
