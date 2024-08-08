def future_value (present_value, annual_rate, years) :
    future_val = present_value * (1.0 + (0.01 * annual_rate)) ** years
    return future_val