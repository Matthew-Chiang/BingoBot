import threading
import speech_recognition as sr
import startCheck
import re

class Recorder(threading.Thread):
    def __init__(self,microphone,recognizer, instance):
        threading.Thread.__init__(self)
        self.microphone = microphone
        self.recognizer = recognizer
        self.instance = instance

    def run(self):
        print("recording")
        try:
            nextThread = Recorder(self.microphone,self.recognizer, self.instance+1)

            with self.microphone as source:
                audio = self.recognizer.record(source,2)

            nextThread.start()

            print("done")

            try:
                speech = self.recognizer.recognize_google(audio)
                print(speech)
                with open("bingobuffer.txt","a") as bufferFile:
                    speech = re.sub('[^0-9]','', speech)
                    bufferFile.write(' ' + speech + ' ')

                startCheck.main()

            except sr.UnknownValueError:
                print("didn't catch that")
        except KeyboardInterrupt:
            pass


def main():

    r = sr.Recognizer()
    m = sr.Microphone()

    try:
        print("silence pls")
        with m as source:
            r.adjust_for_ambient_noise(source)
        print("are you ready?")
        input()
        firstThread = Recorder(m,r,1)
        firstThread.start()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
