import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import altair as alt
import seaborn as sns

st.sidebar.markdown("# Home Page")

insta = pd.read_csv('uppdatedInstagram.csv')
st.title('instagram influencers Application')
st.header("About the Dataset:...")
st.markdown("Instagram is a photo and video sharing social networking service founded in 2010") 
st.markdown("by Kevin Systrom and Mike Krieger, and later acquired by American company Facebook Inc.") 
st.markdown("The app allows users to upload media that can be edited with filters and organized by ") 
st.markdown("hashtags and geographical tagging. Posts can be shared publicly or with preapproved followers.")  
st.markdown("Users can browse other users' content by tag and location, view trending content, like photos, ") 
st.markdown("and follow other users to add their content to a personal feed.")
st.markdown("in addition, in this pages you will find finalization and the findings of a dataset comprises of 200 top influencers profile data of instagram")
    

st.header("Findings from instagram influencers dataset:...")
nof = st.select_slider(
    'Select a number to view:',
    options=['1', '2', '3', '4', '5'])
st.write('Findings NO:', nof)

if (nof == '1'):
  st.markdown("the candlestick chart below shows The number of likes for each Main topic ")
  st.markdown("clearly shows that the sports topic has the largest number of likes, it was about more than ")
  st.markdown("20.000.000,000 likes, which means that sport is one of the people's most important concerns.") 
  st.markdown("In contrast, the news had the lowest number of likes, it was much less than 5.000.000.000..")

elif (nof == '2'):
  st.markdown("The simple bar chart below shows the number of followers for each main topic")
  st.markdown("was clearly the most for a sports topic, and the number of ")
  st.markdown("followers was about 2,000,000,000. In contrast, the people & blogs had the fewest followers,") 
  st.markdown("which shows that most people are interested in sports and don't tend to the people & blogs.")

elif (nof == '3'):
  st.markdown("The line chart below shows The number of likes of each post, it is clear that comedy has")
  st.markdown("the number of posts around 100,000, So comedy has the highest number of posts, ")
  st.markdown("but the number of likes is it is much less than 20,000,000,000 compared to sports") 
  st.markdown("a small number of posts are less than 20,000, but the number of likes was more than 20,000,000.")

elif (nof == '4'):
  st.markdown("The point chart below shows the Engagement rate and the number of followers,")
  st.markdown("Obviously, it's a film and animation has a large number of followers about 500,000,000 but the") 
  st.markdown("Engagement rate was about 0.0, in contrast, the gaming topic has a few followers but the Engagement") 
  st.markdown("rate had the highest of all, was about 0.3 and this means that he's The most inclined people Engagement") 
  st.markdown("in gaming topics.")

else:
  st.markdown("The pie chart below shows the number of posts and the main topic. The comedy topic received more  ")
  st.markdown("comedy topic had the most number of posts, and in contrast, the news and politics  topics had the") 
  st.markdown("lowest number of posts")
