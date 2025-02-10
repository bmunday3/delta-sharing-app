import streamlit as st
# from PIL import Image
# from utils import make_grid, generate_image
from dotenv import load_dotenv

import os
# import numpy as np
# import pandas as pd

load_dotenv()

st.set_page_config(
    page_title="SiriusXM Delta Sharing App",
    page_icon="imgs/sxm/small-logo-blue.png",
    initial_sidebar_state="expanded",
    layout="wide"
)

# ~~~~~~~~~~~~~~~
# side bar config
# ~~~~~~~~~~~~~~~
st.sidebar.markdown("\n")
# st.sidebar.image("imgs/logos/small-scale-lockup-full-color-rgb.png")
# st.sidebar.image("imgs/logos/small-scale-lockup-full-color-white-rgb.png")
st.sidebar.image("imgs/sxm/logo-black.png")
# st.sidebar.image("imgs/logos/small-scale-lockup-one-color-white-rgb.png")

st.sidebar.markdown("Placeholder text")
# st.sidebar.markdown("For more information, visit this Databricks solution accelerator to learn more.")
# st.sidebar.link_button(label="Solution Accelerator", type="primary", use_container_width=True, url="https://www.databricks.com/solutions/accelerators/creating-brand-aligned-images-using-gen-ai")

st.sidebar.divider()
st.sidebar.markdown("# App Configuration")
# brand = st.sidebar.radio(label="Select brand for image generation", options=["McDonalds Happy Meal", "Stanley Tumbler"]) # , "Starbucks Cold Brew"
# st.sidebar.markdown("\n")
# st.sidebar.markdown("\n")
# st.sidebar.divider()

st.markdown("# Placeholder title")
st.markdown("## Placeholder subtitle")





