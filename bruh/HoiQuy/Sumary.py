import streamlit as st


def display():
    st.title("Hồi quy tuyến tính")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        ["Các khái niệm", "Ví dụ 1", "Ví dụ 2", "Hồi quy đa thức", "Nhược điểm", "Giải pháp"])

    with tab1:
        import bruh.HoiQuy.Theory as theory
        theory.display()
    with tab2:
        st.title("Ví dụ hồi quy tuyến tính")
        import bruh.HoiQuy.Bai01
        bruh.HoiQuy.Bai01.display()
    with tab3:
        st.title("Ví dụ đường hồi quy tuyến tính")
        import bruh.HoiQuy.Bai02
        bruh.HoiQuy.Bai02.display()
    with tab4:
        st.title("Các bài toán có thể giải bằng linear regression")
        import bruh.HoiQuy.Bai03
        bruh.HoiQuy.Bai03.display()
    with tab5:
        st.title("Hạn chế của linear regression")
        import bruh.HoiQuy.Bai04
        bruh.HoiQuy.Bai04.display()
    with tab6:
        st.title("Giải pháp")
        import bruh.HoiQuy.Bai05
        bruh.HoiQuy.Bai05.display()
