
def sustainability_score(history):
    final = history.iloc[-1]
    score = (final['flora'] + final['fauna'] + final['water_level'])/3 - final['human_activity']*0.5
    return score
