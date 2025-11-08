import streamlit as st
import util.menu as menu

st.set_page_config(
    page_title="Thống kê",
    layout="wide"
)

#markdown
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Menu
menu.renderMenu()

# Tổng doanh thu tháng
st.subheader("Tổng doanh thu tháng", divider=True)
lst_doanh_thu = [15000000, 12000000, 18000000, 14000000, 16000000, 
                    13000000, 17000000, 19000000, 11000000, 15000000,
                    20000000, 16000000, 14000000, 18000000, 13000000]
st.bar_chart(lst_doanh_thu,
                x_label="Ngày",
                y_label="Doanh thu (triệu VND)",
                color="#ffaa0088")

# Số đơn hàng
st.subheader("Số đơn hàng", divider=True)
lst_đon_hang = [120, 95, 140, 110, 130,
                100, 160, 180, 90, 125,
                200, 150, 115, 170, 105]
st.bar_chart(lst_đon_hang,
                x_label="Ngày",
                y_label="Số đơn hàng",
                color="#0000ff")

# Số khách hàng mới
st.subheader("Số khách hàng mới", divider=True)
lst_khach_hang = [25, 18, 30, 22, 28,
                20, 35, 40, 15, 2,
                20, 32, 24, 38, 21]
st.bar_chart(lst_khach_hang,
                x_label="Ngày",
                y_label="Số khách hàng mới",
                color="#ae22ff74")

# Tổng số sản phẩm bán ra
st.subheader("Tổng số sản phẩm bán ra", divider=True)
lst_sp_ban_ra = [250, 180, 300, 220, 280,
                200, 350, 400, 150, 275,
                320, 290, 240, 380, 210]
st.bar_chart(lst_sp_ban_ra,
                x_label="Ngày",
                y_label="Tổng số sản phẩm bán ra",
                color="#1a7b54")