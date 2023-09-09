# Hands-on ML with Scikit-Learn & TensorFlow by Aurelien Geron #

- [Hands-on ML with Scikit-Learn \& TensorFlow by Aurelien Geron](#hands-on-ml-with-scikit-learn--tensorflow-by-aurelien-geron)
	- [Fundamentals of ML](#fundamentals-of-ml)
	- [Types of ML Systems](#types-of-ml-systems)
		- [Supervised / Unsupervised Learning](#supervised--unsupervised-learning)
			- [Supervised Learning](#supervised-learning)
			- [Unsupervised Learning](#unsupervised-learning)
			- [Semisupervised Learning](#semisupervised-learning)
			- [Reinforcement Learning](#reinforcement-learning)
		- [Batch and Online Learning](#batch-and-online-learning)
			- [Batch Learning](#batch-learning)
			- [Online Learning](#online-learning)
		- [Instance-Based versus Model-Based Learning](#instance-based-versus-model-based-learning)
			- [Instance-based learning](#instance-based-learning)
			- [Model-based learning](#model-based-learning)
	- [Main Challenges of ML](#main-challenges-of-ml)
		- [Bad Data](#bad-data)
			- [Insufficient Quantity of Training Data](#insufficient-quantity-of-training-data)
			- [Nonrepresentative Training Data](#nonrepresentative-training-data)
			- [Poor-Quality Data](#poor-quality-data)
			- [Irrelevant Features](#irrelevant-features)
			- [Overfitting the Training Data](#overfitting-the-training-data)
			- [Underfitting the Training Data](#underfitting-the-training-data)
			- [TLDR](#tldr)
	- [Testing and Validating](#testing-and-validating)
		- [No Free Lunch Theorem](#no-free-lunch-theorem)
	- [Exercices](#exercices)

*Hands-on Machine Learning with Scikit-Learn & TensorFlow by Aurelien Geron(O'Reilly). Copyright 2017 Aurelien Geron, 978-1-491-96229-9*

## Fundamentals of ML ##

*"Machine Learning is the field of study that gives computers the ability to learn without being explicitly programmed"* **- Arthur Samuel, 1959**

**Example :** Spam filter

1. Traditional approach :

   - Study the problem
   - Write rules
   - Evaluate  => Analyze errors => back to step 1
   - Launch

    With time, more and mores rules, will be added and become hard to maintain

2. Machine Learning approach :

   - Study the problem
   - With the help of data, train a ML algorithm
   - Evaluate => analyze errors => back to step 1
   - Launch

Since we trained the model with data, if scammers update their emails, with the ML approach, we just need to update the data to retrain the model, which can be automated.

Another Area where ML shines is too complex problems for traditionnal approaches such as Speech Recognition.

It also helps humans to learn with their ability to dig into large amounts of data to discover patterns => **Data mining**

**TLDR** ML is great for :

- Problems which requires a lot of rules
- Complex problems too big to handle with a traditionnal approach
- Fluctuating environnement which need adaptation to new data
- Getting insights about complex problems and large amounts of data

## Types of ML Systems ##

### Supervised / Unsupervised Learning ###

4 Types :

- Supervised learning (SL)
- Unsupervised learning (UL)
- SemiSupervised learning (SSL)
- Reinforcement learning (RL)

#### Supervised Learning ####

The training data you feed to the algorithm includes the desired solutions, called **labels**.
Typical task => **Classification** (i.e. spam filter)

Typical task => Predict a **target** numeric value (i.e. price of a car) given a set of **features** (i.e. mileage, age, brand, etc.) called **predictors**. =>  this task is called **Regression**.

To train the system, you need to give it many examples of cars, including both their predictors and their labels (i.e. their prices).

In ML, an **attribute** is a data type.

A **features** is an attribute plus its value.

#### Unsupervised Learning ####

The training data is unlabeled. The system tries to learn without a teacher.
Most importants type of UL:

- **Clustering** : detect groups of similar instances in the data => i.e. segmentation => recommender system
- **Visualization and Dimensionality reduction** : simplify the data without losing too much information, which help to detect unsuspected patterns => i.e. data visualization
  - **Dimensionality reduction** : **Feature extraction** => merge several correlated features into one => i.e. car mileage and age into a "car wear" feature
- **Anomaly detection** : detect abnormal instances => i.e. defective products in a factory
- **Association rule learning** : dig into large amounts of data and discover interesting relations between attributes => i.e. Market basket analysis

#### Semisupervised Learning ####

Some algorithms can deal with partially labeled training data, usually a lot of unlabeled data and a little bit of labeled data.

Most semisupervised learning algorithms are combinations of unsupervised and supervised algorithms.

#### Reinforcement Learning ####

The learning system, called an **agent** in this context, can observe the environment, select and perform actions, and get **rewards** in return (or **penalties** in the form of negative rewards) => Need to learn by itself = **Policy**, it defines what action the agent should choose when it is in a given situation. ex: AlphaGo.

### Batch and Online Learning ###

Another criterion used to classify ML systems is whether or not the system can learn incrementally from a stream of incoming data.

#### Batch Learning ####

The system is incapable of learning incrementally : it must be trained using all the available data => **Offline Learning**.

We can update it fairly easily, even online. Like just take the new data, retrain the model and replace the old one with the new one. You can do it like once a day or a week. But this is not adapted if your data is huge or if you need to be reactive. ex : Stock Prices.

There is also the problen of having to train the model on the whole data set, which can take hours or days but mostly ressources => **Money** (CPU, disk space, etc.) Or if you have limited ressources like Mars Rover, you can't let him carry a large amounts of data to retrain the model.

#### Online Learning ####

Train the system incrementally by feeding it data instances sequentially, either individually or by small groups called **mini-batches**. => reat for data with continuous flow (ie stocks). Also great for limited ressources => You have a trained model, you use it, you get data, you retrain the model, then you discard it

It can also be used to train huge datasets that the machine can't handle => **Out of core learning**

**CAUTION** : Online learning can be done offline, the name is confusing => Its more like incremental learning.

The challenge with incremental learning is the **learning rate**
If it's too fast, you will quickly forget the old data => not useful in certain cases

If it's too slow, you will adapt too slowly to the new data, but will be less sensitive to noise => not useful in certain cases

If too much bad data is fed to the system, the model can gradually decline (ie dysfunctions in a captor) => You need to monitor your system and react to its performance drop => **Performance Measure** and data backups

You can also implement a way to react to abnormal data => **Anomaly detection** like talked before

### Instance-Based versus Model-Based Learning ###

One more way to categorize ML systems is by how they **generalize**.

Most ML tasks => Make **predictions** => **Generalize** to examples it has never seen before.

The true goal is to perform well on new instances.

Two mains approaches:

- Instance-based learning
- Model-based learning

#### Instance-based learning ####

The system learns the examples by heart, then generalizes to new cases using a similarity measure => **Similarity measure** => **Measure how much each instance resembles the known instances** => **Instance-based learning**

#### Model-based learning ####

Build a model from examples, then use that model to make predictions => **Model-based learning**

Exemple :
Data from the OECD about life satisfaction and GDP per capita in 2015.

Data is noisy but goes more or less linearly.

Model life satisfaction as a linear function of GDP per capita => **Linear model** => This process is called **Model selection** : you selected a linear model and used it to make predictions.

Then we need to know which values of the model's parameters make it perform best => **Training** the model with a **performance measure**

Utility function => How good the model is

Cost function => How bad the model is

For linear regression problems, cost function is mostly used. It'll measure the distance between the model's predictions and the training examples.

Check **oecd.py** for the code.

If it makes good predictions => ok
Else => get more or better data, use more parameter, use a better model, reduce the noise in the data.

This is a typicak **ML project workflow** :

- Study the data
- Select a model
- Train it
- Apply the model to make predictions

## Main Challenges of ML ##

Our main task is to select a learning algorithm and train it on some data.
Two things can go wrong : **Bad algorithm** or **Bad data**

### Bad Data ###

#### Insufficient Quantity of Training Data ####

Compared to humans, ML algorithms need a lot of data to generalize well. Even for simple problems, typically thousands, for more complex(speech ...) you need millions.

In a 2001 Study from Microsoft => If the data is qualitative enough, and plentiful, the simpler algorithm almost have the same performance as the complex one.

But having access to huge amounts of qualitative data is not always possible, so complex algorithm still need to be done.

#### Nonrepresentative Training Data ####

To generalize well, it is crucial that your training data be representative of the new cases you want to generalize to. Instance-based learning or model-based learning.

To take back the example of the linear model, if you exclude from the data rich countries like Norway, Switzerland, Luxembourg ... the predictions is bad.

Getting a training set that is representative is quite hard => if not enough, data is too prone to sampling noise, but even very large sample can be nonrepresentative if the sampling method is flawed => **Sampling bias**

**Example :** Sampling bias

In 1936, Literary Digest sent a mail to 10 millions people to ask them who they will vote for the presidential election of Landon against Roosevelt.

Landon was presumably winning with 57% of the votes. But Roosevelt won with 62% of the votes.

The problem was a sampling bias, since they sent a mail to the subscribers of the Literary Digest, which were mostly wealthy people + only 25% answered => **Sampling bias**

#### Poor-Quality Data ####

If your training data is full of errors, outliers, and noise (i.e. irrelevant attributes), it will make it harder for the system to detect the underlying patterns.

Cleaning the data is a significant part of a ML project => **Data preprocessing**

For example, if some instances are clearly outliers, it may help to simply discard them or try to fix the errors manually. or if some instances are missing, exclude them, ignore them, fill them with median value or mean value, or train a model with and without them...

#### Irrelevant Features ####

Garbage in, garbage out => A critical part of the success of a ML project is coming up with a good set of features to train from => **Feature engineering** :

- Feature selection : Selecting the most useful features
- Feature extraction : Combining existing features to produce a more useful one (i.e. dimensionality reduction)
- Creating new features by gathering new data.

#### Overfitting the Training Data ####

**Overfitting** : The model performs well on the training data, but it does not generalize well.

Complex models can detect subtle patterns in the data BUT if the sample size is too small it can find patterns in the noise itself. Like if you give data about the OECD, with New Zealand, Norway, Sweden, Switzerland => If a country have W in his name => life satisfaction ++

What can we do ? :

- Simplify the model ( a linear model rather than a high-degree polynomial model) or by constraining the model
- more training data
- reduce the noise and remove outliers

Constraining a model => **Regularization** => The amount of regularization to apply during learning can be controlled by a **hyperparameter** => **Hyperparameter tuning**

It can force the model to have a smaller slope but at the end allows it to generalize better to new examples.

#### Underfitting the Training Data ####

Tge opposite of overfitting => The model is too simple to learn the underlying structure of the data:

- Selecting a more powerful model, with more parameters
- Feeding better features to the learning algorithm (feature engineering)
- Reducing the constraints on the model (e.g. reducing the regularization hyperparameter)

#### TLDR ####

- ML => make machines better at some task by learning from data, instead of having to program the rules manually
- Differents types => Supervided, Unsupervised, Semisupervised, Reinforcement, Batch, Online, Instance-based, Model-based and more
- You gather data to do a training set, feed the training set to the learning algorithm, and it will output a model and then hopefully make good predictions. If its instance based, learn the exemple by heart and use similarity
- It will not perform well if the data set is too small, not representative, poor quality, irrelevant features... It cant be too simple (Underfitting) nor too complex(Overfitting)

So how do we know the model is great and ready to ship ??

## Testing and Validating ##

We need to actually try it and see if he predicts well on new data. One way is to put it directly in production, works well but this will make users complains and possibly lose money.

So we need to test it before, but how ? We need to split the data set into two : **Training set** and **Test set**.

The error rate on new cases is called the **generalization error** (or **out-of-sample error**), and by evaluating your model on the test set, you get an estimation of this error.

If the **training error** is low (i.e. the model makes few mistakes on the training set) but the **generalization error** is high => **Overfitting**

Normally => **80%** of the data in the training set and **20%** in the test set.

It becomes simple enough, if you are hesitating on two different models, you can test them on the test set and keep the best one.

But what if you have a lot of models ? You will end up with a model that performs well on the test set but not on the real data => **Hyperparameter tuning**.

We need a third set => **Validation set**. You train multiple models with the training set, then select the best one with the validation set, then test it on the test set.

To avoid too much wasting of data is its scarce, we can use cross-validation => we split the training set into more subsets called **folds**. Then we train on all but one fold and test on the remaining fold. We do this for each fold and average the results. => **Cross-validation**

### No Free Lunch Theorem ####

A model is a simplified version of the observations => **Assumptions** => **No Free Lunch Theorem** : If you make absolutely no assumption about the data, then there is no reason to prefer one model over any other => Sometimes the best one is a linear model, then a neural network, then a decision tree, etc...

## Exercices ##

1. How would you define Machine Learning?
=> Make machine learn with data instead of programmimg explicitely, it means getting better at some task

2. Can you name four types of problems where it shines?
=> Very complex problem(speech recognition), problem with a lot of rules and evolution(spam filter), A large set of data which can help us get more insight, Fluctuating environnements which need data to reevaluate

3. What is a labeled training set?
=> It is a training set which is already labeled, meaning it have already have the cause and answers to determine the predictors

4. What are the two most common supervised tasks?
=> Classification and Regression

5. Can you name four common unsupervised tasks?
=> Clustering, visualization, anomaly detection, dimensionality reduction, association rule learning

6. What type of Machine Learning algorithm would you use to allow a robot to walk in various unknown terrains?
=> Reinforcement learning

7. What type of algorithm would you use to segment your customers into multiple groups?
=> Clustering (Unsupervised learning) but if you know them, you can do a classification algorithm(supervised learning)

8. Would you frame the problem of spam detection as a supervised learning problem or an unsupervised learning problem?
=> Supervised, the labels are from the userbase

9. What is an online learning system?
=> You give a model, then update it using mini-batches throughout a timeline of your choice, then discard the data, capable of adapting rapidly to changing data

10. What is out-of-core learning?
=> For huge datasets / poor infrastructure , you train the model by dividing the datasets to lessen the costs

11. What type of learning algorithm relies on a similarity measure to make predictions?
=> Instance-based, it'll learn by heart then uses a similarity measures to make predictions

12. What is the difference between a model parameter and a learning algorithm’s hyperparameter?
=> a model has one or more parameters that determine what it will predict given a new instance, a learning algorithm tries to find optimal values for these parameters such that model generalizes well to new instances. A hyperparameter is a parameter of the LA itself, not the model

13. What do model-based learning algorithms search for? What is the most common strategy they use to succeed? How do they make predictions?
=> They try to search for an optimal value for the model parameters such taht the model will generalize well to new instances. They use linear model or neural network to succeed, we train them using a "minimizing cost function" taht measures how bad the system is at making predictions on the training data, plus a penality for model complexity if the model is regularized. To make predictions, we feed the new instance's features into the model's prediction function, using the parameter value found by the learning algo

14. Can you name four of the main challenges in Machine Learning?
=> Get a large set of data, choose the right model, non representative data, uninformative features, too simple model which underfit or too complex model which overfit

15. If your model performs great on the training data but generalizes poorly to new instances, what is happening? Can you name three possible solutions?
=> This can be called Overfitting, it can be resolve by getting more data, simplifying the model or reducing the noise in the training data

16. What is a test set and why would you want to use it?
=> It is data which has not been used to train the model, it will validate the model if the prediction ratio is correct => estimate the generalization error , before launch the model in production

17. What is the purpose of a validation set?
=> Model is trained on the training set, then tuned on the test set, then validate on the validation set, helps to tune the hyperparameters

18. What can go wrong if you tune hyperparameters using the test set?
=> Hyperparameter tuning, the model is too much adapted to the test set after reviewing it, Overfitting

19. What is cross-validation and why would you prefer it to a validation set?
=> We divide the test set into different subset, so we dont have to use a validation set, then train on the different subset but one.
We would prefer it over a validation set in case of a not so large dataset.
