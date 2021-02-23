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
    outfile = outputfolder+"sample.mp3"
    video = moviepy.editor.VideoFileClip(fileinput)
    audio = video.audio
    audio.write_audiofile(outfile)
    basename = outfile.split(".")[0]
    ext = outfile.split(".")[1]
    if ext == "mp3":
        sound = AudioSegment.from_mp3(outfile)
        sound.export('audio' + '.wav', format="wav")

    r = sr.Recognizer()
    OUTFILE = outputfolder+"transcript.txt"
    file =  open(outputfolder + OUTFILE, 'w')

    infile = "audio.wav" if ext == "mp3" else outfile

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