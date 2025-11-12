import streamlit as st
from agents import planner_agent, researcher_agent, reviewer_agent
from state_manager import init_state, add_to_history, clear_history
from agents import planner_agent, researcher_agent, reviewer_agent
from state_manager import init_state, add_to_history, clear_history
st.set_page_config(page_title="Multi-Agent AI MVP", layout="centered")
init_state()

st.title("🧠 Multi-Agent AI System — MVP")
st.write("Modular · Stateful · Gamified — Minimal MVP (no API required)")

col1, col2 = st.columns([4,1])
user_input = col1.text_input("Enter a task or question:", placeholder="e.g., Design a chatbot plan")
run_btn = col2.button("Run Agents")

if st.button("Clear History"):
    clear_history()
    st.success("History cleared.")

if run_btn and user_input.strip():
    add_to_history("user", user_input)

    plan = planner_agent(user_input)
    add_to_history("planner", plan)

    research = researcher_agent(plan)
    add_to_history("researcher", research)

    review_msg, score = reviewer_agent(research + plan)
    add_to_history("reviewer", f"{review_msg} — Score: {score}/10")

st.markdown("---")
st.subheader("Session History")
for item in st.session_state.history:
    st.markdown(f"**{item['role'].capitalize()}**:\n\n{item['content']}")