import dataio
from dataio import LocationException
import coordinates as co
import slice as s
import pandas as pd
import plotly.graph_objects as go

def run():
    while True:
        pass

#remove when gui is up and running

y = input("Coordinate N/Z: ")
x = input("Coordinate E/W: ")
scale_factor = float(input("scale factor: "))


if not co.is_decimal(y):
    y0 = co.convert_coords_to_decimal(y)
else:
    y0 = float(y)

if not co.is_decimal(x):
    x0 = co.convert_coords_to_decimal(x)
else:
    x0 = float(x)


geomap = s.slice(geomap=dataio.load_map(coordX=x0, coordY=y0), coordX=x0, coordY=y0, scale_factor=scale_factor)
#, index=[f"Y{i}" for i in range(geomap.shape[0])], columns=[f"X{i}" for i in range(geomap.shape[1])]
df = pd.DataFrame(data=geomap)
df.head()

# plotting

'''
fig = plt.figure()
ax = fig.gca(projection="3d")

X = np.arange(0, df.shape[0])
Y = np.arange(0, df.shape[1])
X, Y = np.meshgrid(X, Y)
Z = df

surf = ax.plot_surface(X, Y, Z, cmap="ocean", linewidth=0, antialiased=True)
plt.show()

'''
fig = go.Figure(data=[go.Surface(z=df.values)])
fig.update_layout(title="Test", autosize=True, scene=dict(aspectmode="manual", aspectratio=dict(x=10, y=10, z=2)))
fig.show()
# 50°45'01"N
# 3°54'11"E

