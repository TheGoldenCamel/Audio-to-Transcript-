# Run this code and follow the steps in the console to create your transcript.
# If you do not have whisper installed, you will need to do "pip3 install whisper" in your console.
import whisper
import os

models = {'tiny', 'base', 'small', 'medium', 'large'}


file_name = input('Input new transcript file name (.txt already added to end): ')
file_path = file_name + '.txt'
audio_file_path = input('Input the full path to your audio file (e.g., /path/to/AudioTest.mp3): ')

pick_model = input("Pick the model you would like to choose. Not sure which one to choose? Type '1' to get whisper's affilate link ")


if pick_model == '1':
    print('https://github.com/openai/whisper?tab=readme-ov-file#available-models-and-languages')
    exit()

elif pick_model not in models:
    print('Error, not a selectable model, please re-run the code and enter a valid model.')
    exit()


model = whisper.load_model(pick_model)
result = model.transcribe(audio_file_path)
script = result["text"]

def TranscriptDebugging():
    print(script)

    # Save to a separate text file:

def TranscriptToText():
    global file_path

    with open(file_path, 'w') as file:
        file.write(script)

TranscriptDebugging()

TranscriptToText()
