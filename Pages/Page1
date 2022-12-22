import streamlit as st
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt
import seaborn as sns

st.sidebar.markdown("# Page1")

insta = pd.read_csv('uppdatedInstagram.csv')
st.title('instagram influencers Application')
st.header("instagram influencers Application Charts")

#with st.sidebar:
  #  selected = option_menu("Instagram Web App", ["HomePage","page1", 'page2'], 
 #       icons=['house'], menu_icon="cast", default_index=1)
#    selected

plot_type=st.radio("select from the relations",['Candlestick chart','pie chart','Simple Bar Chart','line Chart','point Chart'])

if plot_type == 'Candlestick chart':
#  t1 = st.header("The relation between Main topic and Likes")
#  p1 = insta.groupby('Main topic')['Likes'].mean().plot(kind='pie',autopct="%1.2f%%") 
  t1 = st.text("The relation between Main topic and Likes")
  p1 = alt.Chart(insta).mark_rule().encode(
  x = 'Main topic',
  y = 'Likes',
  color = 'Main topic').interactive()

elif plot_type == 'pie chart':
  t1 = st.header("The relation between Main topic and Posts")
  p1 = alt.Chart(insta).mark_arc().encode(
    theta=alt.Theta(field="Posts", type="quantitative"),
    color=alt.Color(field="Main topic", type="nominal"))


elif plot_type == 'Simple Bar Chart':
  t1 = st.text("The relation between Main topic and Followers")
  p1 = alt.Chart(insta).mark_bar().encode(
  y = 'Main topic',
  x = 'Followers',
  color = 'Main topic')

elif plot_type == 'line Chart':
  t1 = st.text("The relation between Posts and Likes")
  p1 = alt.Chart(insta).mark_line().encode(
  y = 'Posts',
  x = 'Likes',
  color = 'Main topic').interactive()

else:
  t1 = st.text("The relation between Engagement Rate and Followers")
  p1 = alt.Chart(insta).mark_point().encode(
  x = 'Engagement Rate',
  y = 'Followers',
  color = 'Main topic').interactive()

st.echo(t1)
st.altair_chart(p1) 

st.markdown("------------------------------------------------------------")

option = st.selectbox(
    'Choose one of the options to be compared with Likes',
    ('Followers', 'Engagement Rate'))

st.write('You selected:', option)

if(option == "Followers"):
  A1 = alt.Chart(insta).mark_bar().encode(
  y = 'Likes',
  x = 'Followers',
  color = 'Main topic')
else:
  A1 = alt.Chart(insta).mark_bar().encode(
  y = 'Likes',
  x = 'Engagement Rate',
  color = 'Main topic')

st.altair_chart(A1)

