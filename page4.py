import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.sidebar.markdown("# Page4")
insta = pd.read_csv('uppdatedInstagram.csv')

sp = insta[insta['Main topic']== ('Sports')]
ordered_df = sp.sort_values(by='Likes Avg.')
my_range=range(1,len(sp.index)+1)

# Create a color if the group is "B"
my_color=np.where(ordered_df ['Country']=='US', 'pink','blue')
my_size=np.where(ordered_df ['Country']=='US', 70, 30)
# The horizontal plot is made using the hline() function
plt.hlines(y=my_range, xmin=0, xmax=ordered_df['Likes Avg.'], color=my_color, alpha=0.4)
plt.scatter(ordered_df['Likes Avg.'], my_range, color=my_color, s=my_size, alpha=1)

# Add title and axis names
plt.yticks(my_range, ordered_df['Country'])
plt.title("What about the  US Country ?", loc='Center')
plt.xlabel('Likes Avg')
plt.ylabel('Country')

# show the graph
plt.show()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()
