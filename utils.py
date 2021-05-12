def linear_scaler(domain, range):
    return lambda x: (x-domain[0])/(domain[1]-domain[0])*(range[1]-range[0]) + range[0]

