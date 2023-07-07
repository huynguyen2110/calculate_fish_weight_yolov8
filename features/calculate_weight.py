def calculate_weight(fish):
    if fish[0] == "carp":
        return 1
    elif fish[0] == "catfish":
        return 10
    elif fish[0] == "tilapia":
        return 100
    elif fish[0] == "perch":
        return 1000
    else:
        return "unknown"

