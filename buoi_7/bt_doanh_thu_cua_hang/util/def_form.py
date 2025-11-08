import streamlit as st 

def form_add_product():
    with st.expander("Thêm sản phẩm", icon="📝"):
        # Form Add Product
        form_add_product = st.form("form_add_product")
        with form_add_product:
            name = st.text_input("Tên sản phẩm: ")
            number = st.number_input("Số lượng: ", min_value=1, step= 1)
            category = st.selectbox("Danh mục: ",["Điện tử", "Gia dụng", "Mỹ phẩm", "Quần áo", "Giày dép", "Phụ kiện", "Smartphone", "Laptop"])
            price = st.text_input("Giá bán: ")
            status = st.radio("Tình trạng: ", ["Còn hàng", "Hết hàng"], horizontal=True, index=0)
            button = st.form_submit_button("Thêm mặt hàng")
            # Action Add Product
            if(button):
                # Check validate for Name & Price
                isError = False
                if not name:
                    st.warning(":warning: Vui lòng nhập [Tên sản phẩm]!")
                    isError = True
                if not price:
                    st.warning(":warning: Vui lòng nhập [Giá]!")
                    isError = True
                    
                # If have not error, continue insert new product to data
                if not isError:
                    data = {
                        "Tên": name,
                        "Số lượng": number,
                        "Danh mục": category,
                        "Giá bán": f"{format(int(price), ",.0f")} VND",
                        "Tình trạng": status,
                    }
                    # Save item to session
                    st.session_state.lst_product.append(data)
                    st.success(":white_check_mark: Nhập thành công!")



def form_edit_product():
    with st.expander("Sửa sản phẩm", icon="✏️"):
        # Form Add Product
        options= []
        for value in st.session_state.lst_product:
            options.append(value["Tên"])
        select_product = st.selectbox("Chọn sản phẩm cần sửa:", options, index= None)

        # Choose the product item
        if select_product:
            form_edit_product = st.form('form_edit_product', border=False)
            with form_edit_product:
                # Get the info of product detail
                data_editing = {}
                for item in st.session_state.lst_product:
                    if item["Tên"] in select_product:
                        data_editing = item

                number = st.number_input("Số lượng: ", min_value=1, step= 1, value=int(data_editing["Số lượng"]))
                category = st.selectbox("Danh mục: ",["Điện tử", "Gia dụng", "Mỹ phẩm", "Quần áo", "Giày dép", "Phụ kiện", "Smartphone", "Laptop"])
                price = st.text_input("Giá bán: " )
                status = st.radio("Tình trạng: ", ["Còn hàng", "Hết hàng"], horizontal=True, index=0)
                submit_edit = st.form_submit_button("Cập nhật")
                if(submit_edit):
                    isError = False
                    if not price:
                        st.warning(":warning: Vui lòng nhập [Giá]!")
                        isError = True
                    if not isError:
                        # Update a new data for product
                        data_editing.update({
                                    "Tên": data_editing["Tên"],
                                    "Số lượng": number,
                                    "Danh mục": category,
                                    "Giá bán": f"{format(int(price), ",.0f")} VND",
                                    "Tình trạng": status,
                                })
                        st.success(":white_check_mark: Cập nhật thành công!")