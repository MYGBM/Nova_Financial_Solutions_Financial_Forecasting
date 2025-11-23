"""
Text processing utilities for news headlines.
"""
import string
import pandas as pd
import nltk
from typing import List, Tuple, Optional
from collections import Counter
from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import TrigramAssocMeasures


def download_nltk_data(packages: List[str] = None) -> None:
    """
    Download required NLTK data packages.
    
    Args:
        packages: List of NLTK package names to download
    """
    if packages is None:
        packages = ["vader_lexicon", "stopwords", "punkt_tab", "averaged_perceptron_tagger"]
    
    nltk.download(packages, quiet=True)


def get_tokens(headline: str, 
               remove_stopwords: bool = True,
               remove_punctuation: bool = True,
               lowercase: bool = True) -> List[str]:
    """
    Tokenize a headline and return cleaned tokens.
    
    Args:
        headline: The headline text to tokenize
        remove_stopwords: Whether to remove stop words
        remove_punctuation: Whether to remove punctuation
        lowercase: Whether to convert to lowercase
        
    Returns:
        List of cleaned tokens
    """
    # Download required NLTK data if not already present
    try:
        stop_words = set(nltk.corpus.stopwords.words('english'))
    except LookupError:
        download_nltk_data(["stopwords", "punkt_tab"])
        stop_words = set(nltk.corpus.stopwords.words('english'))
    
    punctuation = set(string.punctuation)
    
    if lowercase:
        headline = headline.lower()
    
    try:
        tokens = nltk.word_tokenize(headline)
    except LookupError:
        download_nltk_data(["punkt_tab"])
        tokens = nltk.word_tokenize(headline)
    
    result = []
    for token in tokens:
        token = token.strip()
        if not token:
            continue
        
        # Filter conditions
        if remove_stopwords and token in stop_words:
            continue
        if remove_punctuation and token in punctuation:
            continue
        if not token.isalpha():
            continue
        
        result.append(token)
    
    return result


def get_word_frequencies(headlines: List[str], top_n: Optional[int] = None) -> List[Tuple[str, int]]:
    """
    Get word frequency counts from a list of headlines.
    
    Args:
        headlines: List of headline strings
        top_n: Number of top words to return (None for all)
        
    Returns:
        List of (word, count) tuples, sorted by frequency
    """
    # Tokenize all headlines
    all_tokens = []
    for headline in headlines:
        tokens = get_tokens(headline)
        all_tokens.extend(tokens)
    
    # Count frequencies
    word_counts = Counter(all_tokens)
    
    if top_n:
        return word_counts.most_common(top_n)
    return word_counts.most_common()


def get_trigrams(headlines: List[List[str]], 
                 freq_filter: int = 20, 
                 top_n: int = 50) -> List[Tuple[str, str, str]]:
    """
    Find significant trigrams from tokenized headlines.
    
    Args:
        headlines: List of tokenized headlines (list of lists of words)
        freq_filter: Minimum frequency for a trigram to be considered
        top_n: Number of top trigrams to return based on PMI
        
    Returns:
        List of top significant trigrams
    """
    # Flatten all tokenized words into a single list
    all_words = [word for tokens in headlines for word in tokens]
    
    # Create a TrigramCollocationFinder
    finder = TrigramCollocationFinder.from_words(all_words)
    
    # Apply frequency filter to remove rare trigrams
    finder.apply_freq_filter(freq_filter)
    
    # Get the top N trigrams based on Pointwise Mutual Information (PMI)
    significant_trigrams = finder.nbest(TrigramAssocMeasures.pmi, top_n)
    
    return significant_trigrams


def add_headline_length(df: pd.DataFrame, headline_column: str = 'headline') -> pd.DataFrame:
    """
    Add a column with headline lengths to the DataFrame.
    
    Args:
        df: DataFrame containing headlines
        headline_column: Name of the headline column
        
    Returns:
        DataFrame with added 'headline_length' column
    """
    df = df.copy()
    df[headline_column] = df[headline_column].astype(str)
    df['headline_length'] = df[headline_column].apply(len)
    return df

