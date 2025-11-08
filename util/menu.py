import streamlit as st

def renderMenu():
    # st.sidebar.header("Menu")
    st.sidebar.page_link("app.py", label="Dashboard")
    st.sidebar.page_link("pages/products.py", label="Quản lý sản phẩm")
    st.sidebar.page_link("pages/dashboard.py", label="Thống kê")