import ollama
import json


def suggest_strategies_ollama(ecosystem_state, n=2):
    prompt = f"""
    The ecosystem has the following state:
    Flora: {ecosystem_state['flora']}
    Fauna: {ecosystem_state['fauna']}
    Water Level: {ecosystem_state['water_level']}
    Human Activity: {ecosystem_state['human_activity']}

    Suggest {n} intervention strategies to improve sustainability.
    Each strategy should have:
    - A short name
    - Flora boost (0-50)
    - Fauna boost (0-50)
    - Water boost (0-50)
    - Human activity reduction (0-50)

    Return a JSON array.
    """
    

    try:
        response = ollama.chat(
            model="llama3.2:1b",
            messages=[{"role":"user","content":prompt}]
        )
        strategies = json.loads(response.message["content"])
        return strategies
        #return response["message"]["content"]
    except Exception as e:
        print("Error parsing Ollama response:", e)
        return []

def explain_strategy_ollama(strategy, final_state, steps):
    prompt = f"""
    The ecosystem has the following final state after {steps} steps with the strategy '{strategy['name']}':
    Flora: {final_state['flora']}
    Fauna: {final_state['fauna']}
    Water Level: {final_state['water_level']}
    Human Activity: {final_state['human_activity']}

    Explain why this strategy is recommended or not, and what impact it may have.
    """
    response = ollama.chat(
        model="llama3.2:1b",
        messages=[{"role":"user","content":prompt}]
    )
    return response.message["content"]
