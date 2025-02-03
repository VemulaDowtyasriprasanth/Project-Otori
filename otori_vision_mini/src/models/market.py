from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import List

@dataclass
class MarketData:
    timestamp: datetime
    ovt_price: Decimal
    oct_price: Decimal
    volume_24h: Decimal
    market_cap: Decimal

class Market:
    def __init__(self):
        self.price_history: List[MarketData] = []
        self.current_data: MarketData = None

    def update_market_data(self, data: MarketData):
        self.current_data = data
        self.price_history.append(data)

    def get_price_history(self, days: int = 30) -> List[MarketData]:
        return self.price_history[-days:]