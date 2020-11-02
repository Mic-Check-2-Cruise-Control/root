import sounddevice as sd
from scipy.io.wavfile import write
import soundfile as sf

import argparse
import queue
import sys

from tkinter import *
from builtins import * 
from tkinter.ttk import Combobox 

import tkinter as tk
import PySimpleGUI as sg



sg.theme('DarkAmber')
layout = [[sg.Text("Audio Recording Application")], 
                            [sg.Text(" ")],
                            [sg.Button("Play"), sg.InputText("output.wav"), sg.FolderBrowse()],
                            [sg.Text(" ")],
                            [sg.Button("Record")],
                            [sg.Text(" ")],
                            [sg.Text("Recording Duration"), sg.InputText()],
                            [sg.Text("File Name + \".wav\""), sg.InputText()],
                            [sg.Text("Save to"), sg.InputText(), sg.FolderBrowse()]]

# Create the window
window = sg.Window("Mic Check 2", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Record" :
        # Begin Recording 
        fs=44100
        second=10
        record_voice=sd.rec(int(second * fs),samplerate=fs,channels=2)
        sg.PopupTimed("RECORDING",auto_close_duration = 10)
        sd.wait()
        write("output.wav",fs,record_voice)

    if event == "Play" :
        # Play Recording 
        filename = 'output.wav'
        data, fs = sf.read(filename,dtype = 'float32')
        # Import file with frequency sampling
        sd.play(data,fs)
        sg.PopupTimed("PLAYING",auto_close_duration = 10)
        status = sd.wait()
        # wait for end of recording 
    
    if event == sg.WIN_CLOSED :
        break

window.close()

