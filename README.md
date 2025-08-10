# 🚀 Multi-Agentic Financial Intelligence Platform

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Agno-Framework-orange" alt="Agno Framework">
  <img src="https://img.shields.io/badge/AgentOps-Enabled-success" alt="AgentOps">
</div>

A sophisticated multi-agent financial intelligence platform that combines AI-powered financial analysis with real-time market data, web research capabilities, and interactive visualization. The system leverages multiple specialized AI agents working in concert to provide comprehensive financial insights.

## 🌟 Features

### 🤖 Multi-Agent Architecture
- **Financial Analyst Agent**: Specializes in market analysis, stock recommendations, and financial metrics using YFinance.
- **Web Research Agent**: Performs real-time web research using Crawl4ai for up-to-date information gathering.

### 📊 Core Capabilities
- **Interactive Stock Charts**: View candlestick charts with customizable timeframes
- **Technical Indicators**:
  - Moving Averages (SMA, EMA)
  - MACD (Moving Average Convergence Divergence)
  - RSI (Relative Strength Index)
  - Bollinger Bands
  - Stochastic Oscillator
  - ATR (Average True Range)
  - OBV (On-Balance Volume)
- **S&P 500 Integration**: Access to all S&P 500 constituents
- **Real-time Market Data**: Live stock prices and historical data
- **AI-Powered Analysis**: Advanced financial insights using AI models
- **Web Research**: Real-time information gathering from trusted financial sources
- **Responsive Design**: Works on desktop and mobile devices
- **Data Export**: Download historical data in CSV format

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Required API Keys:
  - GEMINI_API_KEY (for AI analysis)
  - LINKUP_API_KEY (for web search)
  - AGENTOPS_API_KEY (for agent monitoring)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Bharath8080/Multi_Agentic_Financial_Intelligence.git
   cd Multi_Agentic_Financial_Intelligence
   ```

   Or try the live demo: [Multi-Agentic Financial Intelligence](https://multi-agentic-financial-intelligence.onrender.com)

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root and add your API keys:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   LINKUP_API_KEY=your_linkup_api_key_here
   AGENTOPS_API_KEY=your_agentops_api_key_here
   ```

### Running the Application

Start the Streamlit app:
```bash
streamlit run Home.py
```

Open your browser and navigate to `http://localhost:8501`

## 🤖 Agent Capabilities

### Financial Analyst Agent
- **Purpose**: Provides in-depth financial analysis and stock recommendations
- **Capabilities**:
  - Technical analysis using various indicators
  - Fundamental analysis of stocks
  - Market trend analysis
  - Portfolio optimization suggestions
  - Risk assessment

### Web Research Agent
- **Purpose**: Gathers and synthesizes information from the web
- **Capabilities**:
  - Real-time web research
  - Information extraction from financial websites
  - News aggregation and summarization
  - Source citation and verification
  - Market sentiment analysis

## 🎯 Usage Examples

### General Market Analysis
```python
# Get analysis of top tech stocks
response = finance_team.run("What are the top 3 tech stocks to watch this quarter?")
```

### Stock-Specific Research
```python
# Get detailed analysis of a specific stock
response = finance_team.run("Provide a comprehensive analysis of AAPL including technical and fundamental metrics")
```

### Web Research
```python
# Get latest news and analysis
response = finance_team.run("Research the latest developments in electric vehicle market")
```

## 🚀 Deployment

### Local Development
1. Follow the installation steps above
2. Run the Streamlit app:
   ```bash
   streamlit run Home.py
   ```
3. Access the app at `http://localhost:8501`

### Cloud Deployment (Render)
1. Fork this repository
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Set environment variables in the Render dashboard
5. Deploy!

## 📊 Features in Detail

## 🛠 Project Structure

```
Technical_Stock_Analyzer/
├── Home.py               # Main Streamlit application
├── Dockerfile            # Container configuration
├── requirements.txt      # Python dependencies
├── data_loader.py        # Data fetching and processing
├── finance_team.py       # AI-powered financial analysis
├── indicators.py         # Technical indicator calculations
├── plotting.py           # Chart visualization functions
└── utils.py              # Utility functions
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🛠️ Development

### Project Structure
```
├── Home.py               # Main Streamlit application
├── finance_team.py       # Multi-agent financial analysis team
├── pages/                # Additional Streamlit pages
│   └── 1_Fintelligence.py  # Financial intelligence interface
├── data_loader.py        # Data loading and processing
├── indicators.py         # Technical indicators implementation
├── plotting.py           # Chart visualization utilities
└── utils.py              # Helper functions
```

### Adding New Agents
1. Create a new agent in `finance_team.py`
2. Add it to the team configuration
3. Define its capabilities and tools
4. Update the routing instructions

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Bharath Munakala**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/bharathmunakala04/)

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Market data powered by [Yahoo Finance](https://finance.yahoo.com/)
- AI capabilities powered by [Gemini](https://ai.google.dev/)
- Technical analysis with [pandas](https://pandas.pydata.org/) and [TA-Lib](https://mrjbq7.github.io/ta-lib/)

---

<div align="center">
  Made with ❤️ for traders and investors
</div>
