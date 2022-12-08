import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


st.set_page_config(page_title="Tyler Cossairt", page_icon="", layout="wide")


with open("styles.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)



def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


profile_img = Image.open("./images/IMG_1329.jpeg")
logistics_img = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_vfiyayoi.json")


with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Hey there, I'm Tyler!")
        st.write("I'm a data analyst and currently work in Logitics Operations.")
        st.write("I provide data-driven solutions to help improve business processes.")
        st.write("I'm currently at Computer Science student at Western Governors University.")

    with right_column:
        st.image(profile_img, use_column_width=False)

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("My Work")
        st.subheader("Company: Arthrex Inc.")
        st.write("Title: Logistics Operations Specialist Sr.")
        st.write("Duration: 2012 - Present")
        st.write("""
                    •Implemented business intelligence solutions using Microsoft Power BI to provide actionable insights and track KPIs for company stakeholders.\n
                    •Improved business processes, systems, and strategies to optimize Arthrex operations and value.\n
                    •Established SOPs and workflows supporting Arthrex initiatives by gathering business and implementation requirements.\n
                    •Collaborate with internal and external stakeholders to address issues in respect of supply chain and logistical concerns.
                """)

    with right_column:
        st_lottie(logistics_img, height=300, key="logistics")


with st.container():
    st.write("---")
    st.write("##")
    projects_column, skills_column = st.columns (2)
    with projects_column:
        st.header("My Projects")
        st.markdown("[C++ Application](https://github.com/tyler-cossairt/classroster)")
        st.write("A C++ app that outputs data regarding members of a roster array.")
        st.markdown("[Python Application](https://github.com/tyler-cossairt/portfolio)")
        st.write("See the Python code that went into building this app.")
    with skills_column:
        st.header("Skills")
        st.write("""
                    •Python\n
                    •SQL\n
                    •Microsoft Power BI\n
                    •C++\n
                    •HTML/CSS\n
                """)


with st.container():
    st.write("---")
    st.header("Let's get in touch!")
    st.write("##")

    contact_form = """
                    <form action="https://formsubmit.co/tylercossairt22@gmail.com" method="POST">
                    <input type="hidden" name="captcha" value="false">
                    <input type="text" name="name" placeholder="Your name" required>
                    <input type="email" name="email" placeholder="Your email" required>
                    <textarea name="message" placeholder="Your message here" required></textarea>
                    <button type="submit">Send</button>
                    </form>
                    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
