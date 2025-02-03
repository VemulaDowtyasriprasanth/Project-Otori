import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.services.nav_tracker import NAVTracker
from src.services.token_service import TokenService
from src.models.token import TokenType

def render_home():
    st.title("OTORI Vision Mini - Dashboard")
    
    # Initialize services if not in session state
    if 'token_service' not in st.session_state:
        st.session_state.token_service = TokenService()
    
    # Token Supply Overview
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(
            "OVT Supply", 
            f"{st.session_state.token_service.total_ovt_supply:,.0f}",
            "1.2%"
        )
    
    with col2:
        st.metric(
            "OCT Supply", 
            f"{st.session_state.token_service.total_oct_supply:,.0f}",
            "-0.5%"
        )

    # Portfolio Value Chart
    st.subheader("Portfolio Value Over Time")
    dates = [datetime.now().strftime("%Y-%m-%d") for _ in range(30)]
    values = [100 + i * 2 for i in range(30)]  # Sample data
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=values, mode='lines', name='Portfolio Value'))
    fig.update_layout(
        title='Portfolio Performance',
        xaxis_title='Date',
        yaxis_title='Value ($)'
    )
    st.plotly_chart(fig)

    # Recent Activity
    st.subheader("Recent Activity")
    activity_data = [
        {"time": "2 mins ago", "action": "Token Burn", "details": "50,000 OVT burned"},
        {"time": "5 mins ago", "action": "New Investment", "details": "Added to Portfolio A"},
        {"time": "1 hour ago", "action": "Profit Distribution", "details": "36.5% Reinvested"}
    ]
    
    for activity in activity_data:
        st.write(f"**{activity['time']}:** {activity['action']} - {activity['details']}")

if __name__ == "__main__":
    render_home()