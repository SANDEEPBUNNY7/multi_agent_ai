# state_manager.py
import streamlit as st

def init_state():
    """Initialize Streamlit session state."""
    if "history" not in st.session_state:
        st.session_state.history = []

def add_to_history(role: str, content: str):
    """Add messages to the session history."""
    st.session_state.history.append({"role": role, "content": content})

def clear_history():
    """Clear stored conversation."""
    st.session_state.history = []
