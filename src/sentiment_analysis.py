"""
Sentiment analysis utilities using VADER.
"""
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from typing import Dict, Optional


def initialize_sentiment_analyzer() -> SentimentIntensityAnalyzer:
    """
    Initialize and return a VADER sentiment analyzer.
    
    Returns:
        SentimentIntensityAnalyzer instance
    """
    # Download VADER lexicon if not present
    try:
        analyzer = SentimentIntensityAnalyzer()
    except LookupError:
        nltk.download('vader_lexicon', quiet=True)
        analyzer = SentimentIntensityAnalyzer()
    
    return analyzer


def calculate_sentiment_scores(text: str, analyzer: Optional[SentimentIntensityAnalyzer] = None) -> Dict[str, float]:
    """
    Calculate sentiment scores for a text using VADER.
    
    Args:
        text: Text to analyze
        analyzer: SentimentIntensityAnalyzer instance (creates new if None)
        
    Returns:
        Dictionary with sentiment scores (compound, pos, neu, neg)
    """
    if analyzer is None:
        analyzer = initialize_sentiment_analyzer()
    
    return analyzer.polarity_scores(text)


def get_compound_sentiment(text: str, analyzer: Optional[SentimentIntensityAnalyzer] = None) -> float:
    """
    Get compound sentiment score for a text.
    
    Args:
        text: Text to analyze
        analyzer: SentimentIntensityAnalyzer instance (creates new if None)
        
    Returns:
        Compound sentiment score (-1 to 1)
    """
    scores = calculate_sentiment_scores(text, analyzer)
    return scores['compound']


def classify_sentiment(compound_score: float) -> str:
    """
    Classify sentiment based on compound score.
    
    Categories:
    - very-positive: 0.7 - 1.0
    - positive: 0.1 - 0.7
    - neutral: -0.1 - 0.1
    - negative: -0.7 - -0.1
    - very-negative: -1.0 - -0.7
    
    Args:
        compound_score: VADER compound sentiment score
        
    Returns:
        Sentiment category string
    """
    if compound_score >= 0.7:
        return "very-positive"
    elif compound_score >= 0.1:
        return "positive"
    elif compound_score >= -0.1:
        return "neutral"
    elif compound_score >= -0.7:
        return "negative"
    else:
        return "very-negative"


def add_sentiment_analysis(df: pd.DataFrame, 
                          headline_column: str = 'headline',
                          analyzer: Optional[SentimentIntensityAnalyzer] = None) -> pd.DataFrame:
    """
    Add sentiment analysis columns to a DataFrame.
    
    Args:
        df: DataFrame containing headlines
        headline_column: Name of the headline column
        analyzer: SentimentIntensityAnalyzer instance (creates new if None)
        
    Returns:
        DataFrame with added sentiment columns
    """
    df = df.copy()
    
    if analyzer is None:
        analyzer = initialize_sentiment_analyzer()
    
    # Calculate compound sentiment scores
    df['headline_sentiment'] = df[headline_column].apply(
        lambda headline: get_compound_sentiment(headline, analyzer)
    )
    
    # Classify sentiments
    df['sentiment_category'] = pd.cut(
        x=df['headline_sentiment'],
        bins=[-1, -0.7, -0.1, 0.1, 0.7, 1],
        labels=["very-negative", "negative", "neutral", "positive", "very-positive"],
        precision=3
    )
    
    # Add sentiment groups (combine very-positive/positive and very-negative/negative)
    df['sentiment_group'] = df['sentiment_category'].astype(str).replace({
        'very-positive': 'positive',
        'very-negative': 'negative'
    })
    
    return df

