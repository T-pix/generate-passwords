
import random
import PySimpleGUI as sg
import os
from playsound import playsound

class pass_gen:
    def __init__(self): 

        sg.theme('black')
        
        playsound("audio.mp3",block=False)

        layout = [
            [sg.Text('Site',size=(10,1)),sg.Input(key='site',size=(20,1))],
            [sg.Text('User',size=(10,1)),sg.Input(key='user',size=(20,1))],
            [sg.Text('Number of Chars'),sg.Combo(values=list(range(50)),key='total_chars',
                                                 default_value=1,size=(3,1))],
            [sg.Output(size=(32,5))],
            [sg.Button('Generate Password')]
        ]

        self.window = sg.Window('Password Generator',layout)

    def start(self):
        while True:
            event,values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Generate Password':
                new_passw = self.generate_passw(values)
                print(new_passw)
                self.save_passw(new_passw,values)

    def generate_passw(self,values):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*'
        chars = random.choices(char_list,k=int(values['total_chars']))
        new_pass = ''.join(chars)
        return new_pass

    def save_passw(self,new_passw,values):
        with open('passwords.txt','a',newline='') as file:
            file.write(f'site: {values['site']}, user: {values['user']}, new password: {new_passw}')

        print('file saved')

gen = pass_gen()
gen.start()
