def apply_stress_scenario(risk_factor_data, stress_shock):
    stressed_prices = risk_factor_data['price'] * (1 + stress_shock)
    return stressed_prices

def calculate_capital_impact(stressed_prices, baseline_prices):
    return abs(stressed_prices - baseline_prices).sum()