def solution(S : str, K : int):

    # Create a 1:1 mapping between each strings and an integer
    days_mapping = {
        "Mon": 0,
        "Tue": 1,
        "Wed": 2,
        "Thu": 3,
        "Fri": 4,
        "Sat": 5,
        "Sun": 6,
    }

    days_abbr = [ "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    
    try:
        idx = (days_mapping[S] + K) % 7
        return days_abbr[idx]
    except :
        raise KeyError("The input is not a valid day!")