import streamlit as st
from sen_email import send_mail
st.header("Contact me :)")

with st.form(key="email_form"):
    user_email = st.text_input("your email address")
    raw_message = st.text_area("your message")
    message = f"""\
Subject: new email from {user_email}

from: {user_email}
message: {raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_mail(message)
        st.info("Your message sent successfully")
