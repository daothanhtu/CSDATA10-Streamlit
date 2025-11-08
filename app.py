import streamlit as st
import util.menu as menu

st.set_page_config(
    page_title="BẢNG ĐIỀU KHIỂN DOANH THU CỬA HÀNG",
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

# Data
if "lst_product" not in st.session_state:
    data_products = [
        {
            "Tên": "Giày Sneaker nữ trắng",
            "Số lượng": "2200",
            "Danh mục": "Giày dép",
            "Giá bán": "450,000 VND",
            "Tình trạng": "Còn hàng",
        },
        {
            "Tên": "Đầm maxi hoa",
            "Số lượng": "1500",
            "Danh mục": "Quần áo",
            "Giá bán": "350,000 VND",
            "Tình trạng": "Còn hàng",
        },
        {
            "Tên": "Áo khoác jean nam",
            "Số lượng": "800",
            "Danh mục": "Quần áo",
            "Giá bán": "550,000 VND",
            "Tình trạng": "Còn hàng",
        },
        {
            "Tên": "Túi xách tay da",
            "Số lượng": "1200",
            "Danh mục": "Phụ kiện",
            "Giá bán": "780,000 VND",
            "Tình trạng": "Còn hàng",
        },
        {
            "Tên": "Macbook Air",
            "Số lượng": "5",
            "Danh mục": "Laptop",
            "Giá bán": "25,000,000 VND",
            "Tình trạng": "Còn hàng",
        }
    ]
    st.session_state.lst_product = data_products

# Sidebar Menu
menu.renderMenu()

# Content
st.title(":bar_chart: Dashboard")
st.caption("Theo dõi doanh thu, đơn hàng, khách hàng và sản phẩm bán chạy")


# Thống kê
# Columns
st.subheader("Thống kê", divider=True)
col_1, col_2, col_3, col_4 = st.columns(4)

with col_1: 
    st.metric(label="Tổng doanh thu tháng", value="300.000.000 đ", delta="33%")
    st.link_button("Xem chi tiết","/dashboard#tong-doanh-thu-thang", type="secondary", use_container_width=True)
with col_2: 
    st.metric(label="Số đơn hàng", value="137", delta="8%")
    st.link_button("Xem chi tiết","/dashboard#so-don-hang", type="secondary", use_container_width=True)
with col_3: 
    st.metric(label="Số khách hàng mới", value="55", delta="4%")
    st.link_button("Xem chi tiết","/dashboard#so-khach-hang-moi", type="secondary", use_container_width=True)
with col_4: 
    st.metric(label="Tổng số sản phẩm bán ra", value="250", delta="10%")
    st.link_button("Xem chi tiết","/dashboard#tong-so-san-pham-ban-ra", type="secondary", use_container_width=True)

st.divider()

# Biểu đồ

# Columns
chart_area, chart_bar = st.columns(2)
with chart_area:
    # Doanh thu theo ngày trong nửa đầu một tháng (1–15).
    lst_doanh_thu = [15000000, 12000000, 18000000, 14000000, 16000000, 
                     13000000, 17000000, 19000000, 11000000, 15000000,
                     20000000, 16000000, 14000000, 18000000, 13000000]
    st.subheader("Doanh thu theo ngày nửa đầu tháng", divider=True)
    st.area_chart(lst_doanh_thu,
                  x_label="Ngày",
                  y_label="Doanh thu (triệu VND)")
    
with chart_bar:
    # Doanh thu 6 tháng gần nhất (Đơn vị triệu VND).
    lst_don_hang = [
                    {"5": 200000000},
                    {"6":150000000},
                    {"7":230000000},
                    {"8":270000000},
                    {"9":350000000},
                    {"10":130000000}
                ]
    
    st.subheader("Doanh thu 6 tháng gần nhất", divider=True)
    st.bar_chart(lst_don_hang, x_label="Tháng", y_label="Doanh thu (triệu VND)")

st.divider()

#   Bảng Top 5 sản phẩm bán chạy
st.subheader("TOP 5 SẢN PHẨM BÁN CHẠY")
top_data = st.session_state.lst_product
search = st.text_input(":mag_right:  Tìm kiếm", placeholder="Nhập từ cần tìm kiếm...")

# Check keywork 
if search:
    search_data = [] # Data after search
    for item in top_data:
        name = item["Tên"]
        category = item["Danh mục"]
        if search in name or search in category: # Check keyword with Name/Category
            search_data.append(item)
        top_data = search_data
else:
    top_data = st.session_state.lst_product

# Show list product
st.table(top_data)
