def linear_scaler(min_, max_, lower, upper):
    return lambda x: (((x - min_) * (upper - lower)) / (max_ - min_)) + lower