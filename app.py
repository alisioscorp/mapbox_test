import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"]
)

mapstyle = st.sidebar.selectbox(
    "Choose Map Style:",
    options=["light", "dark", "satellite-v9", "road"],
    format_func=str.capitalize,
)

st.pydeck_chart(
    pdk.Deck(
        map_style=f"{mapstyle}",  # 'light', 'dark', 'satellite-v9', 'road'
        map_provider=mapbox,
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=df,
                get_position="[lon, lat]",
                get_color="[200, 30, 0, 160]",
                get_radius=200,
            ),
        ],
    )
)
