import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.services.voting_service import VotingService

def render_voting():
    st.title("Governance")

    # Initialize voting service
    if 'voting_service' not in st.session_state:
        st.session_state.voting_service = VotingService()

    # Create New Proposal
    st.subheader("Create New Proposal")
    with st.form("new_proposal"):
        title = st.text_input("Proposal Title")
        description = st.text_area("Proposal Description")
        options = st.text_input("Options (comma-separated)")
        duration = st.number_input("Duration (days)", min_value=1, value=7)
        
        submitted = st.form_submit_button("Create Proposal")
        if submitted and title and description and options:
            options_list = [opt.strip() for opt in options.split(',')]
            proposal_id = st.session_state.voting_service.create_proposal(
                title=title,
                description=description,
                creator="current_user",
                options=options_list,
                duration_days=duration
            )
            st.success(f"Proposal created with ID: {proposal_id}")

    # Active Proposals
    st.subheader("Active Proposals")
    for proposal_id, proposal in st.session_state.voting_service.proposals.items():
        with st.expander(f"{proposal.title}"):
            st.write(proposal.description)
            st.write(f"Created by: {proposal.creator}")
            st.write(f"End time: {proposal.end_time}")
            
            # Voting Interface
            selected_option = st.selectbox(
                "Select your vote",
                proposal.options,
                key=f"vote_{proposal_id}"
            )
            
            if st.button("Cast Vote", key=f"vote_button_{proposal_id}"):
                success = st.session_state.voting_service.cast_vote(
                    proposal_id=proposal_id,
                    voter="current_user",
                    option=selected_option
                )
                if success:
                    st.success("Vote cast successfully!")
                else:
                    st.error("Failed to cast vote")
            
            # Results
            results = st.session_state.voting_service.get_proposal_results(proposal_id)
            fig = go.Figure(data=[go.Bar(
                x=list(results.keys()),
                y=list(results.values())
            )])
            fig.update_layout(title='Current Results')
            st.plotly_chart(fig)

if __name__ == "__main__":
    render_voting()