import PySimpleGUI as sg
import coordinates as co

def open_gui(input_val="", scale=8.0, message=""):
    layout = [
        [sg.Text("Coordinates: \t"), sg.In(size=(25, 1), enable_events=True, key="-COORDINATES-", default_text=input_val)],
        [sg.Text("Scale: \t\t"), sg.In(size=(25, 1), enable_events=True, key="-SCALE-", default_text=scale)],
        [sg.Text(message)],
        [sg.Button("Enter"), sg.Button("Exit")]
    ]
    last_state = "Open"
    window = sg.Window("3D Map Viewer", layout)
    while True:
        event, values = window.read()
        if event == "Enter" or event == "Exit":
            last_state = event
            break
        if event == sg.WIN_CLOSED:
            break
        if event == "-COORDINATES-":
            input_val = values["-COORDINATES-"]
        if event == "-SCALE-":
            scale = values["-SCALE-"]
    window.close()
    x, y = co.convert_coords_to_decimals(input_val.split())
    return [x, y, scale, last_state]

print(open_gui())