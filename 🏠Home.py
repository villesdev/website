import streamlit as st
import json
from PIL import Image
import requests
import streamlit_lottie
from streamlit_lottie import st_lottie


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


# streamlit run /Users/louisvilleseche/Desktop/Projects/Website/🏠Home.py

st.set_page_config(page_title="Louis", page_icon=":bar_chart:", layout = "wide")
st.sidebar.success("Select a page above.")

# header section
with st.container():
    st.subheader("Hi, I'm Louis :wave:")
    st.title("Bachelor of Commerce student from Melbourne")
    left_column, blank, right_column = st.columns((2,0.2,1))
    with left_column:
        st.subheader("I enjoy learning finance and economics, but am interested in learning Python too. \n\n")
        st.subheader("I'm currently in my second year of a Bachelor of Commerce majoring in Finance at The University of Melbourne. Through my professional experience, I am someone who has developed confidence in leading diverse teams and exceeding high expectations. Additionally, I have a proven capability to deconstruct data and think critically. ")
        st.subheader("[LinkedIn >](https://www.linkedin.com/in/louisvilleseche/)")
    with right_column:
        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()
        lottie_space = load_lottieurl("https://lottie.host/ff2f2bd6-b7fc-4ab3-bba5-2542fcfda441/04T0Hv4vLi.json")
        st_lottie(lottie_space, height=000, width=300, loop=True)

# what i do
with st.container():
    st.write('---')
    left_column, right_column = st.columns((1,2))
    with right_column:
        st.header("What I want to do")
        st.write('##')
        with st.expander("**🐍 Learn Python**"):
            st.write("\n I'm currently learning python to manipulate data and construct interactive visualisations")
        with st.expander('🏦 **Integrate my studies**'):
               "\n I'm learning the best ways to implement topics like finance and economics into python"
        with st.expander('💹 **Have fun**'):
               "\n I want to see how much I can learn Python outside of any structured classes or institution, and of course enjoy the journey"

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
with left_column:
    lottie_spaceship = load_lottieurl("https://lottie.host/448f5a06-142d-4e0d-9f9e-dfaab865a918/CLDEIS44Ey.json")
    st_lottie(lottie_spaceship, height = 300, loop = True)

# projects

with st.container():
    st.write('---')
    st.header("What I've done in the past")
    picture = Image.open("/Users/louisvilleseche/Desktop/Projects/Website/Images/image.png")
    # research
    st.subheader("🔬Student Researcher: **Deakin Integrated Reporting Centre**")
    st.write("**Projects**: Review of ASX300 Corporate Governance Recommendation 4.3 Disclosures: Effectiveness of communication and efficacy of integrity enhancement process"
                 "\n \n Machine Learning and Natural Language Processing of Strategic Reports Prepared in the UK: Capital Market and Real Effects of Sustainability-Related Narrative Reporting")

    # supervisor
    st.subheader("🏥Supervisor: **Victorian Department of Health**")
    st.write("Present seminars to large groups of agents, including daily briefings to organise the workforce, and training sessions as needed. \n \n Convey accurate health advice to the public regarding Covid-19 regulations and vaccinations.\n\nWork across the Vaccinations, Close Contact Outbreak Management, Covid Safe Information teams, and manage critical calls, i.e, threat of harm, agitated callers, media, and lawsuit threats. \n\nAudit and examine call recordings to maintain quality assurance on the accuracy and precision of health advice.")

    # team leader
    st.subheader("🖥️Team Leader: **Foxtel Customer Contact Centre**")
    st.write("Collaborate with a Customer Relationship Manager to align goals and operations by constructing quality assurance frameworks. Communicate issues and report data to the CRM.\n\nAnalyse agent performance data then communicate feedback individually and in groups. Upskill the workforce and run training seminars reducing average hold time by ≈15s.")
    st.write('---')

