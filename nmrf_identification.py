# nmrf_identification.py
import pandas as pd
from datetime import datetime

def is_modellable(risk_factor_data, min_observations=24, max_age_days=30):
    # Check data completeness
    if len(risk_factor_data.dropna()) < min_observations:
        return False
    # Check data timeliness
    latest_date = pd.to_datetime(risk_factor_data['date'].max())
    if (datetime.now() - latest_date).days > max_age_days:
        return False
    return True

# Example usage (you can add test cases here)
if __name__ == "__main__":
    synthetic_data = pd.read_csv("../data/synthetic_fx.csv")
    print(f"Is modellable? {is_modellable(synthetic_data)}")