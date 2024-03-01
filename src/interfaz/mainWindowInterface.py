import os
import PySimpleGUI as sg


sg.theme('BrightColors')
NAME_FONT='ArialRoundedMTBold 40'
DEFAULT_FONT='Arial 15'

password_security = ["Normal","Secure","Super secure!"]

option_layout = [
    [sg.Text('Select level of security'), sg.Combo(password_security, key='-SECURITY OPTIONS-', font=DEFAULT_FONT, size= (17,1))], #level of security of the password
    [sg.Text('Generated password: '), sg.Text('Output:)')],
    [sg.Button("Generate", key='-GENERATE BUTTON-', font=DEFAULT_FONT), sg.Button("Copy", key='-COPY BUTTON-', font=DEFAULT_FONT)]
]


def main_window():
    '''returns the interface of the main window'''
    layout = [
        [sg.Frame('Password generator',option_layout)],
        [sg.Button("Close", key='-FINISH BUTTON-', font=DEFAULT_FONT)]
    ]

    return sg.Window("PASSWORD GENERATOR", layout, size=(400,400), element_justification='center', finalize=True)

main_window()