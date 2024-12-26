import streamlit as st

st.markdown("<h1 style='text-align: center;'>Data Visualizer</h1>", unsafe_allow_html=True)
st.markdown("---")

files = st.file_uploader("Upload multiple files", type=["xlsx"], accept_multiple_files=True)
files_name = list()

if files:
    for file in files:
        files_name.append(file.name)
    selected_file = st.multiselect('Select files', options=files_name)
    if selected_file:
        option = st.radio("Select Entity Against Date", options=["None", "GPU", "CPU", "MOUSE", "KEYBOARD", "CASING"])
        if option != "None":
            print(option)