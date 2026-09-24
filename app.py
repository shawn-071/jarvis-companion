from __future__ import annotations

import base64
from pathlib import Path

import streamlit as st


ROOT = Path(__file__).parent

st.set_page_config(
    page_title="JARVIS Companion",
    page_icon="🕶️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Keep the field guide as a self-contained HTML experience inside Streamlit.
# Inline assets keep image and model downloads working from the iframe.
page = (ROOT / "index.html").read_text(encoding="utf-8")

def as_data_url(path: Path, mime_type: str) -> str:
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"


page = page.replace(
    'src="JARVIS-logo.png"',
    f'src="{as_data_url(ROOT / "JARVIS-logo.png", "image/png")}"',
)
page = page.replace(
    'href="JARVIS_Glasses.obj" download',
    f'href="{as_data_url(ROOT / "JARVIS_Glasses.obj", "text/plain")}" download="JARVIS_Glasses.obj"',
)
page = page.replace(
    'href="JARVIS_Glasses.mtl" download',
    f'href="{as_data_url(ROOT / "JARVIS_Glasses.mtl", "text/plain")}" download="JARVIS_Glasses.mtl"',
)

st.markdown(
    """
    <style>
      [data-testid="stHeader"], [data-testid="stToolbar"], #MainMenu, footer {
        visibility: hidden;
        height: 0;
      }
      [data-testid="stMainBlockContainer"] {
        max-width: none;
        padding: 0;
      }
    </style>
    """,
    unsafe_allow_html=True,
)
st.iframe(page, width="stretch", height="content", tab_index=0)

