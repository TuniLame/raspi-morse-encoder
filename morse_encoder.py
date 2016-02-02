


import sys
import pygame
import time
import wave

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }

ONE_UNIT = 0.5
THREE_UNITS = 3 * ONE_UNIT
SEVEN_UNITS = 6 * ONE_UNIT
SAMPLE_FREQUENCY = 10000
#PATH = '/morse_sound_files/'

def verify(string):
	keys = CODE.keys()
	for char in string:
		if char.upper() not in keys and char != ' ':
			sys.exit('Error the charcter ' + char + ' cannot be translated to Morse Code')

def main():


    PATH = sys.argv[1]+ '/morse_sound_files/'
    print PATH
    # Start
    pygame.mixer.init(SAMPLE_FREQUENCY) # Define sound speed. Original is 8000
    pygame.init()
    morseFile= PATH + 'T_morse_code.ogg'
    pygame.mixer.music.load(morseFile)
    #wave_object= wave.open(morseFile,'r')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1.0)
    time.sleep(THREE_UNITS)
    pygame.quit();
    while True:
        msg = raw_input('MESSAGE: ')
        verify(msg)
        for char in msg:
            if char == ' ':
                print ' '*7,
                time.sleep(SEVEN_UNITS)


            else:
                pygame.mixer.init(SAMPLE_FREQUENCY) # Define sound speed. Original is 8000
                pygame.init()
                morseFile= PATH + char.upper() + '_morse_code.ogg'
                print CODE[char.upper()],
                pygame.mixer.music.load(morseFile)
                #wave_object= wave.open(morseFile,'r')
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(1.0)
                time.sleep(THREE_UNITS)
                pygame.mixer.music.stop()
                pygame.quit();
        print '\n'

if __name__ == "__main__":
	main()
