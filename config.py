# API Configuration (Use environment variables in production)
import os
from dotenv import load_dotenv

load_dotenv()

CONFIG = {
    "ZERODHA_API_KEY": os.getenv("ZERODHA_API_KEY"),
    "ZERODHA_ACCESS_TOKEN": os.getenv("ZERODHA_ACCESS_TOKEN"),
    "NEWSAPI_KEY": os.getenv("NEWSAPI_KEY"),
    "NSE_SYMBOLS": ["RELIANCE", "TCS", "HDFCBANK", "INFY"],
    "RISK_PARAMS": {
        "max_drawdown": 0.15,
        "daily_turnover_limit": 0.2
    }
}
