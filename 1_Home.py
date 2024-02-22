import streamlit as st
import pandas as pd 
import numpy as np


st.tabs(["Home", "About us", "Contacts", "Help"])



with open('style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


st.markdown("""
<style>

	.stTabs, .st-ca [data-baseweb="tab-list"] {
		margin-top : -6rem;
        margin-left : -15rem;
    }
    .st-emotion-cache-18ni7ap {
        visibility: hidden;
    }
	.stTabs [aria-selected="true"] {
  		background-color: #FFFFFF;
	}

</style>""", unsafe_allow_html=True)


bottom_bar_html = """
        <style>
            .bottom-bar {
                position: fixed;
                bottom: 0;
                left: 0;
                width: 100%;
                background-color: #2c3e50;
                padding: 1rem;
                display: flex;
                justify-content: space-around;
                align-items: center;
            }
            .bottom-bar a {
                margin: 0 1rem;
            }
            img {
                height: 50px;
                width : 50px;
            }
        </style>
        <div class="bottom-bar">
            <a href=""> <img src= "upload.png" alt="Link 2"> </a>
            <a href=""> <img src="" > </a>
            <a href=""> <img src="" > </a>
        </div>
    """
    
st.markdown(bottom_bar_html, unsafe_allow_html=True)