from playsound import playsound
import os

print('Python Music player')

list = os.listdir('C:\project')
play = True

print('Your collection:', str(list))


while play:
    
    req = input('Wath you want to listen? ')

    if req == 'Landscape':
        
        playsound('Ryokuoushoku_Shakai_-_Landscape_(musmore.com).mp3')
        
    elif req == 'Shinunoga E-Wa' or req == '死ぬのがい‐わ':
        
        playsound('Fujii_Kaze_-_Shinunoga_E-Wa_(musmore.com).mp3')
    
    elif req != list:
        
        print("You don't have this in your player!")   