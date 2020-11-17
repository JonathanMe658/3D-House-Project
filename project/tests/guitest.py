import PySimpleGUI as sg


output = ""
scale = ""
message = ""
layout = [
    [sg.Text("Coordinates: \t"), sg.In(size=(25, 1), enable_events=True, key="-COORDINATES-", default_text=output)],
    [sg.Text("Scale: \t\t"), sg.In(size=(25, 1), enable_events=True, key="-SCALE-", default_text=scale)],
    [sg.Text(message)],
    [sg.Button("Enter"), sg.Button("Exit")]
]

window = sg.Window("3D Map Viewer", layout)
while True:
    event, values = window.read()
    if event ==  "OK" or event == sg.WIN_CLOSED:
        break
    if event == "-COORDINATES-":
        output = values["-COORDINATES-"]
    if event == "-SCALE-":
        output = values["-COORDINATES-"]
window.close()
print(output)