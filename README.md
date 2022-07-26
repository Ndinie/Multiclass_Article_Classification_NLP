# Project Title
Prediction model on Multiclass Article Classification NLP

## Project Description
Text documents are essential as they are one of the richest sources of data for businesses. 
Text documents often contain crucial information which might shape the market trends or influence the investment flows. 
Therefore, companies often hire analysts to monitor the trend via articles posted online, 
tweets on social media platforms such as Twitter or articles from newspaper. 


However, some companies may wish to only focus on articles related to technologies and politics. 
Thus, filtering of the articles into different categories is required.
Often the categorization of the articles is conduced manually and retrospectively; thus, causing the waste of time and resources due to this arduous task. 
Hence, your job as a machine learning engineer is tasked to categorize unseen articles into 5 categories namely Sport, Tech, Business, Entertainment and Politics.

## How to Install and Run the Project
This project can be run via [Google Colab](https://colab.research.google.com/?utm_source=scs-index) by creating a new notebook or just download the [Multiclass_Article _Classification_train](https://colab.research.google.com/drive/10TdIMgB3o8LG12AfzT1ECkHpEu-iyA0z?usp=sharing) to test it out!

Google Colab also provide us with free GPU where all you neeed to do is change the runtime type to 'GPU'.
Plus Colab does not need any additional modules installation.

# How to use the project
You need to ensure that when you load the dataset, it links directly to the correct path which is here [bbc-text.csv](https://raw.githubusercontent.com/susanli2016/PyCon-Canada-2019-NLP-Tutorial/master/bbc-text.csv)

Then after that you can proceed as usual. You can also check each of sections inside to analyze how the flow of training the dataset is.

With the help of Tensorboard, we were able to see the training process plotted via Tensorboard:

![Training-process-plotted-using-Tensorboard](https://github.com/Ndinie/Multiclass_Article_Classification_NLP/blob/main/static/Training-process-plotted-using-Tensorboard.png)

Below is the classification report which acquired after training the dataset.

![Classification Report](https://github.com/Ndinie/Multiclass_Article_Classification_NLP/blob/main/static/classification-report.png)

From this model, we able to get above 90% accuracy which is great!

## Credits
Greatest respect to [susanli2016](https://github.com/susanli2016/PyCon-Canada-2019-NLP-Tutorial) for providing this dataset.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
