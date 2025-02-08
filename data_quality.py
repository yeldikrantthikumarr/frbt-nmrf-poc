def assess_data_quality(risk_factor_data):
    completeness = len(risk_factor_data.dropna()) / len(risk_factor_data)
    timeliness = (datetime.now() - max(risk_factor_data['date'])).days
    return {
        'completeness': completeness,
        'timeliness': timeliness
    }