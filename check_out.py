import pandas as pd
import streamlit as st
from db import view_all_customer, view_all_emp, get_details, edit_details,check_out_db

def check_out():
    selected_cust=st.number_input('customer id:')
    result=check_out_db(selected_cust)
    df = pd.DataFrame(result, columns=['e_id', 'e_name', 'e_phone', 'room_assigned', 'service_time', 'work'])
    with st.expander("View all Employees"):
        st.dataframe(df)
    
    