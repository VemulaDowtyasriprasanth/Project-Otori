from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from enum import Enum

class TokenType(Enum):
    OVT = "Liquidity Token"
    OCT = "Revenue Share & Voting Token"

@dataclass
class Token:
    id: str
    token_type: TokenType
    amount: Decimal
    owner: str
    created_at: datetime
    price: Decimal

    @property
    def value(self) -> Decimal:
        return self.amount * self.price