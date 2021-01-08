#!/usr/bin/python3

import json
import random
import pyttsx3

tts = pyttsx3.init()
tts.setProperty('voice', 'com.apple.speech.synthesis.voice.anna')

print('\nGerman Vocabulary Trainer\nCopyright 2021, Raphael Radna\nUniversity of California, Santa Barbara\n')

use_speech = input('Use text to speech? (y/n): ')
wordset = input('Load wordset: ')

with open('vocabulary.json') as f: 
    data = f.read()

dict = json.loads(data)
vocab = dict.get(str(wordset))
keys = list(vocab)
n_keys = len(keys)

random_order = list(range(0, n_keys))
random.shuffle(random_order)
n_correct = 0
missed = []

def test_word(n):
    k = random_order[n]
    word = keys[k]
    print(word)

    if (use_speech == 'y'):
        tts.say(word)
        tts.runAndWait()
        tts.stop()

    input('Your answer: ')
    return input('The correct answer: ' + vocab[word] + '\nWere you correct? (y/n): ')

for i in range(len(random_order)):
    print('\n' + str(i + 1) + '/' + str(n_keys) + ':', end=" ")
    v = test_word(i)

    if (v == 'y'):
        n_correct += 1
    else:
        missed.append(i)
        
    #print(str(n_correct) + '/' + str(i + 1)  + ' correct; ' + str(round((n_correct / (i + 1)) * 100)) + '%')

missed_index = 0
while (len(missed) > 0):
    print()
    v = test_word(missed[missed_index])
    
    if (v == 'y'):
        missed.remove(missed[missed_index])
    
    missed_index += 1
    if (missed_index >= len(missed)):
        missed_index = 0

print('\nYou got ' + str(n_correct) + '/' + str(n_keys) + ' correct (' + str(round((n_correct / n_keys) * 100)) + '%); auf Wiedersehen!')