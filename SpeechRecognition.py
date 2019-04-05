import webbrowser
import urllib.request
import urllib.request
import re
import numpy as np
#to search on Google
def searchOnGoogle(d):
    print("check3")
    print("Opening google.....")               
    url = "https://www.google.com/search?q={}".format(d)
    webbrowser.open_new_tab(url)

#ends 
#to play on youtube
def playYoutube(term):
    print("Opening youtube....")
    query_string = urllib.parse.urlencode({"search_query" : term})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    url = "http://www.youtube.com/watch?v={}".format(search_results[0])
    webbrowser.open_new_tab(url)
#ends

#to switch window
def switchTo(term):
    print("Switching to {}.....".format(term))
    if __name__ == "__main__":
        results = []
        top_windows = []
        win32gui.EnumWindows(windowEnumerationHandler, top_windows)
        for i in top_windows:
            if term in i[1].lower():
                win32gui.ShowWindow(i[0],5)
                win32gui.SetForegroundWindow(i[0])
                break
#ends

#to perform commands according to the text
def textAction(textF):
    textF = textF.lower().split()
    i=0
    j=0
    wordCount = len(textF)
    while i<wordCount:
        print(textF[i])
        if textF[i] == "search" or textF[i]=="check":
            i=i+1
            if(textF[i]=="for"):
                i=i+1
            forming = []
            while i<wordCount and textF[i]!="amigo":
                forming.append(textF[i])
                forming.append(" ")
                i=i+1
            searchOnGoogle(''.join(forming)) #GOOGLE SEARCH
        elif textF[i]=="play":
            i=i+1
            forming1 = []
            while i<wordCount and textF[i]!="amigo":
                forming1.append(textF[i])
                forming1.append(" ")
                i=i+1
            playYoutube(''.join(forming1)) #PLAY
        elif textF[i] =="switch":
            i=i+1
            if(textF[i]=="to"):
                i=i+1
            forming2 =[]
            while i<wordCount and textF[i]!="amigo":
                forming2.append(textF[i])
                forming2.append(" ")
                i=i+1
            switchTo(''.join(forming2)) #SWITCH
        i=i+1
#importing speech recoginition
import speech_recognition as sr
r = sr.Recognizer()
#extracting the audio from the text and passing to textAction
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source,duration=1)
    print("Say something...")
    audio = r.listen(source,phrase_time_limit=5)
    # try:
    text = r.recognize_google(audio,language='en-IN')
    print("You said: {}".format(text))
    textAction(text)
    # except:
    #     print("Sorry could not recognize your voice")
#ends passing text to textAction

#to open the window asked by the user
import win32gui
def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
#ends



    
#ends