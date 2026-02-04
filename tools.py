import yfinance as yf


def get_stock_data(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        return {
            "company": info.get("longName", ticker),
            "price": info.get("currentPrice", "N/A"),
            "previous_close": info.get("previousClose", "N/A"),
            "market_cap": info.get("marketCap", "N/A"),
            "sector": info.get("sector", "N/A"),
            "summary": info.get("longBusinessSummary", "N/A"),
        }

    except Exception:
        return {
            "company": ticker,
            "price": "N/A",
            "previous_close": "N/A",
            "market_cap": "N/A",
            "sector": "Unknown",
            "summary": "Stock data unavailable."
        }


def get_news(company: str):
    return [
        f"{company} announced recent quarterly results.",
        f"Market sentiment around {company} remains mixed.",
        f"Analysts discuss growth opportunities and risks for {company}."
    ]
