import dataio
from exceptions import LocationException, InvalidCoordinateException
import slice as s
import pandas as pd
import plotly.graph_objects as go
import gui


def run():
    input_val = ""
    scale = 4.0
    message = ""
    while True:
        try:
            user_input = gui.open_gui(input_val, scale, message)
            if user_input is not None:
                x, y, scale, input_val, last_state = user_input
                geomap = s.slicer(geomap=dataio.load_map(coordX=x, coordY=y), coordX=x, coordY=y, scale_factor=scale)
            else:
                break
        except (LocationException, InvalidCoordinateException) as e:
            message = f"{e}"
        else:
            geodf = pd.DataFrame(data=geomap)
            fig = go.Figure(data=[go.Surface(z=geodf, colorscale="portland")], )
            fig.update_layout(title=f"3D plot of {input_val} with size {scale}", autosize=True,
                              scene=dict(aspectmode="data", xaxis_autorange="reversed"))
            message = "Generating Map..."
            fig.show()


if __name__ == "__main__":
    run()
