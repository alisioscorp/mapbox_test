import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [-12.04, -76.94], columns=["lat", "lon"]
)

mapstyle = st.sidebar.selectbox(
    "Choose Map Style:",
    options=["light"], #"dark", "Satellite", "road"],
    format_func=str.capitalize,
)
# # Create a map layer with the given coordinates
# layer1 = pdk.Layer(type = 'ScatterplotLayer', # layer type
#                   data=df_bos, # data source
#                   get_position='[lon, lat]', # coordinates
#                   get_radius=500, # scatter radius
#                   get_color=[0,0,255],   # scatter color
#                   pickable=True # work with tooltip
#                   )

# # Can create multiple layers in a map
# # For more layer information
# # https://deckgl.readthedocs.io/en/latest/layer.html
# # Line layer https://pydeck.gl/gallery/line_layer.html
# layer2 = pdk.Layer('ScatterplotLayer',
#                   data=df_bos,
#                   get_position='[lon, lat]',
#                   get_radius=100,
#                   get_color=[255,0,255],
#                   pickable=True
#                   )

# >>> layer = pydeck.Layer(
# >>>     'HexagonLayer',
# >>>     UK_ACCIDENTS_DATA,
# >>>     get_position=['lng', 'lat'],
# >>>     auto_highlight=True,
# >>>     elevation_scale=50,
# >>>     pickable=True,
# >>>     elevation_range=[0, 3000],
# >>>     extruded=True,
# >>>     coverage=1)

st.pydeck_chart(
    pdk.Deck(
        map_style='mapbox://styles/mapbox/satellite-v9', #f"{mapstyle}",  # 'light', 'dark', 'mapbox://styles/mapbox/satellite-streets-v12', 'road'
        #layers=[layer1,layer2], # The following layer would be on top of the previous layers
        initial_view_state=pdk.ViewState(
            latitude=-12.04,
            longitude=-76.94,
            zoom=10,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'HexagonLayer', #"ScatterplotLayer",
                data=df,
                opacity=0.8,
                get_position="[lon, lat]",
                get_color="[200, 30, 0, 160]",
                elevation_scale=10, 
                #get_radius=20,
                #elevation_range=[0, 3000],
                radius=150,
                #elevation_scale=4,
                #elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
                coverage=1
            ),
        ],
    )
)
