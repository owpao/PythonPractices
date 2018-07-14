import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)

    print("Say something!")
    while True:
        audio = r.listen(source)

        # recognize speech using Google
        if(r.recognize_google(audio)=='stop' or r.recognize_google(audio)=='exit'):
            print("Bye!")
            break
        else:
            try:
                print("Sphinx thinks you said " + r.recognize_google(audio))
            except sr.UnknownValueError:
                print("Sphinx could not understand audio")
            except sr.RequestError as e:
                print("Sphinx error; {0}".format(e))