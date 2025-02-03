from decimal import Decimal
from datetime import datetime
from typing import Dict
from ..models.token import Token, TokenType

class TokenService:
    def __init__(self):
        self.tokens: Dict[str, Token] = {}
        self.total_ovt_supply = Decimal('0')
        self.total_oct_supply = Decimal('0')

    def create_token(self, token_type: TokenType, amount: Decimal, 
                    owner: str, price: Decimal) -> Token:
        token_id = f"{token_type.name}_{len(self.tokens)}"
        
        token = Token(
            id=token_id,
            token_type=token_type,
            amount=amount,
            owner=owner,
            created_at=datetime.now(),
            price=price
        )
        
        self.tokens[token_id] = token
        
        if token_type == TokenType.OVT:
            self.total_ovt_supply += amount
        else:
            self.total_oct_supply += amount
            
        return token

    def burn_tokens(self, token_type: TokenType, amount: Decimal):
        if token_type == TokenType.OVT:
            self.total_ovt_supply -= amount
        else:
            self.total_oct_supply -= amount