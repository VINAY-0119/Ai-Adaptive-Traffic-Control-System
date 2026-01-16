def average_delay(vehicles):
    if not vehicles:
        return 0
    return sum(v.waiting_time for v in vehicles) / len(vehicles)
