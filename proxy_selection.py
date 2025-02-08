def select_proxy(nmrf_data, candidate_proxies):
    correlations = {}
    for proxy in candidate_proxies:
        correlation = nmrf_data['price'].corr(proxy['price'])
        correlations[proxy['name']] = correlation
    return max(correlations, key=correlations.get)