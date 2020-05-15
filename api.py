from functools import wraps
from datetime import datetime
import os
import urllib.request
import uuid
import json
from vosk import Model, KaldiRecognizer
import sys

model_path = ''
audio_file = "/app/audio.wav"

"""
    How to use:
        > python3 api.py alphacep
        > python3 api.py iara
"""

args = sys.argv[1:]

model_type = args[0] 
if model_type == 'alphacep':
    model_path = '/app/models/alphacep'
elif model_type == 'iara':
    model_path = '/app/models/iara'

SAMPLE_FREQUENCY = 16000

model = Model(model_path)

recognizer = KaldiRecognizer(model, SAMPLE_FREQUENCY)

elapsed_time = None
transcript = []


with open(audio_file, "rb") as f:
    start_time = datetime.now()

    f.read(44)  # skip header

    while True:
        data = f.read(2000)
        if len(data) == 0:
            break

        if recognizer.AcceptWaveform(data):
            words = json.loads(recognizer.Result())
            transcript.append(words)

    words = json.loads(recognizer.FinalResult())
    transcript.append(words)

    end_time = datetime.now()
    elapsed_time = end_time - start_time


transcript = [t for t in transcript if len(t["result"]) != 0]

phrases = [
    t["text"] for t in transcript
]

transcript_text = ' '.join(phrases)

print(str(elapsed_time))
print(transcript_text)
