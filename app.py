import streamlit as st
from travel_agent import travel_agent

st.set_page_config(page_title="AI Travel Planner")

st.title("🌍 LLM Travel Agent")

city = st.text_input("Destination")
days = st.selectbox("Duration", ["2 days", "3 days"])

if st.button("Plan Trip"):

    if not city:
        st.warning("Enter a city")
    else:
        query = f"Plan a {days} trip to {city}"

        with st.spinner("Thinking..."):
            try:
                result = travel_agent.invoke({"input": query})
                st.markdown(result["output"])
            except Exception as e:
                st.error(str(e))