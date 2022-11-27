import streamlit as st
from db import add_data_customer


def check_in():
    col1, col2 = st.columns(2)
    with col1:
        c_id = st.number_input("Customer ID:")
        cust_name = st.text_input("Customer Name:")
        cust_mobile = st.number_input("Customer mobile:")
        cust_email=st.text_input("Customer Emai")
    with col2:
        check_in=st.date_input("check in:")
        check_out=st.date_input("check out:")

    if st.button("Add Customer"):
        add_data_customer(c_id, cust_name, cust_mobile, cust_email, check_in, check_out)
        st.success("Successfully added Customer: {}".format(c_id))