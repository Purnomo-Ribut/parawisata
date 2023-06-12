# -*- coding: utf-8 -*-
"""parawisata.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1htjmO-io-3GaPFUf5LY2XE1RP40kFq6Z
"""

#from google.colab import drive
#drive.mount('/content/drive')

#from google.colab import drive
#drive.mount('/content/drive')

#install library
#Modul Library
import streamlit as st
import numpy as np
import pandas as pd

#Modul library Metode 
#from sklearn.naive_bayes import GaussianNB
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.tree import DecisionTreeClassifier

option = st.sidebar.selectbox(
    'Silakan pilih:',
    ('Home','Modeling','Chart')
)

if option == 'Home' or option == '':
    st.write("""# Halaman Utama""") #menampilkan halaman utama
    st.title('E-LEARNING STUDENTS REACTIONS')
    st.write (""" Purnomo Ribut | 200411100156""")
          (""" Indra Ramadan Fadilafani | 200411100158 """)
    
    
    
elif option == 'Modeling':
    st.write("""## Modeling Naive Bayes""") #menampilkan judul halaman dataframe

    #membuat dataframe dengan pandas yang terdiri dari 2 kolom dan 4 baris data
    df = pd.DataFrame({
        'Column 1':[1,2,3,4],
        'Column 2':[10,12,14,16]
    })
    df #menampilkan dataframe
elif option == 'Chart':
    st.write("""## Draw Charts""") #menampilkan judul halaman 

    #membuat variabel chart data yang berisi data dari dataframe
    #data berupa angka acak yang di-generate menggunakan numpy
    #data terdiri dari 2 kolom dan 20 baris
    chart_data = pd.DataFrame(
        np.random.randn(20,2), 
        columns=['a','b']
    )
    #menampilkan data dalam bentuk chart
    st.line_chart(chart_data)
    #data dalam bentuk tabel
    chart_data





dataset, modelling, implementasi = st.tabs(["Dataset", "Modelling", "Implementasi"])

with dataset:
    """## Data Wisata Sumenep"""
    data = pd.read_csv("destinasi wisata madura - Sheet1.csv")
    # df.rename(columns={"d4r55":"Username","wiI7pd":"Ulasan"}, inplace=True)
    data.head(5)


#ukuran data
data.shape

data = data.drop('no', axis=1)

data

data.isnull().sum()

data.info()

#drop data kosong
data.dropna(inplace=True)

data

data.isnull().sum()

data["label"].value_counts()

#import regex as re

"""## Preprocessing"""

def delete_char(text):
  text = text.replace('\\t',"").replace('\\n',"").replace('\\u',"").replace('\\',"")
  text = text.encode('ascii', 'replace').decode('ascii')
  return text.replace("http://"," ").replace("https://", " ")
  return text.replace("https://","").replace("http://","")
data["penjelasan"]=data["penjelasan"].apply(delete_char)
data

#hapus angka
def del_num(text):
  text =re.sub("\d+","",text)
  return text
data["penjelasan"]=data["penjelasan"].apply(del_num)
data

#ubah huruf kecil
def change_var(text):
  text = text.lower()
  return text
data["penjelasan"]=data["penjelasan"].apply(change_var)
data

from string import punctuation

#hapus tanda hubung
def remove_punctuation(text):
  text = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",text)
  return text
data["penjelasan"]=data["penjelasan"].apply(remove_punctuation)
data

import nltk 
nltk.download("punkt")

from nltk.tokenize import word_tokenize
data["hasil"]=data["penjelasan"].apply(lambda x: nltk.word_tokenize(x))
data["hasil"]

data

normalize = pd.read_excel("/content/drive/MyDrive/parawisata /Normalization Data.xlsx")
normalize_word_dict={}

for row in normalize.iterrows():
  if row[0] not in normalize_word_dict:
    normalize_word_dict[row[0]] = row[1]

def normalized_term(comment):
  return [normalize_word_dict[term] if term in normalize_word_dict else term for term in comment]

data['comment_normalize'] = data['hasil'].apply(normalized_term)
data['comment_normalize'].head(10)

#stopword removal
nltk.download("stopwords")
from nltk.corpus import stopwords
txt_stopwords = stopwords.words("indonesian")

def stopword_removal(filter):
  filter = [word for word in filter if word not in txt_stopwords]
  return filter
data["stopwords_removal"]=data["comment_normalize"].apply(stopword_removal)
data["stopwords_removal"]

#removal2
data_stopwords=pd.read_excel("/content/drive/MyDrive/parawisata /list_stopwords.xlsx")

def stopword_removal2 (filter):
  filter =[word for word in filter if word not in data_stopwords]
  return filter
data["stopwords_removal_final"]=data["stopwords_removal"].apply(stopword_removal2)
data["stopwords_removal_final"]

"""## Stemming"""

#proses stem
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import string
import swifter
factory = StemmerFactory()
stemmer = factory.create_stemmer()

def stemming (term):
  return stemmer.stem(term)

term_dict = {}
for document in data['stopwords_removal_final']:
  for term in document:
    if term not in term_dict:
      term_dict[term] = ''
print(len(term_dict))

for term in term_dict:
  term_dict[term] = stemming(term)
  print(term,":",term_dict[term])

print(term_dict)

def get_stemming(document):
  return [term_dict[term] for term in document]

data['stemming'] = data['stopwords_removal_final'].swifter.apply(get_stemming)

print(data['stemming'])
data.head(20)

#Perhitungan TF-IDF
def joinkata(data):
  kalimat = ""
  for i in data:
    kalimat += i
    kalimat += " "
  return kalimat

text = data['stemming'].swifter.apply(joinkata)
text

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()
tfidf_separate = tfidf_vectorizer.fit_transform(text)

df_tfidf = pd.DataFrame(
    tfidf_separate.toarray(), columns=tfidf_vectorizer.get_feature_names_out(), index=data.index
)
X = df_tfidf.values
Y = data['label']
df_tfidf

Y

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split( 
    X, Y, test_size = 0.3, random_state = 100)
print("Jumlah Data training : ", len(X_train))
print("Jumlah Data test : ", len(X_test))

from sklearn.naive_bayes import GaussianNB
gnb_model = GaussianNB()
gnb_model.fit(X_train, Y_train)

from wordcloud import WordCloud

allWords = ' '.join([twts for twts in data['penjelasan']])
wordCloud = WordCloud(width=1600, height=800, random_state=30, max_font_size=200, min_font_size=20).generate(allWords)

from sklearn.metrics import accuracy_score
Y_pred = gnb_model.predict(X_test)
print (" GNB Accuracy : ",
    accuracy_score(Y_test,Y_pred)*100)
