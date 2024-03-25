import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import cv2
from easygui import *
import os
from PIL import Image, ImageTk
from itertools import count
import tkinter as tk
import string

image   = "signlanguage.jpg"
msg="Silent Symphony"
choices = ["ISL","ASL","Coming Soon"]
reply   = buttonbox(msg,image=image,choices=choices)
if reply==choices[0]:
    os.system("python isl.py")
elif reply==choices[1]:
    os.system("python asl.py")

