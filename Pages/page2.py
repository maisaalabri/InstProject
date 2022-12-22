import streamlit as st
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt
import seaborn as sns

st.sidebar.markdown("# Page2")

insta = pd.read_csv('uppdatedInstagram.csv')
st.title('instagram influencers Application')
st.header("instagram influencers Application Charts")

st.markdown("------------------------------------------------------------")
st.markdown("---The Relation between Main topic and Engagement Rate with Likes---")
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

S1 = alt.Chart(insta).mark_circle(color=color).encode(
x = 'Main topic',
y = 'Engagement Rate' ,
    size='Main topic',
tooltip=['Likes','Engagement Rate']).interactive()

st.altair_chart(S1)

st.markdown("------------------------------------------------------------")

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(insta)

st.download_button(
    label="Download tha dataset as CSV",
    data=csv,
    file_name='instagram.csv',
    mime='text/csv',
)
