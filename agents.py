import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use model you VERIFIED works
model = genai.GenerativeModel("models/gemini-flash-latest")


def collector_agent(stock_data, news):
    prompt = f"""
You are a Stock Data Collector Agent.

Stock Data:
{stock_data}

Recent News:
{news}

Organize the information clearly.
"""
    return model.generate_content(prompt).text


def analyst_agent(collected_data):
    prompt = f"""
You are a Stock Market Analyst.

Based on the data below, provide:
1. Market trend
2. Key risks
3. Short-term outlook

Data:
{collected_data}
"""
    return model.generate_content(prompt).text
