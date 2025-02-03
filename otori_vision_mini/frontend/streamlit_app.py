import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.services.market_simulator import MarketSimulator
from src.services.voting_service import VotingService

def init_session_state():
    if 'market_simulator' not in st.session_state:
        st.session_state.market_simulator = MarketSimulator()
    if 'voting_service' not in st.session_state:
        st.session_state.voting_service = VotingService()

def render_market_view():
    st.subheader("Market Overview")
    
    # Price Charts
    market_sim = st.session_state.market_simulator
    
    # Simulate new price movement
    market_sim.simulate_price_movement()
    
    # Create price charts
    fig = go.Figure()
    
    for token in ['OVT', 'OCT']:
        history = market_sim.get_price_history(token)
        fig.add_trace(go.Scatter(
            x=history['dates'],
            y=history['prices'],
            name=token,
            mode='lines'
        ))
    
    fig.update_layout(
        title='Token Price History',
        xaxis_title='Date',
        yaxis_title='Price ($)'
    )
    
    st.plotly_chart(fig)

def render_voting_view():
    st.subheader("Governance")
    
    # Create New Proposal
    with st.expander("Create New Proposal"):
        title = st.text_input("Proposal Title")
        description = st.text_area("Proposal Description")
        options = st.text_input("Options (comma-separated)")
        
        if st.button("Create Proposal"):
            if title and description and options:
                options_list = [opt.strip() for opt in options.split(',')]
                proposal_id = st.session_state.voting_service.create_proposal(
                    title=title,
                    description=description,
                    creator="current_user",
                    options=options_list
                )
                st.success(f"Proposal created with ID: {proposal_id}")

    # List Active Proposals
    st.subheader("Active Proposals")
    for proposal_id, proposal in st.session_state.voting_service.proposals.items():
        with st.expander(f"{proposal.title}"):
            st.write(proposal.description)
            st.write(f"Created by: {proposal.creator}")
            st.write(f"End time: {proposal.end_time}")
            
            # Voting Interface
            option = st.selectbox(
                "Cast your vote",
                proposal.options,
                key=f"vote_{proposal_id}"
            )
            
            if st.button("Vote", key=f"vote_button_{proposal_id}"):
                success = st.session_state.voting_service.cast_vote(
                    proposal_id=proposal_id,
                    voter="current_user",
                    option=option
                )
                if success:
                    st.success("Vote cast successfully!")
                else:
                    st.error("Failed to cast vote")
            
            # Show Results
            results = st.session_state.voting_service.get_proposal_results(proposal_id)
            fig = go.Figure(data=[go.Bar(
                x=list(results.keys()),
                y=list(results.values())
            )])
            fig.update_layout(title='Current Results')
            st.plotly_chart(fig)

def main():
    st.title("OTORI Vision Mini")
    init_session_state()
    
    tab1, tab2 = st.tabs(["Market", "Governance"])
    
    with tab1:
        render_market_view()
    
    with tab2:
        render_voting_view()

if __name__ == "__main__":
    main()