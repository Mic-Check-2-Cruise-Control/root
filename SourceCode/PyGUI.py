import sounddevice as sd
from scipy.io.wavfile import write
from scipy.io.wavfile import read
import soundfile as sf

import argparse
import queue
import sys

from tkinter import *
from builtins import *
from tkinter.ttk import Combobox

import tkinter as tk
import PySimpleGUI as sg

import matplotlib.pyplot as plt

import os


# Get current Directory
directory = os.getcwd()

# Output wav file name
output = "output.wav"

# File to be played
filename = 'output.wav'

# Recording Duration
dur = 10


# Generate desired elements of the window
sg.theme('DarkAmber')
layout = [[sg.Text("Audio Recording Application")],
          [sg.Text(" ")],
          [sg.Button("Play"), sg.InputText(filename), sg.FileBrowse()],
          [sg.Text(" ")],
          [sg.Button("Record")],
          [sg.Text(" ")],
          [sg.Text("Recording Duration"), sg.InputText(dur)],
          [sg.Text("File Name + \".wav\""), sg.InputText(output)],
          [sg.Text("Save to"), sg.InputText(directory), sg.FolderBrowse()]]

# Create the window
window = sg.Window("Mic Check 2", layout)

# Create an event loop
while True:
    event, values = window.read()

    # print(values[0],values[1],values[2],values[3])

    # End program if user closes window or
    # presses the OK button
    if event == "Record":
        # Begin Recording

        fs = 44100
        second = int(values[1])
        record_voice = sd.rec(int(second * fs), samplerate=fs, channels=2)
        # sg.PopupTimed("RECORDING", auto_close_duration=second)

        # Setup title

        plt.title("Your WAV File")
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        i = 0
        duration = second * 3

        # loop to get voice data in real time
        while i < duration:
            pass
            plt.plot(record_voice)
            plt.pause(0.05)
            i = i + 1

        # Display plot of amplitudes
        plt.show(block=False)
        sd.wait()
        plt.close('all')

        # Set desired directory by user
        directory = values[3] + '/'
        output = directory + values[2]
        write(output, fs, record_voice)

    if event == "Play":
        # Play Recording
        filename = values[0]
        data, fs = sf.read(filename, dtype='float32')

        # This code will create a checkbox to ask the user if they want to make a graph

        # Import file with frequency sampling
        sd.play(data, fs)
        # sg.PopupTimed("PLAYING", auto_close_duration=10)

        # No wait so user can close program if need be

        # Matplot

        rate, graphData = read(filename)
        # Setup title
        plt.title("Your WAV File")

        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.plot(graphData)
        plt.show(block=False)
        # next two lines are untested
        # sd.wait()
        # plt.close('all')

    if event == sg.WIN_CLOSED:
        break

window.close()
