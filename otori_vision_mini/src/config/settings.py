import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "OTORI Vision Mini"
    DEBUG = True
    INITIAL_OVT_SUPPLY = 1000000
    INITIAL_OCT_SUPPLY = 1000000
    INITIAL_PRICE = 1.0
    
    # Rates
    REINVEST_RATE = 0.365
    BUYBACK_RATE = 0.50
    SUCCESS_FEE_RATE = 0.135

settings = Settings()