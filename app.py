import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [-12.04, -77.0428], columns=["lat", "lon"]
)

mapstyle = st.sidebar.selectbox(
    "Choose Map Style:",
    options=["light"], #"dark", "Satellite", "road"],
    format_func=str.capitalize,
)

st.pydeck_chart(
    pdk.Deck(
        map_style='mapbox://styles/mapbox/satellite-v9', #f"{mapstyle}",  # 'light', 'dark', 'mapbox://styles/mapbox/satellite-streets-v12', 'road'
        layers=[layer1,layer2], # The following layer would be on top of the previous layers
        initial_view_state=pdk.ViewState(
            latitude=-12.04,
            longitude=-77.0428,
            zoom=15,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=df,
                get_position="[lon, lat]",
                get_color="[200, 30, 0, 160]",
                get_radius=20,
            ),
        ],
    )
)
