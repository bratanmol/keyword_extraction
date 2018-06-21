import PyPDF2
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from string import punctuation,digits
import numpy as np
import pandas as pd

# creating a pdf file object
pdfFileObj = open('JavaBasics-notes.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
pages= pdfReader.numPages

#List to hold all the text
corpus=[]


for i in range(pages):
    #Reading the text page by page
    pageObj = pdfReader.getPage(i)
   
    #Appending it to the corpus
    corpus.append(pageObj.extractText())
    
# closing the pdf file object
pdfFileObj.close()

#Adding punctuations and digits to stop words list from nltk
stop = set(stopwords.words('english')+list(punctuation)+list(digits))

#Getting rid of the operators from the stopwords list.
operators = set(('and', 'or', 'not'))
stop = set(stop) - operators

#Using ScikitLearn to calculate Tf-Idf score for each word
tf_idf = TfidfVectorizer(stop_words=stop,min_df = 3,max_df=0.75,use_idf=True,ngram_range=(1,1))

#Performing the operation
keywords = tf_idf.fit_transform(corpus)

#Writing the top 20 keywords in a csv file
weights = np.asarray(keywords.mean(axis=0)).ravel().tolist()
weights_df = pd.DataFrame({'term': tf_idf.get_feature_names(), 'weight': weights})
weights_df = weights_df.sort_values(by='weight',ascending=False).head(10)
weights_df.to_csv("keywords.csv",index=False)