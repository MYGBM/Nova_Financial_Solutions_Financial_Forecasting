"""
Data loading utilities for stock and news data.
"""
import os
import pandas as pd
from typing import List, Dict, Optional


def load_stock_data(tickers: List[str], base_path: str = "../data/stock_data/") -> Dict[str, pd.DataFrame]:
    """
    Load stock data for multiple tickers.
    
    Args:
        tickers: List of stock ticker symbols (e.g., ['AAPL', 'MSFT'])
        base_path: Base path to stock data directory
        
    Returns:
        Dictionary mapping ticker symbols to DataFrames
    """
    stock_data = {}
    
    for ticker in tickers:
        file_path = os.path.join(base_path, f"{ticker}.csv")
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            # Convert Date column to datetime
            if 'Date' in df.columns:
                df['Date'] = pd.to_datetime(df['Date'])
            stock_data[ticker] = df
        else:
            print(f"Warning: File not found for {ticker}: {file_path}")
    
    return stock_data


def load_news_data(file_path: str = "../data/raw/raw_analyst_ratings.csv", 
                   drop_unnamed: bool = True) -> pd.DataFrame:
    """
    Load news data from CSV file.
    
    Args:
        file_path: Path to news data CSV file
        drop_unnamed: Whether to drop 'Unnamed: 0' column if present
        
    Returns:
        DataFrame containing news data
    """
    news_df = pd.read_csv(file_path, index_col=False)
    
    if drop_unnamed and 'Unnamed: 0' in news_df.columns:
        news_df.drop(columns=['Unnamed: 0'], inplace=True)
    
    # Convert date column to datetime if present
    if 'date' in news_df.columns:
        news_df['date'] = pd.to_datetime(news_df['date'], utc=True, format='mixed')
    
    return news_df


def get_data_info(df: pd.DataFrame) -> None:
    """
    Print basic information about a DataFrame.
    
    Args:
        df: DataFrame to analyze
    """
    print(f"Shape: {df.shape}")
    print(f"\nColumns: {df.columns.tolist()}")
    print(f"\nData types:\n{df.dtypes}")
    print(f"\nMissing values:\n{df.isnull().sum()}")
    print(f"\nBasic statistics:\n{df.describe()}")

