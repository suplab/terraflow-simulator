from ollama import Ollama
import json

ollama_client = Ollama()  # Uses local model by default

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
    response = ollama_client.chat(
        model="llama2",
        messages=[{"role":"user","content":prompt}],
        max_tokens=300
    )

    try:
        strategies = json.loads(response.text)
        return strategies
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
    response = ollama_client.chat(
        model="llama2",
        messages=[{"role":"user","content":prompt}],
        max_tokens=150
    )
    return response.text
