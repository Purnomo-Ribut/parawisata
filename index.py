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
import re

#Modul library Metode 
#from sklearn.naive_bayes import GaussianNB
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.tree import DecisionTreeClassifier
def load_dataset():
	data = pd.read_csv("destinasi wisata madura - Sheet1.csv")	
	return data

option = st.sidebar.selectbox(
    'Silakan pilih:',
    ('Dataset','Modeling','Implementasi')
)

if option == 'Dataset' or option == '':
    st.write("""# Dataset""") #menampilkan halaman utama
    st.write (""" 
                Purnomo Ribut | 200411100156
		
                Indra Ramadan Fadilafani | 200411100158 """)
    st.write("""
                Dataset yang kami gunakan dalam penelitian ini dengan cara scrawling data di google dengan
website Mytrip dan website random lainnya. dalam website ini kami mengambil nama wisata dan penjelasan wisata
tersebut. berikut data yang kami ambil : 
    """)
    st.dataframe(load_dataset())
    #data = pd.read_csv("destinasi wisata madura - Sheet1.csv")
    # df.rename(columns={"d4r55":"Username","wiI7pd":"Ulasan"}, inplace=True)
    #data = data.drop('no', axis=1)
    st.write (""" 
    Dataset ini terdiri dari 3 fitur yaitu :
    * nama berfungsi untuk menampung nama tempat Wisata
    * penjelasan berfungsi untuk menampung paragraf yang menjelaskan tempat wisata 
    * label berfungsi untuk melabeli apakah wisata termasuk 'Alam' atau 'Buatan'
    
    Dari dataset tersebut kami lakukan Prepocessing data yang terdiri dari : 
    * Cleaning, Cleaning merupakan proses pembersihan data dari karakter yang tidak relevaN seperti tanda baca, mention, character hashtag atau URL. Tujuan dari tahap ini adalah untuk membuat data lebih mudah diolah dan menghilangkan noise pada data. Cleaning text menggunakan library re dan pandas.

    * Case Folding, Case Folding merupakan proses untuk mengkonversi teks ke dalam format huruf kecil (lowercase). Hal ini bertujuan untuk memberikan bentuk standar pada teks.

    * Tokenizing, proses pemotongan teks menjadi bagian-bagian yang lebih kecil, yang disebu token. Pada proses ini juga dilakukan penghilangan angka, tanda baca dan karakter lain yang dianggap tidak memiliki pengaruh terhadap pemrosesan teks.

    * Stopword Removal, Tahap Filtering atau Stopword Removal adalah tahap pemilihan kata-kata yang dianggap penting.

    * Stemming, Stemming adalah proses pengubahan bentuk kata menjadi kata dasar atau tahap mencari root dari tiap kata.
    
    Dilanjutkan dengan Pembobotan data, 
    * Pembobotan kata yang dilakukan adalah kata yang terdapat dalam teks akan diberi berat atau bobot dengan menggunakan metode TF-IDF (Term Frequency - Inverse Document Frequency). Istilah yang terdapat pada satu dokumen lebih difokuskan pada TF (Term Frequency) sedangkan IDF(Inverse Document Frequency) lebih difokuskan pada istilah di banyak dokumen. Metode TF-IDF menggabungkan dua cara untuk perhitungan bobotnya, yaitu dengan menghitung frekuensi kemunculan kata di sebuah dokumen tertentu (TF) dan melakukan perhitungan invers terhadap frekuensi dokumen yang mengandung kata tersebut (IDF).Operator yang digunakan dalam menghubungkan operator dengan data tabel menggunakan operator nominal to text karena dalam Process Documents from Data harus bersifat teks sedangkan data pada tabel bersifat polynomial.
    
    Selanjutnya di Modelling 
    * Dalam tahapan ini Naive Bayes Classification merupakan teknik klasifikasi berdasarkan Teorema Bayes dengan asumsi independensi di antara para prediktor. Naive Bayes Classifier memprediksi peluang di masa depan berdasarkan pengalaman di masa sebelumnya sehingga dikenal sebagai Teorema Bayes. Dalam istilah sederhana, penggolongan Naive Bayes menganggap bahwa kehadiran fitur tertentu di kelas tidak terkait dengan kehadiran fitur lainnya (Hidayatullah, 2014) . Keuntungan penggunan adalah bahwa metode ini hanya membutuhkan jumlah data pelatihan (training data) yang kecil untuk menentukan estimasi parameter yg diperlukan dalam proses pengklasifikasian. Karena yang diasumsikan sebagai variabel independent, maka hanya varians dari suatu variabel dalam sebuah kelas yang dibutuhkan untuk menentukan klasifikasi, bukan keseluruhan dari matriks kovarians. Pada tahapan ini dilakukan modelling dengan model naïve bayes dari data latih yang sudah di pre processing sebelumnya dan diuji dengan data uji

    Selanjutnya Klasifikasi 
    * Pada tahapan proses ini dilakukan untuk menentukan kelas pada masing-masing objek wisata apakah termasuk wisata alam atau buatan dengan menerapkan metode Naive Naive baiyes
    

    """)
    
    
