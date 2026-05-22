import streamlit as st


def footer_home():
    st.markdown(f"""
            <div style="margin-top: 2rem; display:flex; gap:6rem; justify-content: center; item-align:center">
                <p style="font-weight:bold; color:white;">Created with 💖 by <span style="font-weight:bold; color:black;padding-left:4px"> Krishna</span></p>               
            </div>  
                
                """, unsafe_allow_html=True)