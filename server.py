from datetime import datetime
import os

import json

from vosk import Model, KaldiRecognizer

import urllib.request
import uuid

from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO


MODEL_PATH = "model/"

AUDIO_PATH = "audio/"

SAMPLE_FREQUENCY = 16000

model = Model(MODEL_PATH)


def download_temp_file(url, dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    filename = os.path.join(dir_name, str(uuid.uuid4()))
    urllib.request.urlretrieve(url, filename=filename)
    return filename


def remove_temp_file(filename):
    if os.path.exists(filename):
        os.remove(filename)


def post_transcribe(audio_url):

    recognizer = KaldiRecognizer(model, SAMPLE_FREQUENCY)

    elapsed_time = None
    transcript = []

    audio_file = download_temp_file(audio_url, AUDIO_PATH)

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

    remove_temp_file(audio_file)

    transcript = [t for t in transcript if len(t["result"]) != 0]

    phrases = [t["text"] for t in transcript]

    transcription = " ".join(phrases)

    return {
        "elapsed_time": str(elapsed_time),
        "transcription": transcription,
    }


def dict_2_bytes(data):
    json_data = json.dumps(data)
    binary_data = json_data.encode()
    file_pointer = BytesIO(binary_data)
    return file_pointer.getvalue()


def bytes_to_dict(data):
    json_data = json.loads(data.decode("utf-8"))
    return json_data


class TranscriptionHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()

        self.wfile.write(b"API is Running!")

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        body = bytes_to_dict(self.rfile.read(content_length))

        url = body["url"]

        print(f"Transcription URL {url}")

        response = post_transcribe(url)

        self.send_response(201)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        self.wfile.write(dict_2_bytes(response))


if __name__ == "__main__":
    HOST = "0.0.0.0"
    PORT = 8000

    server = HTTPServer((HOST, PORT), TranscriptionHTTPRequestHandler)

    print(f"Starting server {HOST}:{PORT}, use <Ctrl-C> to stop")
    print("Warning: http.server is not recommended for production.")

    server.serve_forever()