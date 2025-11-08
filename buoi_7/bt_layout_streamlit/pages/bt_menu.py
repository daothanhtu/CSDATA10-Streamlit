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
# st.sidebar.page_link("pages/cai_dat.py",label="Cài đặt")
st.sidebar.page_link("pages/nguoi_dung.py",label="Người dùng")
st.sidebar.page_link("pages/bt_menu.py",label="Bài tập menu")
#wrap_content:

#Dữ liệu của các món ăn (st.session_state.lst_mon_an)
if "lst_mon_an" not in st.session_state:
    st.session_state.lst_mon_an = []
    
st.title("Menu KFC Mini")
dict_menu_gia = {
    "ga_ran": 35_000,
    "bo":45_000,
    "khoai":25_000,
    "pepsi":15_000,
    "kem":40_000
}
dict_menu =  {
    "ga_ran": 1,
    "bo":1,
    "khoai":1,
    "pepsi":1,
    "kem":40_000
}


col_chon_mon_an, col_hoa_don = st.columns(2)
with col_chon_mon_an:
    frm_mon_an = st.form("frm_mon_an")
    with frm_mon_an:
        st.title("Chọn món ăn:")
        dict_menu["ga_ran"] = st.number_input("Gà rán",max_value=10,min_value=1,value=1,step=1)
        dict_menu["bo"] = st.number_input("Bò",max_value=10,min_value=1,value=1,step=1)
        dict_menu["khoai"] = st.number_input("Khoai tây chiên",max_value=10,min_value=1,value=1,step=1)
        dict_menu["pepsi"] = st.number_input("Pepsi",max_value=10,min_value=1,value=1,step=1)
        dict_menu["kem"] = st.number_input("Kem vani",max_value=10,min_value=1,value=1,step=1)
        
        btn = frm_mon_an.form_submit_button(label="Đặt món")
with col_hoa_don:
    st.title("Hoá đơn của bạn")
    lst_mon_an = []
    for key in dict_menu:
        item = {
            "Món ăn": key,
            "Đơn giá": dict_menu_gia[key],
            "Số lượng": dict_menu[key],
            "Thành tiền": dict_menu_gia[key] * dict_menu[key]
        }
        lst_mon_an.append(item)
    st.table(lst_mon_an)
    tong_tien = 0
    for item in lst_mon_an:
        tong_tien += item["Thành tiền"]
    st.title(f"Tổng hoá đơn: {tong_tien}") 

    

