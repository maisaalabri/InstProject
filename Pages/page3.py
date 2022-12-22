import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import pandas as pd
import streamlit as st

st.sidebar.markdown("# Page3")

insta = pd.read_csv('uppdatedInstagram.csv')
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

b = insta['Likes Avg.']

ax.scatter(insta['Followers'], insta['Likes Avg.'], insta['Engagement Rate'] , c='b', marker='o', label='blue')
ax.set_xlabel('Followers')
ax.set_ylabel('Likes Avg.')
ax.set_zlabel('Engagement Rate')
plt.title("3D Scatter Plot Example")
plt.legend()
plt.tight_layout()
plt.show()
st.pyplot(fig)
