import streamlit as st

st.set_page_config(layout="wide")

#markdown
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)


#Sidebar
st.sidebar.header("Menu")
st.sidebar.page_link("dashboard.py",label="Điều hướng")
st.sidebar.page_link("pages/bao_cao.py",label="Báo cáo")
st.sidebar.page_link("pages/cai_dat.py",label="Cài đặt")
st.sidebar.page_link("pages/nguoi_dung.py",label="Người dùng")
st.sidebar.page_link("pages/bt_menu.py",label="Bài tập menu")
#wrap_content
st.header("Admin dashboard")

#4 columns
col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric(label="Doanh thu hôm nay",value="12,5 M",delta="+ 5%")
with col2:
    st.metric(label="Người dùng mới",value="327",delta="+ 12.5%")
with col3:
    st.metric(label="Đơn hàng",value="142",delta="- 5%")
with col4:
    st.metric(label="Tỉ lệ chuyển đổi",value="3.8%",delta="0.4%")
    
st.markdown("<hr />",unsafe_allow_html=True)

col_doanh_thu, col_don_hang = st.columns(2)

with col_doanh_thu:
    lst_doanh_thu = [6,14,5,15,10]
    st.title("Doanh thu 7 ngày gần nhất")
    st.line_chart(lst_doanh_thu)

with col_don_hang:
    lst_don_hang = [15,35,53,16]
    st.title("Số lượng đơn theo trạng thái")
    st.bar_chart(lst_don_hang)
    
