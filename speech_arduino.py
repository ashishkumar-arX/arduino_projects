import serial.tools.list_ports,win32gui,speech_recognition,time,win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
program_title = win32gui.GetWindowText(win32gui.GetForegroundWindow())

def is_program_in_focus(program_title):
    current_window_title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    return current_window_title == program_title

#----------------------------------------------------------------------------------------#
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

val = input("Select Port: COM")

for x in range(0,len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portVar = "com" + str(val)
        print(portVar)

serialInst.bautrate = 9600
serialInst.port = portVar
serialInst.open()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Capturing audio...")
        r.energy_threshold = 2500
        r.pause_threshold = 0.8
        audio = r.listen(source)
    print("Audio captured!")
    try:
        print("analysing")
        action = r.recognize_google(audio)
        print(f"You said: {action}")
        return action           
    except speech_recognition.UnknownValueError:
        print("Sorry, I couldn't understand.")
    except speech_recognition.RequestError as e:
        print("Sorry, an error occurred while requesting results; {0}".format(e))

def smithInteraction():
    action = takeCommand()
    
    if action == "turn on":
        command = "ON"
        serialInst.write(command.encode('utf-8'))

    elif action == "turn off":
        command = "OFF"
        serialInst.write(command.encode('utf-8'))

    elif action == "turn blink":
        command = "blink"
        serialInst.write(command.encode('utf-8'))

    elif action == "buzzer on":
        command = "buzzer on"
        serialInst.write(command.encode('utf-8'))
    
    elif action == "buzzer of":
        command = "buzzer off"
        serialInst.write(command.encode('utf-8'))

    elif action == "exit":
        exit()


while True:
    if is_program_in_focus(program_title) :
        smithInteraction()
        time.sleep(4)