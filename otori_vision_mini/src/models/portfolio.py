from decimal import Decimal
from typing import Dict, List
from .token import Token

class Portfolio:
    def __init__(self):
        self.tokens: Dict[str, Token] = {}
        self.total_value: Decimal = Decimal('0')
        self.reinvest_rate: Decimal = Decimal('0.365')
        self.buyback_rate: Decimal = Decimal('0.50')
        self.success_fee_rate: Decimal = Decimal('0.135')

    def add_token(self, token: Token):
        self.tokens[token.id] = token
        self._update_total_value()

    def remove_token(self, token_id: str):
        if token_id in self.tokens:
            del self.tokens[token_id]
            self._update_total_value()

    def _update_total_value(self):
        self.total_value = sum(token.value for token in self.tokens.values())

    def distribute_profits(self, profit: Decimal) -> Dict[str, Decimal]:
        reinvest = profit * self.reinvest_rate
        buyback = profit * self.buyback_rate
        success_fee = profit * self.success_fee_rate

        return {
            'reinvest': reinvest,
            'buyback': buyback,
            'success_fee': success_fee
        }