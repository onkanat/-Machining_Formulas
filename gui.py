import PySimpleGUI as sg
import formuler
from formuler import calculate_mass, general_turning_calculations, milling_calculations

def mass(values):
    shape = values['-SHAPE-'][0]
    density = values['-MALZEME-'][0][1]
    geos_str = values['-MALZEME_GEO-']
    geos = [int(geo) for geo in geos_str.split(',')]

    # print(shape, density, geos)
    mass_value = calculate_mass(shape, density, *geos)
    return shape, density, geos, mass_value


kolon1 = [
    [sg.Text("Formüller ve Hesaplamalar")],
    [sg.Text("Malzeme Yoğunlukları.")],
    [sg.Listbox(values=list(formuler.material_density.items()), key='-MALZEME-', enable_events=True, size=(25, 10))],
]

kolon2 = [
    [sg.Text("")],
    [sg.Text("Malzeme Şekilleri")],
    [sg.Listbox(values=formuler.shape, key='-SHAPE-',enable_events=True, size=(25, 10))],
]

kolon3 = [        
    [sg.Text("Hesaplanacak Değer.")],
    [sg.Listbox(values=formuler.definitions,key='-CALC_METOD-',enable_events=True, size=(25, 11))]
]

kolon4 = [
    [sg.Text("Hesaplama Verisini Gir.")],
    [sg.Input("", key='-CALC_DATA-',size=(25,1))],
    [sg.Output(size=(25,10),key='-CUT_CALC_ANS-')]
]

layoutTab_1 = [
    [sg.T("")],
    [sg.Col(kolon1, p=0), sg.Col(kolon2, p=0)],
    [sg.Input("Malzeme Ölçülerini Gir.",key='-MALZEME_GEO-', size=(54,1))],
    [sg.Output(size=(54, 10), key='-MASS_CALC_ANS-')],
    [sg.Button("AĞIRLIK HESAPLA")]
]

layoutTab_2 = [
    [sg.T("")],
    [sg.Col(kolon3, p=0), sg.Col(kolon4, p=0)],
    [sg.Button("HESAPLA")]
]


layout = [[sg.TabGroup([[sg.Tab('Ağırlık Hesaplama', layoutTab_1),
                         sg.Tab('REPL & Kesme Verisi Hesaplama', layoutTab_2)]])],
                         [sg.Button("ÇIKIŞ")]]          

# Create the window
window = sg.Window("Mühendislik Hesaplamaları ve Verimlilik.", layout, return_keyboard_events=True, margins=(25, 25))

# Create an event loop
while True:
    event, values = window.read() # type: ignore
    # End program if user closes window or
    # presses the OK button
    if event == "AĞIRLIK HESAPLA":
        
        window['-MASS_CALC_ANS-'].print(mass(values))
    elif event == "HESAPLA":
        window['-CUT_CALC_ANS-'].print(values)
    elif event == "ÇIKIŞ" or event == sg.WIN_CLOSED:
        break

window.close()