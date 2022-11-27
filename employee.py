import streamlit as st
from db import view_all_customer, view_all_emp,get_details,view_all_rooms,get_occ,check_out_db
import pandas as pd

def emp():
    result = view_all_emp()
    # st.write(result)
    df = pd.DataFrame(result)
    with st.expander("View all Employees"):
        st.dataframe(df)


def room():
    result = view_all_rooms()
    # st.write(result)
    df = pd.DataFrame(result, columns=['room_no', 'c_id', 'r_service','occupancy'])
    with st.expander("Room details"):
        st.dataframe(df)
    if st.button("Show rooms available"):
        oc=get_occ()
        df = pd.DataFrame(oc, columns=['rooms'])
        with st.expander("View all Rooms Available"):
            st.dataframe(df)

def bill(c_id):
    check_out_db(c_id)