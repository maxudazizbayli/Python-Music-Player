from playsound import playsound
import os

print('Welcome to PMP!!')

list = os.listdir('C:\project')
play = True

print('Your collection:', str(list))


while play:
    
    req = input('Wath you want to listen?(example.mp3) ')
    
    playsound(req)
    
    if req != list:
       
        print("You don't have this in your player!")   
