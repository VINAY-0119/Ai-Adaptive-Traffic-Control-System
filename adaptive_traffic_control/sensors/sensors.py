def get_queue_lengths(lanes):
    return {k: v.length() for k, v in lanes.items()}
