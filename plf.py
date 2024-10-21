import numpy as np
import datetime as dt
from datetime import datetime as dt1
import streamlit as st
import math 
import plotly.graph_objects as go
import pandas as pd

#App build-in

st.set_page_config(
    page_title="LF 2025",
    page_icon="✅",
    layout="wide",
) 

st.title("Analyse d'impact du calcul des salaires LF 2025")

st.markdown('''
Analyse d'impact du calcul des salaires après la LF 2025
- Travail fait par : [Raed Belaidi](https://www.linkedin.com/in/raed-belaidi-8137951b2/)''')

st.write('---')




Nbr = st.number_input("Nombre de salariés",0)
Salaire = st.number_input("Salaire Brut",1.0,format="%f")
Mensualité = st.number_input("Mensualités",12,max_value=12)


st.write("Total des salaires bruts: %d" %(Salaire*Nbr))

cnss = ((Salaire*Mensualité)*0.0968)/Mensualité

Net_social = (Salaire)-cnss

Annuel = Net_social*Mensualité

FP = min(0.1 * Annuel,2000)

Net_FP = Annuel - FP


options = ["Célibataire","Marié","1 enfant" , "2 enfant", "2 enfant", "3 enfant","4 enfant"]


Abattements = st.multiselect(label="Choisir les options qui conviennent",options=options)


abattements = 0 

if "Marié" in Abattements:
    abattements += 300
if "1 enfant" in Abattements:
    abattements += 100
if "2 enfant" in Abattements:
    abattements += 200
if "3 enfant" in Abattements:
    abattements += 300
if "4 enfant" in Abattements:
    abattements += 400

Imposable = Net_FP - abattements


if 0<=Imposable<5000: 
    IRPP = Imposable*0.005
elif 5000<=Imposable<10000: 
    IRPP = (Imposable-5000)*0.1550 + 5000*0.005
elif 10000<=Imposable<20000: 
    IRPP = (Imposable-10000)*0.2550+5000*0.1550+5000*0.005
elif 20000<=Imposable<30000: 
    IRPP = (Imposable-20000)*0.3050+10000*0.2550+5000*0.1550+5000*0.005
elif 30000<=Imposable<40000: 
    IRPP = (Imposable-30000)*0.3350+10000*0.3050+10000*0.2550+5000*0.1550+5000*0.005
elif 40000<=Imposable<50000: 
    IRPP = (Imposable-40000)*0.3650+10000*0.3350+10000*0.3050+10000*0.2550+5000*0.1550+5000*0.005
elif Imposable>50000: 
    IRPP = (Imposable-50000)*0.4050+10000*0.3650+10000*0.3350+10000*0.3050+10000*0.2550+5000*0.1550+5000*0.005


Net_à_payer = (Salaire- cnss- ( IRPP / Mensualité))*Nbr



cnss2 = ((Salaire*Mensualité)*0.0918)/Mensualité

Net_social2 = (Salaire)-cnss2

Annuel2 = Net_social2*Mensualité

FP2 = min(0.1 * Annuel2,2000)

Net_FP2 = Annuel2 - FP2

Imposable2 = Net_FP2 - abattements

if 0<=Imposable2<5000: 
    IRPP2 = Imposable2*0.005
elif 5000<=Imposable2<20000: 
    IRPP2 = (Imposable2-5000)*0.2650 + 5000*0.005
elif 20000<=Imposable2<30000: 
    IRPP2 = (Imposable2-20000)*0.2850+15000*0.2650+5000*0.005
elif 30000<=Imposable2<50000: 
    IRPP2 = (Imposable2-30000)*0.3250+10000*0.2850+15000*0.2650+5000*0.005
elif Imposable2>50000: 
    IRPP2 = (Imposable2-50000)*0.3550+20000*0.3250+10000*0.2850+15000*0.2650+5000*0.005


Net_à_payer2 = (Salaire- cnss2- ( IRPP2 / Mensualité))*Nbr


st.write('---')

kpi1, kpi2 = st.columns(2)
kpi1.metric(
    label=" Net à payer avant LF 2025 en TND ＄",
    value=round(Net_à_payer2,3)
)

kpi2.metric(
    label="Net à payer après LF 2025 en TND ＄",
    value=round(Net_à_payer,3)
)


st.write('---')

st.subheader('Impact (2025-2024) = %d' %(Net_à_payer-Net_à_payer2)) 


st.write('---')

st.subheader("Graphique de l'évolution du salaire net") 

steps = st.number_input("Choix d'increment",10.0)
simulations = st.number_input("Nombre de simulations",1)

final_df_list = []
step_list = []
nap1 = []
nap2 = []

