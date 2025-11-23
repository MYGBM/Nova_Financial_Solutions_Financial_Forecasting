# Predicting Price Moves with News Sentiment

A comprehensive data science project that analyzes the correlation between financial news sentiment and stock market price movements. This project performs detailed exploratory data analysis on a large corpus of financial news articles (1.4M+ articles) and correlates sentiment patterns with historical stock price data for major technology companies.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Data](#data)
- [Usage](#usage)
- [Analysis Components](#analysis-components)
- [Technologies Used](#technologies-used)
- [Key Findings](#key-findings)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)

## 🎯 Overview

This project aims to discover meaningful correlations between news sentiment and stock market movements by:

1. **Analyzing Financial Data**: Examining historical stock prices for 6 major tech stocks (AAPL, AMZN, GOOG, META, MSFT, NVDA) with technical indicators
2. **Processing News Data**: Performing comprehensive EDA on over 1.4 million financial news articles from 2009-2020
3. **Sentiment Analysis**: Using VADER sentiment analyzer to classify news articles into sentiment categories
4. **Correlation Discovery**: Identifying patterns and relationships between news sentiment and price movements

## ✨ Features

- **Stock Price Analysis**: Technical analysis including moving averages, price trends, and support/resistance levels
- **News Data Exploration**: Comprehensive EDA on publication patterns, publishers, and article characteristics
- **Sentiment Classification**: Automated sentiment analysis using VADER (Very-positive, Positive, Neutral, Negative, Very-negative)
- **Time Series Analysis**: Seasonal decomposition of publication patterns (daily, monthly, yearly)
- **Text Mining**: Tokenization, n-gram analysis, and word frequency analysis
- **Publisher Analysis**: Identification of top publishers and organizational patterns
- **Visualization**: Rich visualizations using matplotlib and seaborn

## 📁 Project Structure

```
Predicting-Price-Moves-with-News-Sentiment/
│
├── data/
│   ├── raw/
│   │   └── raw_analyst_ratings.csv    # News articles dataset (1.4M+ records)
│   ├── processed/                      # Processed datasets
│   └── stock_data/                     # Historical stock price data
│       ├── AAPL.csv
│       ├── AMZN.csv
│       ├── GOOG.csv
│       ├── META.csv
│       ├── MSFT.csv
│       └── NVDA.csv
│
├── notebooks/
│   ├── financial_analysis.ipynb        # Stock price analysis and technical indicators
│   └── news_data_eda.ipynb             # News data exploration and sentiment analysis
│
├── scripts/                            # Utility scripts (to be developed)
├── src/                                # Source code modules (to be developed)
├── tests/                              # Unit tests
│   └── basic_test.py
│
├── requirements.txt                    # Python dependencies
├── LICENSE                             # MIT License
└── README.md                           # This file
```

## 🚀 Installation

### Prerequisites

- Python 3.12+
- pip (Python package manager)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Predicting-Price-Moves-with-News-Sentiment
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK data**
   ```python
   import nltk
   nltk.download(['vader_lexicon', 'stopwords', 'punkt_tab', 'averaged_perceptron_tagger'])
   ```

### Note on TA-Lib

TA-Lib (Technical Analysis Library) may require additional setup:

- **Windows**: Download the wheel file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib) or use conda:
  ```bash
  conda install -c conda-forge ta-lib
  ```

- **macOS**: 
  ```bash
  brew install ta-lib
  pip install TA-Lib
  ```

- **Linux**: 
  ```bash
  sudo apt-get install ta-lib
  pip install TA-Lib
  ```

## 📊 Data

### Stock Data

Historical stock price data for 6 major technology companies:
- **AAPL** (Apple Inc.)
- **AMZN** (Amazon.com Inc.)
- **GOOG** (Alphabet Inc.)
- **META** (Meta Platforms Inc.)
- **MSFT** (Microsoft Corporation)
- **NVDA** (NVIDIA Corporation)

Each dataset contains:
- Date
- Open, High, Low, Close prices
- Volume

### News Data

The `raw_analyst_ratings.csv` file contains:
- **1,407,328** financial news articles
- **Date Range**: February 14, 2009 - June 11, 2020
- **Columns**:
  - `headline`: Article headline text
  - `url`: Source URL
  - `publisher`: Publisher name/organization
  - `date`: Publication timestamp
  - `stock`: Associated stock ticker

**Data Characteristics**:
- No missing values
- Headline length: 3-512 characters (avg: 40.7)
- Multiple publishers and organizations
- UTC timestamps

## 💻 Usage

### Running the Notebooks

1. **Start Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

2. **Open and run notebooks**:
   - `notebooks/financial_analysis.ipynb`: Stock price analysis and moving averages
   - `notebooks/news_data_eda.ipynb`: News data exploration and sentiment analysis

3. **Execute cells sequentially** to reproduce the analysis

### Key Analysis Workflows

#### Financial Analysis (`financial_analysis.ipynb`)
- Loads historical stock data for 6 tech stocks
- Converts dates to datetime format
- Visualizes price movements (Open, Close, High, Low)
- Calculates 40-period Simple Moving Averages (SMA)
- Analyzes support/resistance patterns

#### News Data EDA (`news_data_eda.ipynb`)
- Descriptive statistics and data quality checks
- Headline length analysis
- Publisher distribution analysis
- Publication time patterns (hour, day, month, year)
- Text tokenization and n-gram analysis
- Time series decomposition
- VADER sentiment analysis
- Sentiment distribution visualization

## 🔍 Analysis Components

### 1. Stock Price Analysis
- **Moving Averages**: 40-period SMA to identify trends
- **Price Patterns**: Support/resistance level identification
- **Multi-stock Comparison**: Comparative analysis across 6 stocks

### 2. News Data Exploration
- **Descriptive Statistics**: Dataset overview and quality assessment
- **Text Analysis**: 
  - Tokenization with stopword removal
  - Word frequency analysis
  - Trigram collocation analysis
- **Temporal Analysis**:
  - Publication hour/day/month/year distributions
  - Seasonal decomposition (trend, seasonal, residual)
- **Publisher Analysis**:
  - Top publishers by article count
  - Organization extraction from email domains
  - Publisher sentiment patterns

### 3. Sentiment Analysis
- **VADER Sentiment Scoring**: Compound sentiment scores (-1 to +1)
- **Sentiment Categories**:
  - Very-positive: 0.7 - 1.0
  - Positive: 0.1 - 0.7
  - Neutral: -0.1 - 0.1
  - Negative: -0.7 - -0.1
  - Very-negative: -1.0 - -0.7
- **Sentiment Distribution**: Proportion analysis across categories
- **Publisher Sentiment**: Sentiment patterns by publisher

## 🛠 Technologies Used

### Core Libraries
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **matplotlib**: Plotting and visualization
- **seaborn**: Statistical data visualization

### Natural Language Processing
- **nltk**: Natural language toolkit
  - VADER sentiment analyzer
  - Tokenization
  - Stopwords
  - N-gram analysis
- **textblob**: Text processing
- **vaderSentiment**: Sentiment analysis

### Financial Analysis
- **TA-Lib**: Technical analysis indicators (moving averages, etc.)

### Time Series Analysis
- **statsmodels**: Statistical modeling and time series analysis

### Development Tools
- **jupyter**: Interactive notebook environment
- **pytest**: Testing framework

## 📈 Key Findings

### Stock Analysis
- Moving averages act as support/resistance levels for stock prices
- Prices tend to stay above/below moving averages and revert to them before crossing
- Moving averages help reduce unpredictability in price movements

### News Data Insights
- **Publication Patterns**:
  - Higher publication rates on weekdays vs. weekends
  - Constant trend from January to April
  - Sharp decline from August to September
  - Peak publication period: 2009-2011

- **Text Characteristics**:
  - Average headline length: ~41 characters
  - Most headlines range from 47-87 characters (25th-75th percentile)

- **Sentiment Distribution**:
  - Balanced distribution across sentiment categories
  - Publisher-specific sentiment patterns identified

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Mariam Y Gustavo** - Copyright (c) 2025

---

## 🔮 Future Enhancements

Potential areas for future development:
- Machine learning models to predict price movements from sentiment
- Real-time sentiment analysis pipeline
- Correlation analysis between sentiment scores and price changes
- Advanced technical indicators integration
- Web scraping for real-time news data
- API development for sentiment-based trading signals

---

**Note**: This project is for educational and research purposes. Always conduct thorough analysis and consult with financial advisors before making investment decisions.
