from agno.agent import Agent
import os
import agentops
from agno.models.google import Gemini
from agno.tools.yfinance import YFinanceTools
from agno.tools.crawl4ai import Crawl4aiTools
from agno.team.team import Team
from linkup import LinkupClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

AGENTOPS_API_KEY = os.getenv("AGENTOPS_API_KEY") 
agentops.init(
    api_key=AGENTOPS_API_KEY,
    default_tags=['agno']
)
# Initialize the financial analyst agent with Linkup search capability
financial_analyst = Agent(
    name="Financial Analyst with Linkup Search",
    role="Expert in financial analysis and market research using Linkup search",
    model=Gemini(id="gemini-2.5-flash-lite", api_key=os.getenv("GEMINI_API_KEY")),
    tools=[
        # Stock market data and analysis
        YFinanceTools(
            stock_price=True,
            company_info=True,
            stock_fundamentals=True,
            income_statements=True,
            key_financial_ratios=True,
            analyst_recommendations=True,
            historical_prices=True,
            company_news=True,
            technical_indicators=True
        ),
        # Web search for latest information from trusted financial sources
        LinkupClient(api_key=os.getenv("LINKUP_API_KEY"))
    ],
    instructions=[
        # Core analysis approach
        "You are a proactive and autonomous financial analyst providing specific stock recommendations and financial analysis.",
        "When a stock symbol or company name is mentioned, immediately gather and analyze the following:",
        "1. Current price and recent price action",
        "2. Key financial metrics (P/E, P/S, growth rates, margins, etc.)",
        "3. Recent news and market sentiment",
        "4. Analyst ratings and price targets",
        "5. Technical analysis indicators",
        "6. Industry position and competitive advantages",
        "7. Potential risks and challenges",
        "\nThen provide a comprehensive analysis with clear buy/sell/hold recommendation.",
        "\nFor general queries without specific stocks, analyze the overall market and provide 3-5 top stock picks with rationale.",
        "\nUse the Linkup search tool to gather the latest information from these trusted financial domains:",
        "- Market Data: finance.yahoo.com, google.com/finance, marketwatch.com, investing.com",
        "- Financial News: bloomberg.com, reuters.com, cnbc.com, wsj.com, seekingalpha.com",
        "- Research: morningstar.com, zacks.com, tipranks.com, fool.com, investorplace.com",
        "- Technical Analysis: tradingview.com, finviz.com",
        
        # Response format
        "Structure responses with clear, bold headings for each section.",
        "Always include the following sections for stock analysis:",
        "1. **Current Snapshot** (price, market cap, key stats)",
        "2. **Fundamental Analysis** (financial health, growth, valuation)",
        "3. **Technical Analysis** (price trends, support/resistance, indicators)",
        "4. **Market Sentiment** (news, analyst ratings, insider activity)",
        "5. **Investment Thesis** (bull/bear cases, risks, opportunities)",
        "6. **Recommendation** (clear buy/sell/hold with price target and timeframe)",
        "\nUse bullet points for clarity and include relevant metrics in tables when appropriate.",
        
        # Analysis guidelines
        "For any stock query, automatically provide a complete analysis without asking for additional information.",
        "When specific metrics or timeframes aren't mentioned, use these defaults:",
        "- Timeframe: 1 year for price targets",
        "- Risk tolerance: Moderate (balanced growth and stability)",
        "- Investment horizon: Long-term (3-5 years) unless specified otherwise",
        "\nFor general market queries, identify and analyze 3-5 top opportunities across different sectors.",
        "Always include both quantitative metrics and qualitative analysis.",
        "Highlight potential catalysts and risks for each recommendation.",
        
        # Risk disclosure
        "Include a brief risk disclosure at the end of recommendations.",
        "Note that all investments carry risk and past performance is not indicative of future results.",
        
        # Efficiency
        "Be direct and avoid unnecessary disclaimers or hedging.",
        "Prioritize actionable information over general advice.",
        "Update recommendations based on the most current market data available.",
        "When appropriate, provide alternative investment options or hedging strategies."
    ]
)

# Create Web Research Agent
web_research_agent = Agent(
    name="Web Research Agent",
    model=Gemini(id="gemini-2.5-flash-lite", api_key=os.getenv("GEMINI_API_KEY")),
    tools=[Crawl4aiTools(max_length=None)],
    description="You are a web research specialist that helps find and analyze information from the web.",
    instructions=[
        "When given a research query:",
        "1. Use the Crawl4ai tool to gather information from relevant web pages",
        "2. Extract and summarize key information from the crawled content",
        "3. Provide accurate citations for all information sources",
        "4. For financial analysis, focus on: stock performance, company news, and market trends",
        "5. Format the response clearly with proper headings and sections",
        "6. Include direct links to sources when available"
    ],
    markdown=True,
    show_tool_calls=True,
)

# Create Financial Team
finance_team = Team(
    name="Financial Analysis Team",
    mode="route",
    model=Gemini(id="gemini-2.5-flash-lite", api_key=os.getenv("GEMINI_API_KEY")),
    members=[financial_analyst, web_research_agent],
    show_tool_calls=True,
    markdown=True,
    description="A team of financial experts that provides comprehensive stock and market analysis.",
    instructions=[
        "Route financial queries to the most appropriate agent based on the request type:",
        "1. For general financial analysis, market trends, and stock recommendations, use the Financial Analyst.",
        "2. For detailed financial statements, company fundamentals, and raw financial data, use the Financial Data Agent.",
        "3. If uncertain which agent to use, default to the Financial Analyst.",
        "4. Always ensure responses are clear, well-formatted, and include relevant financial metrics.",
        "5. When comparing stocks or analyzing multiple companies, use consistent metrics and time periods."
    ],
    show_members_responses=True,
)

# Example usage
if __name__ == "__main__":
    # Test with a general market query (goes to financial_analyst)
    print("=== General Market Analysis ===")
    finance_team.print_response("What are the top 3 tech stocks to watch this quarter?", stream=True)
    
    # Test with a web research query (goes to web_research_agent)
    print("\n=== Web Research Analysis ===")
    finance_team.print_response("Research the latest news and analysis for Tesla (TSLA)", stream=True)