elif option == 'Modeling':
	st.write("""## Modeling Naive Bayes""") #menampilkan judul halaman dataframe
	st.write("""
	Naïve bayes adalah algoritma yang dikembangkan berdasarkan teorema bayes yang mengasumsikan setiap atribut sebagai independen sendiri dan berbeda dengan atribut lainnya. menggunakan metode Naive Bayes untuk membantu wisatawan dalam memilih objek wisata yang sesuai dengan preferensi mereka. Metode Naive Bayes dipilih karena telah terbukti efektif dalam melakukan klasifikasi pada data dengan fitur yang kompleks seperti halnya pada klasifikasi objek wisata.
	
	""")
	code = '''
	# Membaca file CSV "destinasi wisata madura - Sheet1.csv" dan menyimpan datanya ke dalam variabel `data`
	data = pd.read_csv("destinasi wisata madura - Sheet1.csv")

	# Menghapus kolom 'no' dari DataFrame `data`
	data = data.drop('no', axis=1)

	# Menghitung jumlah nilai null (kosong) dalam setiap kolom DataFrame `data`
	data.isnull().sum()

	# Menampilkan informasi tentang DataFrame `data`, termasuk jumlah baris, jumlah kolom, dan tipe data setiap kolom
	data.info()

	# Menghapus baris yang mengandung nilai null dari DataFrame `data`
	data.dropna(inplace=True)

	# Kembali menghitung jumlah nilai null (kosong) dalam setiap kolom DataFrame `data` setelah baris-baris yang mengandung nilai null dihapus
	data.isnull().sum()

	# Menghitung jumlah kemunculan setiap nilai dalam kolom 'label' DataFrame `data` dan menampilkannya
	data["label"].value_counts()
	'''

	st.code(code, language='python')
	
	data = pd.read_csv("destinasi wisata madura - Sheet1.csv")
	data = data.drop('no', axis=1)
	data.isnull().sum()
	data.info()
	data.dropna(inplace=True)
	data.isnull().sum()
	data["label"].value_counts()
	
	"""## Preprocessing"""
	st.write("""Cleaning """)
	def delete_char(text):
	  text = text.replace('\\t',"").replace('\\n',"").replace('\\u',"").replace('\\',"")
	  text = text.encode('ascii', 'replace').decode('ascii')
	  return text.replace("http://"," ").replace("https://", " ")
	  return text.replace("https://","").replace("http://","")
	data["penjelasan"]=data["penjelasan"].apply(delete_char)
	st.write("""Hasil Cleaning """)	
	data
	
	#hapus angka
	def del_num(text):
	  text =re.sub("\d+","",text)
	  return text
	data["penjelasan"]=data["penjelasan"].apply(del_num)
	data
	
    
	    

	

    
    #membuat dataframe dengan pandas yang terdiri dari 2 kolom dan 4 baris data
    #df = pd.DataFrame({
     #   'Column 1':[1,2,3,4],
      #  'Column 2':[10,12,14,16]
    #})
    #df #menampilkan dataframe
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
    


#ukuran data
data.shape



#import regex as re





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
