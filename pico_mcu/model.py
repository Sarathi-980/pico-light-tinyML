def predict_light(raw_adc):
    if raw_adc <= 14250:
        return "DARK"
    elif raw_adc <= 45500:
        return "NORMAL"
    else:
        return "BRIGHT"