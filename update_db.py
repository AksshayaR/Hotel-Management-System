import datetime

import pandas as pd
import streamlit as st
from db import view_all_customer, view_all_emp, get_details, edit_details


def update_customer():
    result = view_all_customer()
    # st.write(result)
    df = pd.DataFrame(result, columns=['c_id', 'cust_name', 'cust_mobile', 'cust_email', 'check_in', 'check_out'])
    with st.expander("View all Customers"):
        st.dataframe(df)
    
    selected_customer = st.number_input("Customer to Edit")
    selected_result = get_details(selected_customer)
    st.write(selected_result)
    if selected_result:
        c_id = selected_result[0][0]
        cust_name = selected_result[0][1]
        cust_mobile = selected_result[0][2]
        cust_email = selected_result[0][3]
        check_in = selected_result[0][4]
        check_out = selected_result[0][5]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_c_id = c_id
            new_cust_name = st.text_input("Customer Name:")
            new_cust_mobile = st.number_input("Customer mobile:")
            new_cust_email=st.text_input("Customer Email:")
        with col2:
            new_check_in=st.date_input("check in:")
            new_check_out=st.date_input("check out:")

        if st.button("Update Customer"):
            edit_details(new_c_id, new_cust_name, new_cust_mobile, new_cust_email, new_check_in, new_check_out, c_id, cust_name, cust_mobile, cust_email, check_in, check_out)
            st.success("Successfully updated")
            
    result2 = view_all_customer()
    df2 = pd.DataFrame(result2, columns=['c_id', 'cust_name', 'cust_mobile', 'cust_email', 'check_in', 'check_out'])
    with st.expander("Updated data"):
        st.dataframe(df2)