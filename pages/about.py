"""
Entrypoint for streamlit app.
Runs top to bottom every time the user interacts with the app (other than imports and cached functions).
"""

# Library imports
import traceback
import copy

import streamlit as st


from utils.page_components import (
    add_common_page_elements,
)


# def show():
sidebar_container = add_common_page_elements()
page_container = st.sidebar.container()
sidebar_container = st.sidebar.container()

st.divider()

displaytext = """## About xT Model Translation App"""

st.markdown(displaytext)

displaytext = (
    """This application builds on the Twelve Educational framework to demonstrate how different machine learning models can translate their outputs into natural language. """
    """The app showcases multiple xT (expected threat) models for football pass analysis—including Logistic Regression, explainable Neural Networks (xNN), and XGBoost—and uses AI to generate human-readable explanations of each model's predictions. \n\n"""
    """The code is set up in a general way, to allow users to build systems that translate model outputs into text. """
    """The pass analysis tool displays contribution plots showing how different features influence each model's xT prediction. It then generates AI-powered commentary explaining the pass in context, comparing predictions across models."""
)

st.markdown(displaytext)
