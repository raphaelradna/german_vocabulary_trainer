# German Vocabulary Trainer

I wrote this simple program to quiz myself on vocabulary while learning German as part of my graduate studies. A CLI Python application, the program loads words from a user-editable database, presents them in a random order, then prompts the user to input a definition. It optionally reads the word via text-to-speech, to aid pronunciation. The program then reveals the correct answer, and prompts the user to report whether they were correct. It keeps track of missed words, presenting them again after all words in the set have been exhausted. Once every word has been defined correctly, the program gives the user their score and exits.

## Prerequisites

This program runs in Python, which can be downloaded from python.org, or via a platform-dependent package manager, e.g. [Homebrew](https://brew.sh/) on macOS. It aso requires you to use pip to install pyttsx3, which provides text-to-speech functionality. Once Python and pip are installed (pip is installed automatically with Python), run:

```
pip3 install pyttsx3
```

to add the text-to-speech package.

## Installing

Simply move ```german_vocabaulary_trainer.py``` and ```vocabulary.json``` to the desired directory on your system.

## Running

Using your shell (e.g. the 'Terminal' app on macOS), navigate to the directory containing the program using:
```
cd /your/path/here
```
Then launch the program with:
```
python3 german_vocabulary_trainer.py
```
The user is first prompted to choose whether or not to use the text-to-speech function. Note that this feature is hardcoded to support macOS, and will likely trigger an error on other platforms; to avoid that, simply enter ```n``` here.

Next, the program asks you which wordset to load. This must match one of the valid sub-dictionaries defined in ```vocabulary.json``` (see below). Entering one of the default wordset names of ```1``` or ```2``` would work for testing purposes.

## Editing/Adding Wordsets

You can define your own wordsets by editing ```vocabulary.json``` in a standard text editor. The document is human-readable, and is formatted as a top-level dictionary containing sub-dictionaries (wordsets) comprised of key/value pairs. Follow the example of the default wordsets to add new entries. You can also add new wordsets, so long as you are careful to preserve the formatting. If the program quits with an error after editing the database, this is the likely culprit.

## License

This project is licensed under the GNU General Public License v3.0; see [LICENSE.md](LICENSE.md) for details.