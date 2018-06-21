 # importing required modules
import PyPDF2
import RAKE
import pandas as pd


# creating a pdf file object
pdfFileObj = open('JavaBasics-notes.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
pages= pdfReader.numPages

#Corpus list to hold all the text
corpus=[]

for i in range(pages):
    # creating a page object
    pageObj = pdfReader.getPage(i)
   
    #Appending each page to the corpus
    corpus.append(pageObj.extractText())
    
# closing the pdf file object
pdfFileObj.close()

#Converting corpus list to string
text = ''.join(str(e) for e in corpus)

#Using Stopwords provided by nltk 
stoplist = RAKE.NLTKStopList()

#Some common useless words in the document treated as stopwords
stoplist.extend(('rights reserved','ok','com','use','example','c','c+','// b'))

#Creating Rake Object
rake = RAKE.Rake(stoplist)

#Finding Keywords with Rake 
keywords =rake.run(text, minCharacters = 3, maxWords = 1, minFrequency = 5)

#Writing the results to a csv file
df = pd.DataFrame.from_records(keywords)
df.columns=['Term','Score']
df.to_csv("keywords_with_rake.csv",index=False)


