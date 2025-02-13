import streamlit as st
import requests
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(layout='wide')

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animations
lottie_data_science = load_lottieurl(url="https://lottie.host/bfda9522-c7e9-4a29-8a5e-1e7a27d3c27d/VGN73p4NeD.json")
lottie_contact_us = load_lottieurl(url="https://lottie.host/e5aa96e5-62d8-4f6c-99c6-3a3c218698ec/54lEkuR72c.json")

# Load project images
heart_disease_project_image = Image.open('book.jpg')

# Add custom CSS for Times New Roman font
st.markdown(
    """
    <style>
        * {
            font-family: 'Times New Roman', Times, serif;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Set the title of the app
st.title("My Data Science Portfolio!")
st.write(
    """Welcome to my data science portfolio! I'm Ashish Nalawade, a passionate data scientist with a solid foundation in Machine Learning, Deep Learning, and Natural Language Processing. This website showcases some of my projects and contributions in the field of data science."""
)

st.write('----------------------------------------------------------------')

with st.container():
    selected = option_menu(
        None, ["About Me", "Projects", "Contact"],
        icons=['person', 'code-slash', 'chat-left-text-fill'],
        menu_icon="cast", default_index=0, orientation="horizontal"
    )

if selected == 'About Me':
    col1, col2 = st.columns(2)
    with col1:
        st.title("I am Ashish Nalawade")
        st.write(
            """I'm a passionate data scientist with a strong foundation in Machine Learning, Deep Learning, and Natural Language Processing. My expertise extends to Data Analytics, where I apply cutting-edge techniques and tools to derive actionable insights from complex datasets.

I am proud to be a Smart India Hackathon finalist, where I showcased my skills in solving real-world problems. Additionally, I have worked on real-time projects leveraging AI, ML, and Data Science modules to deliver impactful solutions.

This portfolio highlights some of my projects and contributions in data science and analytics. I am proficient in tools and technologies such as Tableau, Microsoft Excel, Power BI, Python, and MySQL, which I use to craft compelling visualizations, design efficient workflows, and build robust models.

Explore my work to see how I leverage data-driven approaches to solve real-world problems and create meaningful impact."""
        )
    with col2:
        st_lottie(lottie_data_science)
    st.write('----------------------------------------------------------------')

    with st.container():
        col3, col4 = st.columns(2)

        with col3:
            st.subheader("Education")
            st.write(
                """- Bachelor Of Engineering in Artificial Intelligence And Data Science
    - Jaihind College Of Engineering, Kuran
    - CGPA:  9.40
- Higher Secondary School Certificate 
    - Annasaheb Waghire College, Otur
    - Percentage: 92.46%
- Secondary School Certificate 
    - Shivneri Vidyalaya, Dholwad
    - Percentage: 88.60%        
                """
            )
            st.subheader("Training & Certificates")

            # Certified Data Analyst
            st.write(
                """**Certified Data Analyst**
- Certificate Provider: Excelr Solutions Pune  
- Certification Date: 05-09-2024
                """
            )
            st.markdown("[View Certificate](https://drive.google.com/file/d/1JfnmENrYYmjLv5eOezVdcjOS28erXsR_/view?usp=drive_link)")
            st.markdown("[View Internship Certificate](https://drive.google.com/file/d/1Uk5ZatILKN4UVCnyotltdki24C8dJyfF/view?usp=sharing)")

            # Certified Data Scientist
            st.write(
                """**Certified Data Scientist**
- Certificate Provider: Excelr Solutions Pune  
- Certification Date: 06-12-2024
                """
            )
            st.markdown("[View Certificate](https://drive.google.com/file/d/10kgYJMzK36j8_woPdfCe0xl-0d3puZm7/view?usp=drive_link)")
            st.markdown("[View Internship Certificate](https://drive.google.com/file/d/1O2WV0rPnLbyzj0oDD3S1uFinr2pbLsyW/view?usp=sharing)")
        with col4:
            st.subheader("Technical Skills")
            st.write(
                """- Analytics Tools: MsExcel, PowerBi, Tableau, MySql

- Programming Languages: Python, R, SQL

- Data Manipulation and Analysis: pandas, NumPy, SciPy

- Machine Learning: scikit-learn, TensorFlow, Keras, XGBoost

- Deep Learning: neural networks, CNNs, RNNs using TensorFlow and Keras

- Data Visualization: Tableau, Matplotlib, Seaborn, Plotly

- Big Data Technologies: Spark, Hive

- Natural Language Processing (NLP): NLTK, SpaCy,Hugging Face

- Model Management and Experiment Tracking: MLflow, Optuna

- Version Control: Git, GitHub, DVC, dagshub"""
            )

if selected == 'Projects':
    
    with st.container():
        col5, col6 = st.columns(2)
        
        with col5:
            st.subheader("Resume Classification using ML")
            st.write(
                """
                - Overview: Developed a machine learning model to classify resumes based on their content into predefined categories. This project demonstrates a full machine learning pipeline, including text preprocessing, feature extraction, model building, and deployment.

                - Technologies Used:

                    - Programming Languages: Python
                    - Libraries: scikit-learn, pandas, NumPy, NLTK, Spacy, Matplotlib, Seaborn, Optuna, MLflow
                    - Tools: Jupyter Notebook, Streamlit, Streamlit Cloud
                """
            )
            st.markdown('[Visit Github Repository](https://github.com/AshishNalawade0188/Resume_Classification)')
        
        with col6:
            st.image(r"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWKnuEafd69OnKjoEujUV948muA7ANWHYfuA&s", width=700, use_container_width=True)
    
    with st.container():
        col7, col8 = st.columns(2)
        
        with col7:
            st.subheader("Book Recommendation System")
            st.write(
                """
                - Overview: Built a book recommendation system that suggests books based on user preferences and reading history using collaborative filtering and content-based filtering techniques.

                - Technologies Used:

                    - Programming Languages: Python
                    - Libraries: pandas, NumPy, scikit-learn, NLTK, Surprise, Matplotlib, Seaborn
                    - Tools: Jupyter Notebook, Streamlit, Streamlit Cloud
                """
            )
            st.markdown('[Visit Github Repository](https://github.com/AshishNalawade0188/Book-Recommendation-System)')
        
        with col8:
            st.image(r"https://miro.medium.com/v2/resize:fit:828/format:webp/1*8vUVRUrqjUDlMNFmr0Wx6g.png", width=700, use_container_width=True)


if selected == 'Contact':
    st.subheader('My Contacts')
    left_col, right_col = st.columns(2)
    with left_col:
        st.write("Email: ashishnalawade683@gmail.com")
        st.write("Phone: +91 9130320188")
        st.markdown("LinkedIn: [Profile](https://www.linkedin.com/in/ashishnalawade0188)")
        st.markdown("Github: [Profile](https://github.com/AshishNalawade0188)")
    with right_col:
        st_lottie(lottie_contact_us, height=200)

st.write('----------------------------------------------------------------')
