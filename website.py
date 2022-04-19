import streamlit as st
import players
from Players import hurts, wentz, jackson
import pandas as pd

all = pd.concat([hurts.df_hurts, jackson.df_jackson, wentz.df_wentz])

st.title('NFL QBs')
# st.subheader('Hurts')
# st.table(players.get_hurts_passing_stats())
# st.subheader('Jackson')
# st.table(players.get_jackson_passing_stats())
# st.subheader('Wentz')
# st.table(players.get_wentz_passing_stats())

st.subheader('Hurts')
st.table(hurts.df_hurts)
st.subheader('Jackson')
st.table(jackson.df_jackson)
st.subheader('Wentz')
st.table(wentz.df_wentz)
st.subheader('All Players')
st.table(all)