import PySimpleGUI as sg
import pandas as pd
import matplotlib.pyplot as plt

# Very basic form.  Return values as a list
# sg.ChangeLookAndFeel('GreenTan')
data = pd.read_csv("results.csv")


def getSurgeMultiplier(info):
    # print(info)
    surge_loc = data.loc[(data['source'] == info[0]) & (data['destination'] == info[1])
                         & (data['icon'] == info[2]) & (data['hour'] == info[3])
                         & (data['weekday'] == info[4])]
    if len(surge_loc.index) == 0:
        return []
    return surge_loc.values[0][6]

def drawFigure(info):
    surge_loc = data.loc[(data['source'] == info[0]) & (data['destination'] == info[1])
                         & (data['icon'] == info[2]) & (data['hour'] == info[3])]
    weekday = surge_loc['weekday']
    surge = surge_loc['predict']
    plt.plot(weekday, surge)
    plt.show()
form = sg.FlexForm('Surge Multiplier Estimator')  # begin with a blank form

column1 = [[sg.Text('Weekday', background_color='#F7F3EC', justification='center', size=(10, 1))],
           [sg.Spin(values=('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'),
                    initial_value='Monday')],
           ]

layout = [
    [sg.Text('Please enter your Source, Destination, Hour, Weekday, Weather', font='Trebuchet 12 bold',
             border_width=20)],
    [sg.Text("Source", size=(8, 1)), sg.InputCombo(('Back Bay', 'Beacon Hill', 'Boston University', 'Fenway',
                                                    'Financial District', 'Haymarket Square', 'North End',
                                                    'North Station', 'Northeastern University', 'South Station',
                                                    'Theatre District', 'West End'), size=(20, 5))],
    [sg.Text("Destination", size=(8, 1)), sg.InputCombo(('Back Bay', 'Beacon Hill', 'Boston University', 'Fenway',
                                                         'Financial District', 'Haymarket Square', 'North End',
                                                         'North Station', 'Northeastern University', 'South Station',
                                                         'Theatre District', 'West End'), size=(20, 5))],
    [sg.Text("Weather", size=(8, 1)),
     sg.InputCombo(('fog', 'partly-cloudy-day', 'clear-day', 'rain', 'cloudy'), size=(20, 5))],
    [sg.Text('Hour', size=(8, 1)), sg.Slider(range=(0, 23), orientation='h')],
    [sg.Text("Weekday", size=(8, 1)),
     sg.InputCombo(('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'), size=(20, 5))],
    [sg.Text('Results', size=(6, 1), text_color='white', font='Trebuchet 12 bold', background_color='blue')],
    [sg.Text('', size=(8, 3), key='output')],
    [sg.Button('Show'), sg.Button('Exit')],
]

sg.ChangeLookAndFeel('GreenTan')
gui = form.Layout(layout)
while True:  # Event Loop
    button, values = gui.read()
    print(values[0])
    print(button, values)
    if button in (None, 'Exit'):
        break
    if button == 'Show':
        # Update the "output" text element to be the value of "input" element
        surge = getSurgeMultiplier(values)
        if surge==[]:
            surge = 'No Data'
        drawFigure(values)
        gui['output'].update(surge, text_color='red')
        # sg.Popup(button, values)
# button, values = form.Layout(layout).Read()
# print(button, values[0], values[1], values[2])
# sg.Popup(button, values)
