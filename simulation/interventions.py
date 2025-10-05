
def predefined_interventions():
    return [
        {"name": "Flora Boost", "flora_boost": 20, "fauna_boost": 0, "water_boost":0, "human_activity_reduction":0},
        {"name": "Fauna Boost", "flora_boost":0, "fauna_boost":20, "water_boost":0, "human_activity_reduction":0},
        {"name": "Water Boost", "flora_boost":0, "fauna_boost":0, "water_boost":20, "human_activity_reduction":0},
        {"name": "Reduce Human Activity", "flora_boost":0, "fauna_boost":0, "water_boost":0, "human_activity_reduction":20},
        {"name": "Combined Boost", "flora_boost":10, "fauna_boost":10, "water_boost":10, "human_activity_reduction":10}
    ]

def suggest_interventions(ecosystem):
    suggestions = []
    if ecosystem.flora < 40:
        suggestions.append("Plant more trees / flora")
    if ecosystem.fauna < 40:
        suggestions.append("Introduce species carefully")
    if ecosystem.water_level < 40:
        suggestions.append("Reduce pollution / increase water sources")
    if ecosystem.human_activity > 60:
        suggestions.append("Implement park regulations to reduce human activity")
    return suggestions
