import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

def render_analytics():
    st.title("Analytics Dashboard")

    # Time Period Selector
    time_period = st.selectbox(
        "Select Time Period",
        ["24 Hours", "7 Days", "30 Days", "90 Days"]
    )

    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Value Locked", "$12.5M", "8.1%")
    with col2:
        st.metric("Trading Volume", "$1.2M", "5.2%")
    with col3:
        st.metric("Active Users", "1,234", "3.1%")
    with col4:
        st.metric("Proposals Created", "45", "2.5%")

    # Portfolio Distribution
    st.subheader("Portfolio Distribution")
    portfolio_data = {
        'Category': ['Web3', 'DeFi', 'NFT', 'Gaming', 'Infrastructure'],
        'Value': [30, 25, 15, 20, 10]
    }
    fig = px.pie(portfolio_data, values='Value', names='Category')
    st.plotly_chart(fig)

    # Token Metrics
    st.subheader("Token Metrics")
    col1, col2 = st.columns(2)
    
    with col1:
        # OVT Supply Chart
        supply_data = pd.DataFrame({
            'Date': pd.date_range(start='2024-01-01', periods=30),
            'Supply': [1000000 - i*1000 for i in range(30)]
        })
        fig = px.line(supply_data, x='Date', y='Supply', title='OVT Supply')
        st.plotly_chart(fig)
    
    with col2:
        # OCT Distribution
        distribution_data = {
            'Category': ['Treasury', 'Community', 'Team', 'Investors'],
            'Amount': [40, 30, 20, 10]
        }
        fig = px.pie(distribution_data, values='Amount', names='Category', title='OCT Distribution')
        st.plotly_chart(fig)

if __name__ == "__main__":
    render_analytics()