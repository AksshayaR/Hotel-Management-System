import streamlit as st




from see_customers import read
from update_db import update_customer
from check_out import check_out
from check_in import check_in
from delete_customers import delete
from employee import emp,room,bill
from db import query


def main():
    st.title("Hotel Management System")
    cust_menu = ["Check in", "View customers", "Edit customers","delete customer","Edit customer Info", "check out"]
    choice = st.sidebar.selectbox("Customer Menu", cust_menu)

    
    if choice == "Check in":
        st.subheader("Enter customer Details:")
        check_in()
        query()

    elif choice == "View customers":
        st.subheader("View customers Details:")
        read()
    elif choice == "Edit customers":
        st.subheader("Edited customers Details:")
        update_customer()

    elif choice == "delete customer":
        st.subheader("Delete customer Details:")
        delete()

    elif choice == "Edit customers Info":
        st.subheader("Edited customers Details:")
        read()

    elif choice == "check out":
        st.subheader("check out:")
        check_out()

    else:
        st.subheader("About hotel")

    emp_menu=['show employees','Room Details','Billing Details']
    emp_choice = st.sidebar.selectbox("Employee Menu", emp_menu)
    if emp_choice=='show employees':
        st.subheader("Employee Details:")
        emp()

    elif emp_choice=='Room Details':
        st.subheader("Room Details:")
        room()

    elif emp_choice=='Billing Details':
        st.subheader("Billing Details:")
        cus=st.number_input("customer id:")
        bill(cus)

if __name__ == '__main__':
    main()