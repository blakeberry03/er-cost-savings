# Save this as app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="ER Cost Savings Dashboard",
    page_icon="💰",
    layout="centered"
)

st.title("💡 ER Cost Savings Dashboard")
st.markdown("""
Explore potential cost savings by redirecting ER visits to urgent care or primary care.
Adjust the sliders to see how savings change.
""")

# Inputs
er_visits = st.slider(
    "Number of ER visits per year",
    min_value=30000,
    max_value=150000,
    value=50000,
    step=1000
)

redirect_pct = st.slider(
    "Percentage of visits redirected (%)",
    min_value=10,
    max_value=40,
    value=20
)

avg_er_cost = 1600  # Average ER cost per visit

# Calculation
savings = er_visits * (redirect_pct / 100) * avg_er_cost

st.markdown(f"### 💰 Estimated Savings: ${savings:,.0f}")

# Optional: show savings across the range of redirect percentages
percent_range = list(range(10, 41, 1))
savings_data = pd.DataFrame({
    "Redirect Percentage": percent_range,
    "Savings ($)": [er_visits * (p / 100) * avg_er_cost for p in percent_range]
})

fig = px.line(
    savings_data,
    x="Redirect Percentage",
    y="Savings ($)",
    title=f"Savings vs. Percentage of ER Visits Redirected (ER Visits = {er_visits})",
    markers=True
)
fig.update_layout(yaxis_tickprefix="$", yaxis_tickformat=",")
st.plotly_chart(fig, use_container_width=True)
