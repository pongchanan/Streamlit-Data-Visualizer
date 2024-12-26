import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

figure = plt.figure()

def date_converter(date_col):
    # Convert to string format and extract the date part
    result = date_col.dt.strftime('%Y-%m-%d').tolist()
    return result

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
            for file in files:
                if file.name in selected_file:
                    shop_data = pd.read_excel(file, index_col=0)
                    item = list(shop_data[option])
                    dates = date_converter(shop_data["DATE"])
                    index = np.arange(len(dates))
                    plt.plot(index, item)
                    print(dates)
            st.write(figure)