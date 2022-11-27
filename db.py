import mysql.connector
import streamlit as st

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="project"
)
c = mydb.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Train2 (Train_No int, Name varchar(30), Train_Type varchar(20), Source varchar(20), Destination varchar(20), Availability varchar(5));')


def add_data_customer(c_id, cust_name, cust_mobile, cust_email, check_in, check_out):
    c.execute('INSERT INTO customer (c_id, cust_name, cust_mobile, cust_email, check_in, check_out) VALUES (%s,%s,%s,%s,%s,%s);',
              (c_id, cust_name, cust_mobile, cust_email, check_in, check_out))
    c.execute('call assign_room({})'.format(c_id))
    mydb.commit()


def view_all_customer():
    c.execute('SELECT * FROM customer')
    customers = c.fetchall()
    return customers


def view_all_emp():
    c.execute('SELECT * from emp')
    emp = c.fetchall()
    return emp

def view_all_rooms():
    c.execute('select r.room_no,r.c_id,r.r_service,occupancy.room_occ from room_details as r join occupancy WHERE r.room_no=occupancy.room_no')
    rooms = c.fetchall()
    return rooms

def get_details(c_id):
    c.execute('SELECT * FROM customer WHERE c_id="{}"'.format(c_id))
    data = c.fetchall()
    return data

def get_occ():
    c.execute('SELECT room_no FROM occupancy where room_occ="no"')
    occ=c.fetchall()
    return occ

def check_out_db(c_id):
    c.execute('call check_out("{}")'.format(c_id))
    out=c.fetchall()
    return out

def query():
    st.write('Query:')
    with st.form("SQL input:"):
        sql=st.text_input('sql statement:').lower()
        submitted=st.form_submit_button("submit")
    if submitted:
        c.execute(sql)
        for i in c.fetchall():
            st.text(i)

def edit_details(new_c_id, new_cust_name, new_cust_mobile, new_cust_email, new_check_in, new_check_out, c_id, cust_name, cust_mobile, cust_email, check_in, check_out):
    c.execute("UPDATE customer SET c_id=%s, cust_name=%s, cust_mobile=%s, cust_email=%s, check_in=%s, check_out=%s WHERE "
              "c_id=%s and cust_name=%s and cust_mobile=%s and cust_email=%s and check_in=%s and check_out=%s", (new_c_id, new_cust_name, new_cust_mobile, new_cust_email, new_check_in, new_check_out, c_id, cust_name, cust_mobile, cust_email, check_in, check_out))
    
    mydb.commit()
    data = c.fetchall()
    return data


def delete_data(c_id):
    #c.execute('DELETE FROM customer WHERE c_id="{}"'.format(c_id))
    c.execute('DELETE FROM customer WHERE c_id=1')
    mydb.commit()