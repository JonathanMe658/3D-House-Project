import PySimpleGUI as sg
import coordinates as co


def open_gui(input_val: str = "", scale: float = 8.0, message: str = "") -> list:
    layout = [
        [sg.Text("Coordinates (DMS): \t"), sg.In(size=(25, 1), enable_events=True, key="-COORDINATES-", default_text=input_val)],
        [sg.Text("Scale: \t\t\t"), sg.In(size=(25, 1), enable_events=True, key="-SCALE-", default_text=scale)],
        [sg.Text(message)],
        [sg.Button("Enter"), sg.Button("Exit")]
    ]
    window = sg.Window("3D Map Viewer", layout)
    while True:
        event, values = window.read()
        if event == "Enter" or event == "Exit":
            last_state = event
            break
        if event == sg.WIN_CLOSED:
            last_state = "Exit"
            break
        if event == "-COORDINATES-":
            input_val = values["-COORDINATES-"]
        if event == "-SCALE-":
            scale_input = values["-SCALE-"]
            if co.is_decimal(scale_input):
                scale = float(scale_input)
    window.close()
    if last_state == "Exit":
        return None
    x, y = co.convert_coords_to_decimals(input_val.split())
    return [x, y, scale, input_val, last_state]
