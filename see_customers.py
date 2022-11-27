import pandas as pd
import streamlit as st

from db import view_all_customer


def read():
    result = view_all_customer()
    # st.write(result)
    df = pd.DataFrame(result, columns=['c_id', 'cust_name', 'cust_mobile', 'cust_email', 'check_in', 'check_out'])
    with st.expander("View all Customers"):
        st.dataframe(df)
    