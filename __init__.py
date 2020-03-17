from google_speech_recognizer import GoogleSpeechRecognizer
from extract_region import find_speech_regions
from audio_convert import AudioOperation
from formatter import format_fulltext, format_srt
import sys
import argparse

parser = argparse.ArgumentParser(
    description='Generate subtitle from video file!')

parser.add_argument('infile', argparse.FileType('r'), nargs=1)
parser.add_argument('-o', type=str, nargs=1, help="output srt name")
parser.add_argument('-l', type=str, nargs=1, help="language")

args = parser.parse_args()


def main():
    recognizer = GoogleSpeechRecognizer(rate=44100, encoding="MP3")
    converter = AudioOperation(args.infile)
    audio_file = converter.extract_audio()
    regions = find_speech_regions(audio_file)

    transcripts = []
    for region in regions:
        data = converter.extract(region)
        results = recognizer.recognize(data)
        for result in results:
            start_time, end_time = region
            transcripts.append({
                "start_time": start_time,
                "end_time": end_time,
                "text": u"{}".format(result.alternatives[0].transcript)
            })
    format_srt(transcripts, args.outfile)
    format_fulltext(transcripts, args.outfile)
    print("Full text file generated: ./text.txt")
    print("Subtitle text file generated: ./text.srt")


if __name__ == 'main':
    sys.exit(main())
