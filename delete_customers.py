import pandas as pd
import streamlit as st
from db import view_all_customer, view_all_emp, delete_data


def delete():
    customers = view_all_customer()
    df = pd.DataFrame(customers, columns=['c_id', 'cust_name', 'cust_mobile', 'cust_email', 'check_in', 'check_out'])
    with st.expander("Current data"):
        st.dataframe(df)

    #list_of_trains = [i[0] for i in view_only_train_names()]
    selected_cust = st.number_input("c_id to delete")
    st.warning("Do you want to delete ::{}".format(selected_cust))
    if st.button("Delete customer"):
        delete_data(selected_cust)
        st.success("customer has been deleted successfully")
    new_result = view_all_customer()
    df2 = pd.DataFrame(new_result, columns=['c_id', 'cust_name', 'cust_mobile', 'cust_email', 'check_in', 'check_out'])
    with st.expander("Updated data"):
        st.dataframe(df2)