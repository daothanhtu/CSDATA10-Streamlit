import streamlit as st
import util.menu as menu
import util.def_form as def_form


st.set_page_config(
    page_title="Quản lý sản phẩm",
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

# Create a session for product
if "lst_product" not in st.session_state:
    # Data Demo
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


# Content
st.header(":file_folder: Quản lý sản phẩm")

# Columns
col_addProduct, col_ProductsList = st.columns([1,3])

# Expander: Add Product 
def_form.form_add_product()


# Expander: Edit product
def_form.form_edit_product()

# List Products
st.subheader("Danh sách sản phẩm", divider="gray")
products = st.session_state.lst_product
search = st.text_input(":mag_right:  Tìm kiếm", placeholder="Nhập từ cần tìm kiếm...")

# Check keywork 
if search:
    search_data = [] # Data after search
    for item in products:
        name = item["Tên"]
        category = item["Danh mục"]
        if search in name or search in category: # Check keyword with Name/Category
            search_data.append(item)
        products = search_data
else:
    products = st.session_state.lst_product
# Show list product
st.table(products)