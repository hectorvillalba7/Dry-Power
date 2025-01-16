import streamlit as st
from streamlit_option_menu import option_menu

from views.drypower_euro import run as drypower_euro_run
from views.drypower_gbp import run as drypower_gbp_run
from views.drypower_usd import run as drypower_usd_run
from views.drypower_aud import run as drypower_aud_run
from views.drypower_nzd import run as drypower_nzd_run
from views.drypower_cad import run as drypower_cad_run
from views.drypower_chf import run as drypower_chf_run
from views.drypower_jpy import run as drypower_jpy_run

# --- PAGE SETUP ---
pages = {
    "USD": drypower_usd_run,
    "EUR": drypower_euro_run,
    "GBP": drypower_gbp_run,
    "AUD": drypower_aud_run,
    "NZD": drypower_nzd_run,
    "CAD": drypower_cad_run,
    "JPY": drypower_jpy_run,
    "CHF": drypower_chf_run,
}

with st.sidebar:
    st.title("Currency")
    page_selection = option_menu(
        menu_title=None,
        options=list(pages.keys()),
        icons=["currency-dollar","currency-euro","currency-pound","arrow","arrow-forward-ios",
               "arrow-forward-ios", "currency-yen","currency-franc"],  # icons
        menu_icon="cast", 
        default_index=0,  
        styles={
            "container": {"padding": "5px", "background-color": "#f0f2f6"}, 
            "icon": {"color": "black", "font-size": "18px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0px",
                "color": "black",
            },  
            "nav-link-selected": {"background-color": "#007bff", "color": "white"}, #Page selector
        },
    )

# --- RUN SELECTED PAGE ---
pages[page_selection]()

