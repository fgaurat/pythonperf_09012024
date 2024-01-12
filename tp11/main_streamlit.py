import streamlit as st
from UserDAO import UserDAO
def main():
    dao = UserDAO("./formation.db")
    users = dao.findAll()

    st.set_page_config(layout="wide")
    # streamlit run main_streamlit.py
    st.title('User List')
    st.write('## Bonjour')

    title = st.text_input('Movie title', '')
    

    if st.button("Show"):
        st.write('The current movie title is', title)

    st.table(dao.findAll())

if __name__ == '__main__':
    main()