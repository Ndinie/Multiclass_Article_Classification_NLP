# -*- coding: utf-8 -*-
"""Multiclass_Article _Classification_train.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZF1K9UtfoTlKrmToE47DFXvNIx7F-6bh

IMPORT NECESSARY PACKAGES
"""

import os
import re
import json
import pickle
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tensorflow.keras.layers import Embedding
from tensorflow.keras.utils import plot_model
from tensorflow.keras import Input, Sequential
from sklearn.preprocessing import OneHotEncoder
from tensorflow.keras.callbacks import TensorBoard
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import LSTM, Dense, Dropout, Bidirectional
from multiclass_article_classification_module import ModelDevelopment, ModelEvaluation
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

"""# STEP 1) DATA LOADING"""

nlp_df = pd.read_csv('https://raw.githubusercontent.com/susanli2016/PyCon-Canada-2019-NLP-Tutorial/master/bbc-text.csv')

"""# STEP 2) DATA INSPECTION"""

nlp_df.info()

nlp_df.describe().T

nlp_df.head()

"""CHECK DUPLICATES"""

nlp_df.duplicated().sum()

"""CHECK NANs"""

nlp_df.isna().sum()

"""# STEP 3) DATA CLEANING

REMOVE DUPLICATES
"""

nlp_df.duplicated().sum()

nlp_df.drop_duplicates(inplace=True)

category = nlp_df['category']
text = nlp_df['text']

"""# STEP 4) FEATURE SELECTION

# STEP 5) DATA PREPROCESSING

X features
"""

vocab_size = 1000
oov_token = '<OOV>'
tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_token)
tokenizer.fit_on_texts(text)

word_index = tokenizer.word_index
print(dict(list(word_index.items())))

text_int = tokenizer.texts_to_sequences(text)

max_len = np.median([len(text_int[i]) for i in range (len(text_int))])

padded_review = pad_sequences(text_int, 
                              maxlen = int(max_len),
                              padding = 'post',
                              truncating = 'post')

"""y target"""

ohe = OneHotEncoder(sparse=False)
category = ohe.fit_transform(np.expand_dims(category, axis=-1))

X_train, X_test, y_train, y_test = train_test_split(padded_review,
                                                    category,
                                                    test_size=0.3,
                                                    random_state=123)

"""# MODEL DEVELOPMENT"""

input_shape = np.shape(X_train)[1:]
nb_class = len(np.unique(y_train, axis=0))

md = ModelDevelopment()
nlp = md.sequential_model(input_shape, vocab_size = 1000, out_dims = 128, 
                          nb_class=5, nb_node=128, dropout_rate=0.3)

plot_model(nlp, show_shapes=(True))

nlp.compile(optimizer='adam',loss='categorical_crossentropy',
              metrics=['accuracy','acc'])

LOGS_PATH = os.path.join(os.getcwd(),'nlp_logs',datetime.datetime.now().
                         strftime('%Y%m%d-%H%M%S'))

tensorboard_callback = TensorBoard(log_dir=LOGS_PATH,histogram_freq=1)

!zip -r /content/nlp_logs.zip /content/nlp_logs
from google.colab import files
files.download("/content/nlp_logs.zip")

hist = nlp.fit(X_train, y_train, epochs=10,
               validation_data=(X_test, y_test),
               callbacks=tensorboard_callback)

"""LOAD TENSORBOARD"""

# Commented out IPython magic to ensure Python compatibility.
# %load_ext tensorboard

# Commented out IPython magic to ensure Python compatibility.
# %tensorboard --logdir nlp_logs

"""To show available keys:"""

hist.history.keys()

me = ModelEvaluation()
me.plot_hist_graph(hist)

"""# MODEL ANALYSIS

CLASSIFICATION REPORT
"""

y_pred = np.argmax(nlp.predict(X_test), axis=1)
y_actual = np.argmax(y_test, axis=1)

cr = classification_report(y_actual, y_pred)
print(cr)

"""CONFUSION MATRIX"""

cm = confusion_matrix(y_actual, y_pred)
labels = ['tech','business','sport','entertainment','politics']
disp = ConfusionMatrixDisplay(confusion_matrix = cm ,display_labels = labels)
disp.plot(cmap='PuBuGn')
plt.show()

"""# MODEL SAVING

*tokenizer*
"""

TOKENIZER_SAVE_PATH = os.path.join(os.getcwd(), 'tokenizer.json')

token_json = tokenizer.to_json()
with open(TOKENIZER_SAVE_PATH, 'w') as file:
  json.dump(token_json, file)

"""*onehotencoder*"""

OHE_SAVE_PATH = os.path.join(os.getcwd(), 'ohe.pkl')

with open(OHE_SAVE_PATH, 'wb') as file:
  pickle.dump(ohe, file)

"""*model*"""

NLP_SAVE_PATH = os.path.join(os.getcwd(), 'nlp.h5')
nlp.save(NLP_SAVE_PATH)