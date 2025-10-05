import plotly.graph_objects as go

def plotly_compare_strategies(histories):
    fig = go.Figure()
    for name, history in histories.items():
        fig.add_trace(go.Scatter(
            x=history['step'], y=history['flora'],
            mode='lines+markers', name=f'{name} - Flora'
        ))
        fig.add_trace(go.Scatter(
            x=history['step'], y=history['fauna'],
            mode='lines+markers', name=f'{name} - Fauna', line=dict(dash='dash')
        ))
        fig.add_trace(go.Scatter(
            x=history['step'], y=history['water_level'],
            mode='lines+markers', name=f'{name} - Water', line=dict(dash='dot')
        ))
        fig.add_trace(go.Scatter(
            x=history['step'], y=history['human_activity'],
            mode='lines+markers', name=f'{name} - Human Activity', line=dict(dash='longdash')
        ))
    fig.update_layout(
        title="Ecosystem Simulation: Multiple Strategies",
        xaxis_title="Time Step",
        yaxis_title="Value",
        legend_title="Metrics",
        hovermode="x unified"
    )
    return fig
