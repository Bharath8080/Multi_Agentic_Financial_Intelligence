# Technical Stock Analyzer

A powerful Streamlit-based web application for technical analysis of stocks, featuring comprehensive charting tools, technical indicators, and AI-powered financial analysis.

## 🌟 Features

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
- **AI-Powered Analysis**: Advanced financial insights using AI models
- **Responsive Design**: Works on desktop and mobile devices
- **Data Export**: Download historical data in CSV format

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

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
   GEMINI_API_KEY=your_gemini_api_key
   AGENTOPS_API_KEY=your_agentops_api_key
   ```

### Running the Application

Start the Streamlit app:
```bash
streamlit run Home.py
```

Open your browser and navigate to `http://localhost:8501`

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

## 📊 Usage

1. **Select a Company**: Choose from the S&P 500 companies
2. **Customize Timeframe**: Select your desired date range
3. **Add Indicators**: Toggle technical indicators from the sidebar
4. **Analyze**: View the interactive charts and technical analysis
5. **Get AI Insights**: Use the AI analysis feature for deeper insights

## 🐳 Docker Support

Build and run the application using Docker:

```bash
# Build the Docker image
docker build -t stock-analyzer .

# Run the container
docker run -p 8501:8501 stock-analyzer
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

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
