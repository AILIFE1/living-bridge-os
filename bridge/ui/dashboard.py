import streamlit as st

st.title("🌉 Living Bridge OS v0.1 Dashboard")

st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Go to", ["Active Mission", "Memory Browser", "Artifact Browser", "Debate Timeline"])

if page == "Active Mission":
    st.header("🚀 Active Mission")
    objective = st.text_input("Mission Objective")
    if st.button("Launch Mission"):
        st.success("Mission launched! (API integration pending)")

st.info("Multi-agent collaboration environment - Persistent knowledge building in progress.")
