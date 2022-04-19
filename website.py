import streamlit as st
from urllib.request import urlopen
from PIL import Image
from Players import hurts, wentz, jackson
import pandas as pd

all = pd.concat([hurts.df_hurts, jackson.df_jackson, wentz.df_wentz], ignore_index=True, sort=False)

header_image = Image.open(urlopen('https://i.pinimg.com/originals/93/b6/2e/93b62e4a2d6df775a6c198d6578f5a5f.png'))
st.image(header_image)
st.title('NFL QBs')

st.subheader('Hurts')
st.table(hurts.df_hurts)

st.subheader('Jackson')
st.table(jackson.df_jackson)

st.subheader('Wentz')
st.table(wentz.df_wentz)

st.subheader('All Players')
st.table(all)