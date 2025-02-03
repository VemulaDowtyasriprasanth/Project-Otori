from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict

@dataclass
class Proposal:
    id: str
    title: str
    description: str
    creator: str
    created_at: datetime
    end_time: datetime
    options: List[str]
    votes: Dict[str, int] = None

    def __post_init__(self):
        if self.votes is None:
            self.votes = {option: 0 for option in self.options}

@dataclass
class Vote:
    proposal_id: str
    voter: str
    option: str
    voting_power: float
    timestamp: datetime