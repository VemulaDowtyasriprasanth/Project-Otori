import streamlit as st
import plotly.graph_objects as go
from datetime import datetime, timedelta
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.services.market_simulator import MarketSimulator
from src.services.price_feed import PriceFeed

def render_market():
    st.title("Market Overview")

    # Initialize services
    if 'market_simulator' not in st.session_state:
        st.session_state.market_simulator = MarketSimulator()
    if 'price_feed' not in st.session_state:
        st.session_state.price_feed = PriceFeed()

    # Current Prices
    col1, col2 = st.columns(2)
    current_prices = st.session_state.price_feed.get_current_prices()
    
    with col1:
        st.metric(
            "OVT Price",
            f"${current_prices['OVT']:.4f}",
            "2.5%"
        )
    
    with col2:
        st.metric(
            "OCT Price",
            f"${current_prices['OCT']:.4f}",
            "-1.2%"
        )

    # Price Charts
    st.subheader("Price History")
    
    # Get historical data
    ovt_history = st.session_state.market_simulator.get_price_history('OVT')
    oct_history = st.session_state.market_simulator.get_price_history('OCT')

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=ovt_history['dates'],
        y=ovt_history['prices'],
        name='OVT'
    ))
    fig.add_trace(go.Scatter(
        x=oct_history['dates'],
        y=oct_history['prices'],
        name='OCT'
    ))
    
    fig.update_layout(
        title='Token Prices',
        xaxis_title='Date',
        yaxis_title='Price ($)'
    )
    st.plotly_chart(fig)

    # Market Statistics
    st.subheader("Market Statistics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("24h Volume", "$1.2M", "5.2%")
    with col2:
        st.metric("Market Cap", "$45.6M", "1.8%")
    with col3:
        st.metric("Total Holders", "1,234", "3.1%")

if __name__ == "__main__":
    render_market()