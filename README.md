# 🌱 Localized Ecosystem Simulation

**Objective**: Autonomous agent that simulates and predicts environmental changes in a micro-ecosystem (urban park, river, or lake) based on user interventions.

## MVP Features:

- Input: ecosystem parameters (flora, fauna, water levels, human activity).
- Simulation of future scenarios (pollution, biodiversity change).
- Suggest optimal interventions for sustainability.
- Visual output of predicted changes over time.

## Agentic Workflow:

1. User inputs ecosystem parameters.
2. Agent runs simulation (rule-based or lightweight ML model).
3. Agent evaluates multiple intervention strategies autonomously.
4. Agent produces a visualization of predicted outcomes and recommendations.

## Tech Stack:

Models: Rule-based + reinforcement learning (lightweight Python sim).

LLM: ollama2 for interpreting simulation outputs and generating recommendations.

Visualization: Matplotlib / Plotly for scenario charts.

Frontend: Streamlit for interactive dashboards.

## Roadmap:

Create data input form for ecosystem parameters.

Implement simulation engine (e.g., simplified population dynamics or pollution spread).

Integrate agent to propose interventions.

Visualize outcomes for different intervention strategies.

Bonus: Allow user to “tweak” interventions in real-time.

## Project Structure

```
localized_ecosystem_sim/
├─ app.py                  # Streamlit frontend + main agent workflow
├─ simulation/
│   ├─ __init__.py
│   ├─ ecosystem.py        # Core simulation engine
│   └─ interventions.py    # Predefined interventions
├─ utils/
│   ├─ __init__.py
│   ├─ visualization.py    # Interactive Plotly charts
│   ├─ score.py            # Sustainability scoring
│   └─ ollama_agent.py     # Ollama LLM strategies & explanations
├─ requirements.txt
└─ README.md
```

## Setup

1. Clone repo and create virtualenv:
```bash
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows
pip install -r requirements.txt
```

2. Install and run Ollama:
```bash
ollama run llama2
```

3. Run the app:
```bash
streamlit run app.py
```

4. Adjust ecosystem parameters and intervention strategies in real-time.

