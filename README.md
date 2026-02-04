
# Stock GenAI – Multi-Agent Stock Analysis System

## 📌 Overview
Stock GenAI is a **web-based stock analysis application** built using **Google Gemini API**, **LangGraph**, and **Streamlit**.  
The system uses a **multi-agent architecture** to fetch stock data, process contextual information, and generate AI-powered market insights.

The application runs in a browser and provides:
- Real-time stock information
- Company details
- AI-generated market trend, risks, and outlook


## 🧠 System Architecture

The system follows a **multi-agent workflow orchestrated using LangGraph**:


User (Browser)
↓
Streamlit UI (app.py)
↓
LangGraph Orchestrator
↓
Data Collector Agent
↓
Stock Data + News Context
↓
Stock Analyst Agent (Gemini)
↓
AI Analysis Output
↓
Browser Display


### 🔹 Agents Used
1. **Data Collector Agent**
   - Collects stock price, company details, and recent news
   - Structures raw data into readable context

2. **Stock Analyst Agent**
   - Uses Gemini API
   - Analyzes collected data
   - Produces:
     - Market trend
     - Key risks
     - Short-term outlook
## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit** – Web UI
- **LangGraph** – Multi-agent orchestration
- **Google Gemini API** – LLM reasoning
- **Yahoo Finance (yfinance)** – Stock data
- **CSS** – UI styling
## 📂 Project Structure

stock-genai/
│
├── app.py              # Streamlit application
├── agents.py           # Gemini-powered agents
├── tools.py            # Stock data utilities
├── requirements.txt    # Dependencies
├── README.md
├── .env                # API key
│
└── assets/
└── style.css       # Custom CSS

## ⚙️ Setup Instructions

### 1️⃣ Clone or Download the Project
git clone <repository-url>
cd stock-genai

### 2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### 4️⃣ Configure Gemini API Key

Create a `.env` file in the project root:
GEMINI_API_KEY=your_gemini_api_key_here

### 5️⃣ Run the Application
streamlit run app.py

## 🌐 Example Usage

1. Open the browser link shown in terminal:
   http://localhost:8501

2. Enter a stock ticker:

   TSLA

3. Click **Analyze Stock**

### Output Includes:

* Company name
* Current stock price
* Previous close
* Market cap
* Sector
* Company summary
* AI-generated:

  * Market trend
  * Risk analysis
  * Short-term outlook

## 📊 Sample Output (Browser)

* **Company:** Tesla Inc.
* **Current Price:** $XXX
* **Sector:** Consumer Cyclical
* **AI Analysis:**
  *“Tesla shows moderate growth potential driven by innovation, while facing risks related to market volatility and regulatory pressures.”*

## ✅ Key Features

* Multi-agent architecture using LangGraph
* Real-time stock data integration
* Gemini-powered intelligent analysis
* Web-based UI with CSS styling
* Modular and extensible design

## 📌 Notes

* If Yahoo Finance rate-limits requests, the system automatically uses fallback logic.
* Gemini model used: `models/gemini-flash-latest`
