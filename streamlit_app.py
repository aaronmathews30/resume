import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Aaron Biju Mathews
##### *Resume* 
''')

image = Image.open('dp.jpeg')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Final year Master of Data Science student with 2 years of corporate experience in creating SOAP/REST services at Ingram Micro. 
- Highly organised, resourceful, and keen to take on new challenges. Can efficiently work in a challenging environment with a keen eye for detail. 
- Can independently work on multiple projects and deliver with exceeding expectations by constantly engaging with stakeholders. 
- I've performed research & data analysis and presented my findings & key insights to important stakeholders.  
- Can contribute my abilities to the whole data analysis lifecycle with a collaborative attitude, from gathering requirements, business analysis, sourcing and exploring data, data cleansing, data modelling, and report creation and visualisation, data analysis, to provide better clarity to the relevant stakeholders. ''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="/" target="_blank">Aaron Biju Mathews</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

def txt5(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

#####################
st.markdown('''
## Education
''')

txt('**Master of Data Science**', 'JUL 20-current')
txt('*RMIT University*', 'Melbourne')
st.markdown('''
- GPA: `3.6`
- Secured 4 G.P.A in first year
''')

txt('**Bachelors of Science**' ,'AUG 14- MAY 18')
txt('*University of Mumbai* ', 'Mumbai')
st.markdown('''
- Won 1st Prize in Idea Presentation Competition at “SPECTRA 2K17”, a State-level Competition, India. 
- Presented a technical paper titled "Live Data forensics & Metadata analysis" at a National level Conference held in Sandip Institute of Engineering & Management, Nashik, Maharashtra, and won the 1st Prize, 2018.

''')

#####################
st.markdown('''
## Work Experience
''')
txt('**Casual Researcher**', 'MAR 22 - current')
txt('*RMIT University*', 'Melbourne')
st.markdown('''
- Designed & implemented a Database application for RMIT Factlab, which is a partnership between RMIT University and the ABC, which will be used in the federal election 2022 to track the misinformation campaign.
- Created a UI to interact with the database and visualisations for efficient information delivery.
''')

txt('**Data Science Intern**','MAR 22 -JUN 22')
txt('*Universal Biosensors*', 'Melbourne')
st.markdown('''
- Designed & implemented an API platform that will be used by scientists to analyse raw data for research.
- Implemented & suggested different machine learning algorithms to detect prostate cancer from a drop of blood.
''')

txt('**Business Consultant**','NOV 21 - DEC 21')
txt('*Ngalaya Indigenous Corporation*','NSW') 
st.markdown('''
- Analysed and presented the organisation's purpose and alignment to UN Sustainable Development Goals.
- Outlined opportunities or activities that might enhance the organisation's social or environmental impact.
- Redefined productivity (finance models, personnel structures, marketing, supply chain, logistics) to value by making for alternative income streams to be built for Ngalaya to become more sustainable.
''')


txt('**Data Engineer Intern**','SEP 21 - NOV 21')
txt('*Marwadi Shares and Finance Ltd.*','Mumbai') 
st.markdown('''
- Implemented trading algorithm which will be deployed in the live markets in a hedge fund. 
- Performed Data standardisation on raw datasets of assets into a standard format as used by quantitative traders.
- Maintained database for strategy-wise trade consolidation & profit-loss calculation with M2M procedure implementation. 
- Created visualisations to assist the quantitative traders in identifying trends & progresses in the implemented strategies.
''')


txt('**ML/OPS Intern**','FEB 21 - MAY 21')
txt('*Larsen and Toubro Infotech*','Mumbai') 
st.markdown('''
- Optimised the process of finding outliers by creating data cleaning scripts that were used in the ML pipelines.
''')


txt('**Software Developer**',' JUL 18 - AUG 20')
txt('*Ingram Micro*',' Mumbai')
st.markdown('''
-	Successfully integrated and managed web-based applications by developing middleware solutions in a multinational B2B giant. 
-	Reduced rigorous maintainability of multiple ERPs by developing a solution that helped maintain a single ERP system containing all the information from existing ERPs used in multiple countries.
-	Achieved many secure APIs by successfully migrating two business-critical and high-volume services, being the only point of contact for this pilot project. 
-	Received “Appreciation Leaf” for my contribution towards a critical MDG project at Ingram Micro.

''')




#####################
st.markdown('''
## Skills

