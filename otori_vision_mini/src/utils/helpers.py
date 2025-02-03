from decimal import Decimal
from datetime import datetime, timedelta

def format_currency(amount: Decimal) -> str:
    return f"${amount:,.2f}"

def calculate_percentage_change(old_value: Decimal, new_value: Decimal) -> Decimal:
    if old_value == 0:
        return Decimal('0')
    return ((new_value - old_value) / old_value) * 100

def get_time_periods(days: int) -> list:
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    return [start_date + timedelta(days=x) for x in range(days)]