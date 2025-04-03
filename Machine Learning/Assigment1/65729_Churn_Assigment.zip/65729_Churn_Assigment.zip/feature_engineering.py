# feature_engineering.py
import pandas as pd

def apply_feature_engineering(X):
    """
    Perform feature engineering on the telecom dataset.
    
    This function:
      - Computes aggregated features: TotalMinutes, TotalCalls, MonthlyCharges.
      - Converts binary variables ('Churn', 'International plan', 'Voice mail plan') into 0/1.
      - Calculates relative percentages for minutes, charges, and calls.
      - Drops the original detailed columns.
    
    Parameters:
      X (pd.DataFrame): Original DataFrame with raw features.
    
    Returns:
      pd.DataFrame: DataFrame with engineered features.
    """
    # Compute aggregated features
    X['TotalMinutes'] = (X['Total day minutes'] + 
                          X['Total eve minutes'] + 
                          X['Total night minutes'] + 
                          X['Total intl minutes'])
    
    X['TotalCalls'] = (X['Total day calls'] + 
                        X['Total eve calls'] + 
                        X['Total night calls'] + 
                        X['Total intl calls'])
    
    X['MonthlyCharges'] = (X['Total day charge'] + 
                            X['Total eve charge'] + 
                            X['Total night charge'] + 
                            X['Total intl charge'])
    
    # Convert binary variables only if the column exists
    if 'Churn' in X.columns:
        X['Churn'] = X['Churn'].map({False: 0, True: 1})
    X['International plan'] = X['International plan'].map({'No': 0, 'Yes': 1})
    X['Voice mail plan'] = X['Voice mail plan'].map({'No': 0, 'Yes': 1})
    
    # Calculate relative percentages for minutes
    X['DayMinutesPct'] = (X['Total day minutes'] / X['TotalMinutes']) * 100
    X['EveMinutesPct'] = (X['Total eve minutes'] / X['TotalMinutes']) * 100
    X['NightMinutesPct'] = (X['Total night minutes'] / X['TotalMinutes']) * 100
    X['IntlMinutesPct'] = (X['Total intl minutes'] / X['TotalMinutes']) * 100
    
    # Calculate relative percentages for charges
    X['DayChargesPct'] = (X['Total day charge'] / X['MonthlyCharges']) * 100
    X['EveChargesPct'] = (X['Total eve charge'] / X['MonthlyCharges']) * 100
    X['NightChargesPct'] = (X['Total night charge'] / X['MonthlyCharges']) * 100
    X['IntlChargesPct'] = (X['Total intl charge'] / X['MonthlyCharges']) * 100
    
    # Calculate relative percentages for calls
    X['DayCallsPct'] = (X['Total day calls'] / X['TotalCalls']) * 100
    X['EveCallsPct'] = (X['Total eve calls'] / X['TotalCalls']) * 100
    X['NightCallsPct'] = (X['Total night calls'] / X['TotalCalls']) * 100
    X['IntlCallsPct'] = (X['Total intl calls'] / X['TotalCalls']) * 100
    
    # Drop the original detailed columns
    cols_to_drop = [
        'Total day minutes', 'Total eve minutes', 'Total night minutes', 'Total intl minutes',
        'Total day calls', 'Total eve calls', 'Total night calls', 'Total intl calls',
        'Total day charge', 'Total eve charge', 'Total night charge', 'Total intl charge'
    ]
    X = X.drop(columns=cols_to_drop, errors='ignore')
    
    return X
