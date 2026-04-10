def extract_features(X):
    """
    Extract and validate features for the model.

    Parameters:
        X (pd.DataFrame): Input feature dataframe

    Returns:
        pd.DataFrame: Processed features ready for model
    """

    
    required_columns = ['spkts', 'dur', 'sbytes']

    for col in required_columns:
        if col not in X.columns:
            raise ValueError(f"Missing required column: {col}")

    
    X = X[required_columns].fillna(0)

    
    X['bytes_per_packet'] = X['sbytes'] / (X['spkts'] + 1)

    return X