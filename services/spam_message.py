from joblib import dump,load
import numpy as np
import sys
import os
from joblib import dump,load
from sklearn.feature_extraction.text import CountVectorizer

class SpamService():
	def __init__(self):
		self.initM()

	def initM(self):
		self.Classifier = load('models/spamModel/spamPredict.joblib');
		self.Vectorizer = load('models/spamModel/vectroizer.pk1');

	def is_spam(self,m):
		data= self.Vectorizer.transform([m.text])
		calculous=  self.Classifier.predict(data)
		m.m_type ='text'
		if str(calculous[0])== 'ham':
			m.text = 'Non Spam'
		else:
			m.text = 'Spam'

		return m
