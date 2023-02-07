READ ME

Airlines delays and cancellations are a common occurrence and an unfortunate part of travel today. It can happen for a number of reasons, e.g., weather delays, equipment failures, staff shortages, etc. When it does occur - it is a significant inconvenience to passengers, airlines, and airports, and can have a significant snowball effect. 

The purpose of this project is to use airline, and weather data to better predict airline delays (by 15 minutes or more) using several machine learning algorithms. 

In the real world, this type of model could be executed an hour before take off time. The hope is that airport staff would be able to use the predictions from these models to better manage passengers and other relevant workstreams. 

Specifically we will be using logistic regression to develop a baseline model, and build on it with improved logistic and linear regression models, decision trees, ensemble learning methods (random forests and gradient boosted trees), and finally neural network Multilayer Perceptron (MLP) model to predict whether a flight will take off on time. To evaluate our different models we are focusing on using the F1 score and accuracy for the classification models, and then Mean Absolute Error (MAE) for the regression models. 

The best performing model for Classification is Decision Tree (DT) with an F1 score of 0.774 and for Regression is Linear Regression (LR) with an MAE of 18.07. Moving forward both our models have room for improvement before going into production.


The following files would be the most complete to understand this project:
- HouseSpark_Master.ipynb
	- This notebook contains refers to the other notebooks in this repository. 
- FinalPresentation.pdf

