# -*- coding: utf-8 -*-
"""mlh final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Dq35ul84TSSQb9GfxziPtgb__gRVbPUk
"""

!pip install docx2txt

"""CLEANING THE RESUME"""

import docx2txt
import numpy as np
resume = docx2txt.process("/content/Minimal Resume.docx")
import re
def cleanResume(resumeText):
    resumeText = re.sub('http\S+\s*', ' ', resumeText)  # remove URLs
    resumeText = re.sub('RT|cc', ' ', resumeText)  # remove RT and cc
    resumeText = re.sub('#\S+', '', resumeText)  # remove hashtags
    resumeText = re.sub('@\S+', '  ', resumeText)  # remove mentions
    resumeText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', resumeText)  # remove punctuations
    resumeText = re.sub(r'[^\x00-\x7f]',r' ', resumeText) 
    resumeText = re.sub('\s+', ' ', resumeText)  # remove extra whitespace
    res1 = ''.join([i for i in resumeText if not i.isdigit()])
    return res1
    
resume0=cleanResume(resume)
print(resume0)
d='RESUME Name TEELLA VANAJA Contact  Email vanajateella Career Objective Seeking a position in a reputed Organisation where I can use my technical skills as well as soft skills for the development of the organization and my professional growth Educational Qualifications Course Institute University Board Year of Completion CGPA Percentage B Tech CIVIL Gayatri Vidya Parishad College Of Engineering Autonomous Jawaharlal Nehru Technological University Kakinada JNTUK    Intermediate Vidwan junior college Bobbili Board of Intermediate Education Andhra P'
#d='RESUME Name DHARANI POLUKONDA Contact  Email polukondadharani LinkedIn Career Objective Seeking a position in a reputed Organisation where I can use my technical skills as well as soft skills for the development of the organization and my professional growth Educational Qualifications Course Institute University Board Year of Completion CGPA Percentage B Tech CSE Data Science Gayatri Vidya Parishad College Of Engineering Autonomous Jawaharlal Nehru Technological University Kakinada JNTUK    pursuing Intermediate Star Junior College Machilipatnam Board of Intermediate Education Andhra Pradesh    SSC Narayana e Techno School Machilipatnam SSC      Technical Skills Languages C Java R Advanced python Web Technologies HTML CSS JavaScript PHP Databases Oracle SQL Data Structures OOPs Concepts Design Analysis of Algorithms Operating Systems Computer Networks Database Management Systems and Software Engineering linux Certifications PCAP Programming Essentials in Python certification from CISCO Networking Academy Strengths Adaptability Optimistic Always interested in learning new things and also sharing the acquired knowledge with others Confidence Projects Developed a Dice game using JavaScript and HTML Developed an Application named Plavika which can be used to find plasma donors and allows the interested people to enroll as a Plasma Donor Academic Achievements Qualified in WE talent sprint supported by google Extra Curricular Activities I m an active participant of YES RACGVP of our College Participated in Group Discussion organized by IEEE WIE AG GVPCE A Participated in Debate organized by ICE under the auspices of Association of Civil Engineers Participated in Byte Code Quiz organized by IEEE Personal Details Father s Name Polukonda Veeranjaneyulu Date of Birth    Languages Known English Hindi Telugu Hobbies Cooking Browsing Internet Paper Craft Dancing Address for communication Plot  Sri venkateswara complex near kanayaka parameswari rice mill Godugupeta Koner center Machilipatnam pin code  Andhra Pradesh Declaration I hereby declare that the above mentioned information is a urate to the best of my knowledge Place Machilipatnam Signature Date    P Dharani'

