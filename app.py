import streamlit as st
from simulation.ecosystem import Ecosystem
from simulation.interventions import predefined_interventions, suggest_interventions
from utils.visualization import plotly_compare_strategies
from utils.score import sustainability_score
from utils.ollama_agent import suggest_strategies_ollama, explain_strategy_ollama

st.title("🌱 Localized Ecosystem Simulation (Offline, Ollama)")

# --- User Inputs ---
st.sidebar.header("Ecosystem Parameters")
flora = st.sidebar.slider("Flora",0,100,50)
fauna = st.sidebar.slider("Fauna",0,100,50)
water_level = st.sidebar.slider("Water Level",0,100,50)
human_activity = st.sidebar.slider("Human Activity",0,100,50)
steps = st.sidebar.slider("Simulation Steps",1,30,10)

# --- Strategies ---
interventions = predefined_interventions()
ecosystem_state = {'flora':flora,'fauna':fauna,'water_level':water_level,'human_activity':human_activity}
gpt_strategies = suggest_strategies_ollama(ecosystem_state,n=2)
if gpt_strategies:
    interventions.extend(gpt_strategies)

# --- Real-time tweak sliders ---
st.sidebar.header("Tweak Interventions")
for i, intervention in enumerate(interventions):
    st.sidebar.subheader(intervention['name'])
    intervention['flora_boost'] = st.sidebar.slider(f"Flora Boost {intervention['name']}",0,50,intervention.get('flora_boost',0))
    intervention['fauna_boost'] = st.sidebar.slider(f"Fauna Boost {intervention['name']}",0,50,intervention.get('fauna_boost',0))
    intervention['water_boost'] = st.sidebar.slider(f"Water Boost {intervention['name']}",0,50,intervention.get('water_boost',0))
    intervention['human_activity_reduction'] = st.sidebar.slider(f"Human Activity Reduction {intervention['name']}",0,50,intervention.get('human_activity_reduction',0))

# --- Simulate All Strategies ---
strategy_histories = {}
for intervention in interventions:
    eco = Ecosystem(flora, fauna, water_level, human_activity)
    history = eco.simulate(steps, interventions=[intervention]*steps)
    strategy_histories[intervention['name']] = history

# --- Interactive Visualization ---
st.subheader("Simulation Results: Strategy Comparison")
fig = plotly_compare_strategies(strategy_histories)
st.plotly_chart(fig, use_container_width=True)

# --- Sustainability Scores & Best Strategy ---
scores = {name:sustainability_score(history) for name,history in strategy_histories.items()}
best_strategy = max(scores, key=scores.get)
st.subheader("🏆 Best Strategy Recommendation")
st.markdown(f"**{best_strategy}** with score {scores[best_strategy]:.2f}")

# --- Ollama Explanations ---
st.subheader("Strategy Explanations (Ollama LLM)")
for intervention in interventions:
    final_state = strategy_histories[intervention['name']].iloc[-1]
    explanation = explain_strategy_ollama(intervention, final_state, steps)
    st.markdown(f"**{intervention['name']}**: {explanation}")
