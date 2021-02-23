import moviepy.editor
import sys, getopt, argparse
import speech_recognition as sr 
from pydub import AudioSegment
import time


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_language', type=str, default='fr')
    parser.add_argument('--inputfilepath', type=str)
    parser.add_argument('--outputfolder', type=str)
    args = parser.parse_args()
    #if args.output_language not in LANG:
    #    print("invalid destination language code, must be part of")
    #    print(LANG)
    #    exit(1)
    fileinput = args.inputfilepath
    outputfolder = args.outputfolder

    basename = fileinput.split(".")[0]
    ext = fileinput.split(".")[1]
    if ext == "mp3":
        print("Base Name = "+basename+" ext = "+ext)
        print(fileinput)
        sound = AudioSegment.from_mp3("sample.mp3")
        sound.export('audio' + '.wav', format="wav")

    r = sr.Recognizer()
    OUTFILE = outputfolder+"transcript.txt"
    file =  open(outputfolder + OUTFILE, 'w')

    infile = "audio.wav" if ext == "mp3" else fileinput

    with sr.AudioFile(infile) as src:
        while True:
            try:
                audio = r.listen(src)
                text = r.recognize_google(audio)
                print(text)
                time.sleep(0.5)
                file.writelines(text)
            except Exception as ex:
                print(str(ex))
                break

    file.close()