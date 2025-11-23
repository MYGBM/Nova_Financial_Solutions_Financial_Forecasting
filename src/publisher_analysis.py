"""
Publisher analysis utilities.
"""
import pandas as pd
from typing import Optional


def get_top_publishers(df: pd.DataFrame,
                      publisher_column: str = 'publisher',
                      headline_column: str = 'headline',
                      top_n: int = 20) -> pd.DataFrame:
    """
    Get top publishers by article count.
    
    Args:
        df: DataFrame with publisher data
        publisher_column: Name of the publisher column
        headline_column: Name of the headline column (for counting)
        top_n: Number of top publishers to return
        
    Returns:
        DataFrame with top publishers
    """
    publisher_grouping = df.groupby(publisher_column).count().sort_values(
        by=headline_column, ascending=False
    )
    return publisher_grouping[[headline_column]].head(top_n)


def extract_organization_from_email(email: str) -> str:
    """
    Extract organization/domain name from an email address.
    
    Args:
        email: Email address string
        
    Returns:
        Organization name (domain without extension)
    """
    if '@' not in email:
        return email
    
    # Split on @ and get the domain part
    domain = email.split('@')[1]
    # Split on . and get the first part (organization name)
    organization = domain.split('.')[0]
    
    return organization


def add_organization_column(df: pd.DataFrame,
                           publisher_column: str = 'publisher',
                           organization_column: str = 'organization') -> pd.DataFrame:
    """
    Add organization column by extracting from email addresses in publisher column.
    
    Args:
        df: DataFrame with publisher data
        publisher_column: Name of the publisher column
        organization_column: Name for the new organization column
        
    Returns:
        DataFrame with added organization column
    """
    df = df.copy()
    
    # Filter publishers that contain '@'
    email_mask = df[publisher_column].str.contains('@', na=False)
    
    # Extract organization for email publishers
    df.loc[email_mask, organization_column] = df.loc[email_mask, publisher_column].apply(
        extract_organization_from_email
    )
    
    return df


def get_organization_counts(df: pd.DataFrame,
                          organization_column: str = 'organization') -> pd.DataFrame:
    """
    Get organization counts from DataFrame.
    
    Args:
        df: DataFrame with organization column
        organization_column: Name of the organization column
        
    Returns:
        DataFrame with organization counts
    """
    if organization_column not in df.columns:
        df = add_organization_column(df)
    
    # Filter out NaN values
    org_counts = df[organization_column].value_counts().reset_index()
    org_counts.columns = ['organization', 'count']
    
    return org_counts

