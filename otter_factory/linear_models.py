import numpy as np
from sklearn.linear_model import LinearRegression

def calculate_capm_beta(asset_returns, market_returns):
    """
    Calculate CAPM beta coefficient using linear regression (scikit-learn implementation).
    
    Args:
        asset_returns (numpy.ndarray): Array of asset returns.
        market_returns (numpy.ndarray): Array of market returns.
        
    Returns:
        float: CAPM beta coefficient.
    """
    # Reshape the data if needed (for single feature)
    market_returns = market_returns.reshape(-1, 1)
    
    # Create a linear regression model
    model = LinearRegression()
    
    # Fit the model to the data
    model.fit(market_returns, asset_returns)
    
    # Extract beta coefficient from the regression model
    beta_coefficient = model.coef_[0]
    
    return beta_coefficient
