from decimal import Decimal
from datetime import datetime
import random

class PriceFeed:
    def __init__(self):
        self.ovt_price = Decimal('1.0')
        self.oct_price = Decimal('1.0')
        self.volatility = Decimal('0.02')

    def get_current_prices(self):
        # Simulate price movements
        self.ovt_price *= (1 + Decimal(str(random.uniform(-0.02, 0.02))))
        self.oct_price *= (1 + Decimal(str(random.uniform(-0.02, 0.02))))
        
        return {
            'OVT': self.ovt_price,
            'OCT': self.oct_price,
            'timestamp': datetime.now()
        }