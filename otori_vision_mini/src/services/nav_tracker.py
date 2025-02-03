from decimal import Decimal
from datetime import datetime
from typing import Dict, List
from ..models.portfolio import Portfolio

class NAVTracker:
    def __init__(self, portfolio: Portfolio):
        self.portfolio = portfolio
        self.nav_history: List[Dict] = []

    def calculate_nav(self) -> Decimal:
        total_supply = sum(token.amount for token in self.portfolio.tokens.values())
        if total_supply == 0:
            return Decimal('0')
        return self.portfolio.total_value / total_supply

    def update_nav(self):
        current_nav = self.calculate_nav()
        self.nav_history.append({
            'timestamp': datetime.now(),
            'nav': current_nav
        })
        return current_nav

    def get_nav_history(self, days: int = 30) -> List[Dict]:
        return self.nav_history[-days:]