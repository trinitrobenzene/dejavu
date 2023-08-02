import json

from dejavu import Dejavu
from dejavu.logic.recognizer.file_recognizer import FileRecognizer
from dejavu.logic.recognizer.microphone_recognizer import MicrophoneRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)

if __name__ == "__main__":
    filename = "files/43s_cut.mp3"

    # create a Dejavu instance
    djv = Dejavu(config)

    # Fingerprint all the mp3's in the directory we give it
    # djv.fingerprint_directory("test", [".wav", ".mp3"])

    recognizer = FileRecognizer(djv)
    results = recognizer.recognize_file(filename=filename)
    print(f"No shortcut, we recognized: {results}\n")
