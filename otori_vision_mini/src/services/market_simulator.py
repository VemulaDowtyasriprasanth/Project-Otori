import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List

class MarketSimulator:
    def __init__(self):
        self.price_history: Dict[str, List[float]] = {
            'OVT': [],
            'OCT': []
        }
        self.current_prices = {'OVT': 1.0, 'OCT': 1.0}
        self.volatility = 0.02

    def simulate_price_movement(self):
        for token in ['OVT', 'OCT']:
            change = np.random.normal(0, self.volatility)
            new_price = self.current_prices[token] * (1 + change)
            self.current_prices[token] = max(0.01, new_price)
            self.price_history[token].append(new_price)

    def get_price_history(self, token: str, days: int = 30) -> Dict:
        if token not in self.price_history:
            return {}
            
        history = self.price_history[token][-days:]
        dates = [(datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d') 
                for i in range(len(history)-1, -1, -1)]
        
        return {
            'dates': dates,
            'prices': history
        }