#### Technical Skills
''')
txt3('Programming', '`Python`, `R`, `Java`,`Linux`')
txt3('Frameworks', '`Flask`, `Django`')
txt3('Database','`Oracle`,`PostgreSQL`,`MongoDB`')
txt3('SQL','`SQL`, `relational database`, `semi-structured data`, `NoSQL`')
txt3('Data processing/wrangling', '`pandas`, `numpy`')
txt3('Python libraries','`streamlit`, `tkinter`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3("Tibco","`Tibco BW 5.X and 6.5`, `Admin 5.8`, `TEA`, `EMS`, `GEMS`, `Tibco-Substation`")
txt3('XML Technologies', '`XML`, `XSLT`, `WSDL`, `XSD`, `XPATH`, `Canonical Data Models (CDM)`')
txt3('Network & Protocols', '`HTTP`, `Tibco EMS`, `SOAP`, `REST JSON`')
txt3('Testing tools', '`SOAP UI`, `POSTMAN`, `JMeter`')
txt3('Operating systems', '`Linux`, `Windows`, `Mainframe (Basics)`')
txt3('Other tools', '`SAP`, `AWS`, `Apigee`, `Splunk`, `Putty`, `HPQC`, `SharePoint`, `Tortoise SVN`, `GIT`, `MS Office (Excel)`')

st.markdown('''
#### Soft Skills
'''
)
txt5('`Time Management`', '`Excellent Communication Skills`' )
txt5('`Team leader`', '`Self-Motivated`')
txt5('`High attention to detail`', '`Maintain high accuracy & timelines`')

#####################
st.markdown('''
## Projects

''')
txt('**API Platform for Data analysis**','') 
st.markdown('''
- Designed & implemented an API platform using Flask to help scientists upload, cleanse & visualize data.
- Looked into different explainable Machine Learning models which will be used to detect prostate cancer from square wave voltammetry data. 
''')

txt('**Web-based Database application**','') 
st.markdown('''
- Designed & implemented a database application using Django to help journalists at ABC network track the social misinformation campaign during the federal elections.
- Deployed the database application using PostgresSQL as the back.
''')

txt('**Prediction of patients in ICU who would develop sepsis during their ICU stay**','') 
st.markdown('''
Intensive Care Units (ICUs) are constantly challenged to monitor their patients for the risk of sepsis development (an infection that can accrue while staying in ICU). While this challenge has been around for many years, the recent COVID-19 pandemic has increased its prominence. For an ICU, the ability to predict if a patient in ICU will develop a sepsis is very beneficial. That would assist with reducing the risk of health complications, and managing the ICU resources (such as bed availability, etc.).

So, to get help the hosiptals, I developed an ML model to predict if a patient will develop 
sepsis in the period of their stay in the ICU, based on provided attributes (features) 
related to: patient characteristics, diagnoses, treatments, services, hospital charges and 
patients socio-economic background.

Different models were considered with Decision Tree with basic parameters as the baseline models. Later Random forest & random forest with hyperparameter tuning was looked into to check if there
is any significant change in the model accuracy.
''')

txt('**Image classification using Deep Learning**','') 
st.markdown('''
The field of computer vision includes a set of main problems such as image classification, 
localization, image segmentation, and object detection. Among those, image classification can be 
considered the fundamental problem. It forms the basis for other computer vision problems. Image classification is probably the most important part of digital 
image analysis. In this age of smart vehicles, Image classification can be considered as one of its foundations. 
This project was designed to train a model to classify images of trffc signs. The project is divided into 2 task, one is to classify the images according to sign-type &
the other is to classift the images according to sign-shape.  
''')

txt('**Share Price Prediction**','') 
st.markdown('''
Predicting accurately the future value of a share's price is a priceless asset for a stock trader. Almost every trading institution uses machine learning, time series analysis, etc. and other sorts of statistical & technical aid to predict future stock market prices. 
For this project, I've used a daily closing price of a stock trading in ASX. This project will implement different trend models and identify the best fitting model for the data. 
That model will be then used to predict future values.
''')


txt('**Prediction of Quarterly Revenue of Amazon**','') 
st.markdown('''
Amazon is one of the world's largest e-commerce companies, having a global presence. 
Its online retail operation is built upon the Prime programme, which is backed up by the company's vast delivery network. 
For this project I look into Amazon's quarterly revenue from 2010 through 2022. I used that the predict the revenue of the next 10 quarters. 
''')




txt("**Data cleaning and Summarising of NBA players' statistics.**",'') 
st.markdown('''
-	Performed pre-processing steps on the data, rectified the errors and managed the outliers. 
-	Explored the data by using different graphs for insights.
''')
txt('**Prediction of survival of heart failure patients using 2 different classification models**','') 
st.markdown('''
- Medical records of heart failure patients were retrieved, pre-processed, and explored, and two classification models were trained using them. These models were then used to predict the survival of patients.
''')

txt('**Analysis of Crime Statistics and per capita Income in Victoria, AU**','') 
st.markdown('''
- Performed Data Wrangling on the data like inspecting the data for errors, tidying the data, combining the 2 datasets, identifying, and treating outliers, and transforming the data.
''')

txt('**Live Data Forensics & Metadata Analysis**','') 
st.markdown('''
- Developed a forensics investigation tool that creates images, and hash values, recovers deleted files from NTFS tables, analyse metadata & identifies Malware from RAM images.
''')
#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'www.linkedin.com/in/Aaron10')
txt2('GitHub', 'https://github.com/aaronmathewsRMIT')
txt2('', 'https://github.com/aaronmathews30')