for i in range(simulations):
    steps = steps + Salaire
    cnss_step = ((steps*Mensualité)*0.0968)/Mensualité

    Net_social_step = (steps)-cnss_step

    Annuel_step = Net_social_step*Mensualité

    FP_step = min(0.1 * Annuel_step,2000)

    Net_FP_step = Annuel_step - FP_step


    Imposable_step = Net_FP_step - abattements


    if 0<=Imposable_step<5000: 
        IRPP_step = Imposable_step*0.005
    elif 5000<=Imposable_step<10000: 
        IRPP_step = (Imposable_step-5000)*0.1550 + 5000*0.005
    elif 10000<=Imposable_step<20000: 
        IRPP_step = (Imposable_step-10000)*0.2550+5000*0.1550+5000*0.005
    elif 20000<=Imposable_step<30000: 
        IRPP_step = (Imposable_step-20000)*0.3050+10000*0.2550+5000*0.1550+5000*0.005
    elif 30000<=Imposable_step<40000: 
        IRPP_step = (Imposable_step-30000)*0.3350+10000*0.3050+10000*0.2550+5000*0.1550+5000*0.005
    elif 40000<=Imposable_step<50000: 
        IRPP_step = (Imposable_step-40000)*0.3650+10000*0.3350+10000*0.3050+10000*0.2550+5000*0.1550+5000*0.005
    elif Imposable_step>50000: 
        IRPP_step = (Imposable_step-50000)*0.4050+10000*0.3650+10000*0.3350+10000*0.3050+10000*0.2550+5000*0.1550+5000*0.005


    Net_à_payer_step = (steps- cnss_step- ( IRPP_step / Mensualité))*Nbr

    cnss_step2 = ((steps*Mensualité)*0.0918)/Mensualité

    Net_social_step2 = (steps)-cnss_step2

    Annuel_step2 = Net_social_step2*Mensualité

    FP_step2 = min(0.1 * Annuel_step2,2000)

    Net_FP_step2 = Annuel_step2 - FP_step2

    Imposable_step2 = Net_FP_step2 - abattements

    if 0<=Imposable_step2<5000: 
        IRPP_step2 = Imposable_step2*0.005
    elif 5000<=Imposable_step2<20000: 
        IRPP_step2 = (Imposable_step2-5000)*0.2650 + 5000*0.005
    elif 20000<=Imposable_step2<30000: 
        IRPP_step2 = (Imposable_step2-20000)*0.2850+15000*0.2650+5000*0.005
    elif 30000<=Imposable_step2<50000: 
        IRPP_step2 = (Imposable_step2-30000)*0.3250+10000*0.2850+15000*0.2650+5000*0.005
    elif Imposable_step2>50000: 
        IRPP_step2 = (Imposable_step2-50000)*0.3550+20000*0.3250+10000*0.2850+15000*0.2650+5000*0.005

    Net_à_payer_step2 = (steps- cnss_step2- ( IRPP_step2 / Mensualité))*Nbr
    diff = Net_à_payer_step - Net_à_payer_step2
    
    nap1.append(Net_à_payer_step)
    nap2.append(Net_à_payer_step2)

    final_df_list.append(diff)
    step_list.append(steps)
    
# Create a DataFrame with steps, nap1, nap2, and values
dff = pd.DataFrame({
    "index": [i for i in range(simulations)],
    "Nap1": nap1,
    "Nap2": nap2,
    "step": step_list,
    "values": final_df_list
})


# Create figure
fig = go.Figure()

# Add initial traces for the first step
fig.add_trace(go.Scatter(x=[step_list[0]], y=[nap1[0]], mode='lines+markers', name="Net à payer en 2025"))
fig.add_trace(go.Scatter(x=[step_list[0]], y=[nap2[0]], mode='lines+markers', name="Net à payer avant 2025"))
fig.add_trace(go.Scatter(x=[step_list[0]], y=[final_df_list[0]], mode='lines+markers', name="Impact net du changement LF 2025"))

# Create frames for animation
frames = []
for i in range(1, len(step_list)):
    frames.append(go.Frame(
        data=[
            go.Scatter(x=step_list[:i+1], y=nap1[:i+1], mode='lines+markers', name="Net à payer en 2025"),
            go.Scatter(x=step_list[:i+1], y=nap2[:i+1], mode='lines+markers', name="Net à payer avant 2025"),
            go.Scatter(x=step_list[:i+1], y=final_df_list[:i+1], mode='lines+markers', name="Impact net du changement LF 2025"),
        ],
        # Add dynamic annotations for each frame with slightly larger font size and staggered positioning
        layout=go.Layout(
            annotations=[
                go.layout.Annotation(
                    x=step_list[i], y=nap1[i],
                    text=f'Net 2025: {nap1[i]:.2f}',
                    showarrow=True,
                    arrowhead=2,
                    ax=-30, ay=-40,  # Position slightly to the left and above
                    font=dict(size=12)  # Slightly bigger font size
                ),
                go.layout.Annotation(
                    x=step_list[i], y=nap2[i],
                    text=f'Net 2024: {nap2[i]:.2f}',
                    showarrow=True,
                    arrowhead=2,
                    ax=30, ay=40,  # Position slightly to the right and below
                    font=dict(size=12)  # Slightly bigger font size
                ),
                go.layout.Annotation(
                    x=step_list[i], y=final_df_list[i],
                    text=f'Impact: {final_df_list[i]:.2f}',
                    showarrow=True,
                    arrowhead=2,
                    ax=-30, ay=40,  # Position slightly to the left and below
                    font=dict(size=12)  # Slightly bigger font size
                )
            ]
        )
    ))

# Add frames to figure
fig.frames = frames

# Set up layout with animation settings
fig.update_layout(
    xaxis_title="Salaire brut",
    yaxis_title="Net à payer",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    ),
    updatemenus=[{
        "type": "buttons",
        "buttons": [
            {
                "label": "Play",
                "method": "animate",
                "args": [None, {"frame": {"duration": 500, "redraw": True}, "fromcurrent": True}]
            },
            {
                "label": "Pause",
                "method": "animate",
                "args": [[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate"}]
            }
        ]
    }]
)

# Set initial visible range
fig.update_xaxes(range=[min(step_list), max(step_list)])
fig.update_yaxes(range=[min(min(nap1), min(nap2), min(final_df_list)), max(max(nap1), max(nap2), max(final_df_list))])

# Display the animated plot
st.plotly_chart(fig)