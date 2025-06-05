import streamlit as st
import pandas

#st.set_page_config(layout="wide")

col1, col2, = st.columns(2)

with col1:
    st.image("images/photo.png")


with col2:
    st.title("CAN SEVER")
    content = """
    I'm a Computer Engineering student based in Warsaw with hands-on experience in e-commerce and web development.
    
I ran an Etsy shop where I used Excel to analyze data and improve sales performance. I also interned as a Front-End Web Developer and gained practical skills in Python, Git, and JavaScript.

I enjoy solving problems, learning new technologies, and building things. I'm currently looking for entry-level roles or internships in software or data-related fields.
    """
    st.info(content)

content2 = """
Below you can find some apps that I've built in Python. Feel free to contact me!
"""
st.write(content2)

col3, col4 = st.columns(2)
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
