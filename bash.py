import os 
from os import listdir
from os.path import isfile, join
import moviepy.editor
import sys, getopt, argparse
import speech_recognition as sr 
from pydub import AudioSegment
import time
from google_trans_new import google_translator  
from languages import LANG
from constant import LANGUAGES, DEFAULT_SERVICE_URLS

if __name__ == '__main__': 
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_language', type=str, default='fr')
    parser.add_argument('--inputfilepath', type=str)
    parser.add_argument('--outputfolder', type=str)
    args = parser.parse_args()
    if args.output_language not in LANG:
        print("invalid destination language code, must be part of")
        print(LANG)
        exit(1)
    fileinput = args.inputfilepath
    outputfolder = args.outputfolder
    outfile = "sample.mp3"

    video = moviepy.editor.VideoFileClip(fileinput)
    audio = video.audio
    audio.write_audiofile(outfile)

    dir = "out"      
    os.mkdir(dir)
    os.system("split -b 200k sample.mp3 out/output_")
    list = os.listdir(dir) # dir is your directory path
    number_files = len(list)
    #print(number_files)
    onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]
    onlyfiles.sort()
    #print(onlyfiles)
    OUTFILE = outputfolder+"originalfile.txt"
    file =  open(OUTFILE, 'w')
    for f in onlyfiles:
       fileinput = "out/"+f+".mp3"
       os.rename("out/"+f,fileinput)


       basename = fileinput.split(".")[0]
       ext = fileinput.split(".")[1]
       if ext == "mp3":
            #print("Base Name = "+basename+" ext = "+ext)
            #print(fileinput)
            sound = AudioSegment.from_mp3(fileinput)
            sound.export('audio' + '.wav', format="wav")

       r = sr.Recognizer()
       

       infile = "audio.wav" if ext == "mp3" else fileinput

       with sr.AudioFile(infile) as src:
            #print("withiner")
            while True:
                try:
                    #print("Triing")
                    audio = r.listen(src)
                    text = r.recognize_google(audio)
                    print(text)
                    time.sleep(0.5)
                    file.writelines(text+"\n")
                except Exception as ex:
                    print(str(ex))
                    break

    file.close()
    os.system("rm -rf out")
    os.system("rm audio.wav")
    os.system("rm sample.mp3")
    language = LANG[args.output_language]
    inputfile = args.inputfilepath
    outputfile = args.outputfolder
    translator = google_translator() 
    translatedfile = outputfolder+"translatedfile.txt" 
    with open(OUTFILE, 'r') as fileO:
        with open(translatedfile, 'w') as ofile:
            for line in fileO:
                res = translator.translate(line,lang_tgt=language)  
                print(res)
                ofile.writelines(res+"\n")

    