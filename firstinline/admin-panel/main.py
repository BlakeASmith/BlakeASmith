import streamlit as st

import stateful

stateful.load()

st.title("FirstInLine Developer Dashboard")

venue = st.selectbox(
    label="Choose a venue",
    options=["Oak Bay Recreation Center"],
)

date_input = stateful.record(st.date_input)

date = date_input("date")

if st.button("Clear"):
    date_input.state.clear()
    stateful.clear()
    []
else:
    [str(d) for d in date_input.state]

session = st.multiselect(
    label="Choose a session",
    options=[1, 2, 3],
)

stateful.save()
