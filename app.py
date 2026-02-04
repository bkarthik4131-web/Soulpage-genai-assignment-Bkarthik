import streamlit as st
from tools import get_stock_data, get_news
from agents import collector_agent, analyst_agent
from langgraph.graph import StateGraph, END
from typing import TypedDict


# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Stock GenAI",
    page_icon="📈",
    layout="wide"
)


# ---------- LOAD CSS ----------
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# ---------- LANGGRAPH STATE ----------
class StockState(TypedDict):
    ticker: str
    collected: str
    analysis: str


def collector_node(state: StockState):
    data = get_stock_data(state["ticker"])
    news = get_news(data["company"])
    collected = collector_agent(data, news)
    return {"collected": collected}


def analyst_node(state: StockState):
    analysis = analyst_agent(state["collected"])
    return {"analysis": analysis}


graph = StateGraph(StockState)
graph.add_node("collector", collector_node)
graph.add_node("analyst", analyst_node)
graph.set_entry_point("collector")
graph.add_edge("collector", "analyst")
graph.add_edge("analyst", END)
app_graph = graph.compile()


# ---------- UI ----------
st.title("📊 Stock GenAI – Intelligent Stock Analysis")

ticker = st.text_input("Enter Stock Ticker (AAPL, TSLA, INFY)", "TSLA")

if st.button("Analyze Stock"):
    with st.spinner("Fetching data and analyzing..."):
        stock_data = get_stock_data(ticker)
        result = app_graph.invoke({"ticker": ticker})

    st.subheader("🏢 Company Details")
    col1, col2, col3 = st.columns(3)

    col1.metric("Company", stock_data["company"])
    col2.metric("Current Price", stock_data["price"])
    col3.metric("Previous Close", stock_data["previous_close"])

    st.markdown(f"""
    **Sector:** {stock_data['sector']}  
    **Market Cap:** {stock_data['market_cap']}
    """)

    st.subheader("📄 Company Summary")
    st.write(stock_data["summary"])

    st.subheader("🤖 AI Stock Analysis")
    st.write(result["analysis"])
