import streamlit as st 
import pandas as pd 

st.title("Data Cleaning App")

file_Uploader = st.file_uploader("Upload your file", type=["csv","xlsx"])

if file_Uploader is not None:
    try:
        if file_Uploader.name.endswith(".csv"):
            file_Reader = pd.read_csv(file_Uploader)
        else:
             file_Reader = pd.read_excel(file_Uploader)       
         # wait mien check karrha hun 
        st.write("Your Exact Data")         
        st.dataframe(file_Reader)
        st.write("Clean Your Data")

        remove_Missing = st.checkbox("Remove Missing Value")
        remove_Duplicate = st.checkbox("Remove Duplicate Value")

        if remove_Missing:
           file_Reader = file_Reader.dropna()
           st.success("Your missing value has been removed")
    
    
        if remove_Duplicate:
             file_Reader = file_Reader.drop_duplicates()
             st.success("Your duplicate data has been removed")    
    
        st.write("Your cleaned data")    
        st.dataframe(file_Reader)

        @st.cache_data 
        def Download_Button(file_Reader):
            return file_Reader.to_csv(index=False)
        csv = Download_Button (file_Reader)
        st.download_button(
          label = "Download your clean data",
          data = csv,
          file_name = "CleanData.csv",
          mime = "text/csv"
    ) 
    except Exception as last:
        st.write(f"Error:{last}")
        
    