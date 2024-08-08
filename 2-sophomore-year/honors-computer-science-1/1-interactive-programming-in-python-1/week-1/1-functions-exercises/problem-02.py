def total_seconds (hours, minutes, seconds):
    hours_to_seconds = hours * 3600
    minutes_to_seconds = minutes * 60
    total_time = hours_to_seconds + minutes_to_seconds + seconds
    return total_time