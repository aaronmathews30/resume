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
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Aaron Biju Mathews</a>
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
- Implemented & suggested 
''')

txt('**Business Consultant**','NOV 21 - DEC 21')
txt('*Ngalaya Indigenous Corporation*','NSW') 
st.markdown('''
- Analysed and presented the organisation’s purpose and alignment to UN Sustainable Development Goals.
- Outlined opportunities or activities that might enhance the organisation’s social or environmental impact.
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
## Social Media
''')
txt2('LinkedIn', 'www.linkedin.com/in/Aaron10')
txt2('GitHub', 'https://github.com/aaronmathewsRMIT')
txt2('', 'https://github.com/aaronmathews30')
