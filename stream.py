import streamlit as st
import pandas as pd
def main():
    st.title("EXPENSE TRACKER DATA")
    csv_file = "output.csv"  
    df = pd.read_csv(csv_file)
    st.write("Data from the CSV file:")
    st.dataframe(df)
    st.write("Summary statistics:")
    st.write(df.describe())
if __name__ == "__main__":
    main()
    
