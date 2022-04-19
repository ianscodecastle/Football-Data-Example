import streamlit as st
import players
from Players import hurts, wentz, jackson
import pandas as pd

all = pd.concat([hurts.df_hurts, jackson.df_jackson, wentz.df_wentz], ignore_index=True, sort=False)

st.title('NFL QBs')

st.subheader('Hurts')
st.table(hurts.df_hurts)

st.subheader('Jackson')
st.table(jackson.df_jackson)

st.subheader('Wentz')
st.table(wentz.df_wentz)

st.subheader('All Players')
st.table(all)