def cleanResume(resumeText):
    resumeText = re.sub('httpS+s*', ' ', resumeText)  # remove URLs
    resumeText = re.sub('RT|cc', ' ', resumeText)  # remove RT and cc
    resumeText = re.sub('#S+', '', resumeText)  # remove hashtags
    resumeText = re.sub('@S+', '  ', resumeText)  # remove mentions
    resumeText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[]^_`{|}~"""), ' ', resumeText)  # remove punctuations
    resumeText = re.sub(r'[^x00-x7f]',r' ', resumeText) 
    resumeText = re.sub('s+', ' ', resumeText)  # remove extra whitespace
    return resumeText
t1=cleanResume(resume0)

"""importing libaries"""

import nltk
from nltk.corpus import stopwords
import string
from wordcloud import WordCloud
nltk.download('stopwords')
nltk.download('punkt')
import pandas as pd
import re
from sklearn.preprocessing import LabelEncoder

""" Store the job description into a variable"""

resumeDataSet = pd.read_csv("/content/UpdatedResumeDataSet.csv")
print(resumeDataSet)
resumeDataSet['cleaned_resume'] = ''
resumeDataSet.head()

resumeDataSet.info()

print ("Displaying the distinct categories of resume:\n\n ")
print (resumeDataSet['Category'].unique())
print("total unique category: {}". format(len(resumeDataSet['Category'].unique())))

print(resumeDataSet['Category'].value_counts())

# import seaborn as sns
# import matplotlib.pyplot as plt
# plt.figure(figsize=(20,15))
# sns.countplot(y="Category",data=resumeDataSet)

"""Cleaning the dataset"""

import re
def cleanResume(resumeText):
    resumeText = re.sub('http\S+\s*', ' ', resumeText)  # remove URLs
    resumeText = re.sub('RT|cc', ' ', resumeText)  # remove RT and cc
    resumeText = re.sub('#\S+', '', resumeText)  # remove hashtags
    resumeText = re.sub('@\S+', '  ', resumeText)  # remove mentions
    resumeText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', resumeText)  # remove punctuations
    resumeText = re.sub(r'[^\x00-\x7f]',r' ', resumeText) 
    resumeText = re.sub('\s+', ' ', resumeText)# remove extra whitespace
    res1 = ''.join([i for i in resumeText if not i.isdigit()])
    return res1
    
resumeDataSet['cleaned_resume'] = resumeDataSet.Resume.apply(lambda x: cleanResume(x))

type(resumeDataSet)

resumeDataSet.head()

"""word count

"""

import nltk
from nltk.corpus import stopwords
import string
from wordcloud import WordCloud

stopwords=set(stopwords.words('english')+['``',"''"])

total_words=[]
sentences=resumeDataSet['Resume'].values
cleanSentences =""

for i in range(0,200):
    resumeText=cleanResume(sentences[i])
    cleanSentences+=resumeText
    words=nltk.word_tokenize(resumeText)
    for word in words:
        if word not in stopwords and word not in string.punctuation:
            total_words.append(word)
            
word_freq_dist=nltk.FreqDist(total_words)
most_common=word_freq_dist.most_common(100)

print(most_common)

import nltk
from nltk.corpus import stopwords
import string
from wordcloud import WordCloud
stopwords=set(stopwords.words('english')+['``',"''"])

total_words_1=[]
sentences_1=resume0
print(sentences_1)
cleanSentences_1 =""

resumeText_1=cleanResume(sentences_1)
cleanSentences_1+=resumeText_1
words_1=nltk.word_tokenize(resumeText_1)
for word in words_1:
        if word not in stopwords and word not in string.punctuation:
            total_words.append(word)
            
word_freq_dist_1=nltk.FreqDist(total_words_1)
most_common_1=word_freq_dist_1.most_common(100)

print(most_common_1)

from sklearn.preprocessing import LabelEncoder

var=['Category']
le= LabelEncoder()
for i in var:
    resumeDataSet[i]=le.fit_transform(resumeDataSet[i])

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack


vect=TfidfVectorizer(
     sublinear_tf=True,
    stop_words='english',
        max_features=146)
resume=[resume0]

vect.fit(resume)
Word_feature_1=vect.transform(resume)
print(Word_feature_1)

resumeDataSet

"""Vectorization"""

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack


text=resumeDataSet['cleaned_resume'].values
terget=resumeDataSet['Category'].values
vect=TfidfVectorizer(
     sublinear_tf=True,
    stop_words='english',
        max_features=2000)
vect.fit(text)
Word_feature=vect.transform(text)
print(Word_feature)

#x=resumeDataSet.drop(['Category'],axis=1)
#y=resumeDataSet['Category']
#y.value_counts().plot.pie()

x_train, x_test, y_train, y_test=train_test_split(Word_feature, terget, random_state=0, test_size=0.2)
print(x_train.shape)
print(x_test.shape)

import sklearn
from sklearn.multiclass import OneVsRestClassifier
from sklearn.neighbors import KNeighborsClassifier

model=OneVsRestClassifier(KNeighborsClassifier())
model.fit(x_train, y_train)

prediction=model.predict(x_test)

print("training Score: {:.2f}".format(model.score(x_train, y_train)))
print("test Score: {:.2f}".format(model.score(x_test, y_test)))

from sklearn import metrics
print("model report: %s: \n %s\n" % (model, metrics.classification_report(y_test, prediction)))

import pickle
pickle.dump(vect,open("count-Vectorizer.pkl","wb"))
pickle.dump(model,open("Movie_Review_classification.pkl","wb"))



save_vect=pickle.load(open("count-Vectorizer.pkl","rb"))
model=pickle.load(open("Movie_Review_classification.pkl","rb"))

resumeDataSet['Category'].value_counts()

resumeDataSet['Category']

def test_model(de):
    sen=save_vect.transform([de]).toarray()
    res=model.predict(sen)[0]
    if res==15:
        return "Java Developer"
    if res==23:
        return "Testing"
    if res==8:
        return "DevOps Engineer"
    if res==24:
        return "Web Designing"
    if res==20:
        return "Python Developer"
    if res==12:
        return "HR"
    if res==13:
        return "Hadoop"
    if res==3:
        return "Blockchain "
    if res==10:
        return "ETL Developer"
    if res==18:
        return "Operations Manager"
    if res==6:
        return "Data Science"
    if res==22:
        return "Sales"
    if res==16:
        return "Mechanical Engineer"
    if res==1:
        return "Arts"
    if res==7:
        return "Database"
    if res==11:
        return "Electrical Engineering"
    if res==14:
        return "Health and Fitness"
    if res==19:
        return "PMO"
    if res==4:
        return "Business Analyst"
    if res==9:
        return "DotNet Developer"
    if res==2:
        return "Automation Testing"
    if res==17:
        return "Network Security Engineer"  
    if res==21:
        return "SAP Developer"                                            
    if res==5:
        return "Civil Engineer"
    if res==0:
        return "Advocate"
    else:
        return "Sorry,You have no jobs"

r=test_model(resume0)
print(r)



!pip install streamlit

!pip install pyngrok

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import pickle
# import streamlit as st
# import re
# def cleanResume(resumeText):
#     resumeText = re.sub('http\S+\s*', ' ', resumeText)  # remove URLs
#     resumeText = re.sub('RT|cc', ' ', resumeText)  # remove RT and cc
#     resumeText = re.sub('#\S+', '', resumeText)  # remove hashtags
#     resumeText = re.sub('@\S+', '  ', resumeText)  # remove mentions
#     resumeText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', resumeText)  # remove punctuations
#     resumeText = re.sub(r'[^\x00-\x7f]',r' ', resumeText) 
#     resumeText = re.sub('\s+', ' ', resumeText)  # remove extra whitespace
#     res1 = ''.join([i for i in resumeText if not i.isdigit()])
#     return res1
# 
# def main():
#   pickle_in=open("Movie_Review_classification.pkl","rb")
#   classifier=pickle.load(pickle_in)
#   st.title("job role prediction")
#   html_temp="""
#   <div style="background-color:tomato;padding:10px">
#   </div>
#   """
#   st.markdown(html_temp,unsafe_allow_html=True)
#   uploaded_file = st.file_uploader("choose a file")
#   if uploaded_file is not None:
#     # To read file as bytes:
#     bytes_data = uploaded_file.getvalue()
#     st.write(bytes_data)
# 
#     # To convert to a string based IO:
#     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
#     st.write(stringio)
# 
#     # To read file as string:
#     string_data = stringio.read()
#     st.write(string_data)
#   #dataframe = uploaded_file
#   #st.write(dataframe)
#   dataframe=cleanResume(uploaded_file)
#   predict=st.button("predict")
#   if predict:
#       result=""
#       result=test_model(dataframe)
#       st.success('the output is {}'.format(result))
# if __name__=="__main__":
#   main()

!ls

!ngrok authtoken 2Et3wrBYLj6S4YgaMwEgeetqmUM_6d7ZfdhQFnAXoRZfaDxaj

!ngrok

!app.run_server(mode='external')

from pyngrok import ngrok

#!nohub streamlit run app.py
!streamlit run app.py&>/dev/null&

!pgrep streamlit

publ_url=ngrok.connect(port="8050")
publ_url

!killall ngrok

ngrok.kill()

from pyngrok import ngrok
!nohup streamlit run app.py &
url=ngrok.connect(port="8501")
print(url)
!streamlit run --server.port 80 app.py >/dev/null

