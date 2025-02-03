from datetime import datetime, timedelta
from typing import List, Dict
from ..models.voting import Proposal, Vote

class VotingService:
    def __init__(self):
        self.proposals: Dict[str, Proposal] = {}
        self.votes: Dict[str, List[Vote]] = {}
        self.oct_balances: Dict[str, float] = {}

    def create_proposal(self, title: str, description: str, creator: str, 
                       options: List[str], duration_days: int = 7) -> str:
        proposal_id = f"PROP_{len(self.proposals)}"
        proposal = Proposal(
            id=proposal_id,
            title=title,
            description=description,
            creator=creator,
            created_at=datetime.now(),
            end_time=datetime.now() + timedelta(days=duration_days),
            options=options
        )
        self.proposals[proposal_id] = proposal
        self.votes[proposal_id] = []
        return proposal_id

    def cast_vote(self, proposal_id: str, voter: str, option: str) -> bool:
        if proposal_id not in self.proposals:
            return False
        
        proposal = self.proposals[proposal_id]
        if datetime.now() > proposal.end_time:
            return False

        voting_power = self.oct_balances.get(voter, 0)
        vote = Vote(
            proposal_id=proposal_id,
            voter=voter,
            option=option,
            voting_power=voting_power,
            timestamp=datetime.now()
        )
        
        self.votes[proposal_id].append(vote)
        proposal.votes[option] += voting_power
        return True

    def get_proposal_results(self, proposal_id: str) -> Dict[str, float]:
        if proposal_id not in self.proposals:
            return {}
        
        proposal = self.proposals[proposal_id]
        return proposal.votes