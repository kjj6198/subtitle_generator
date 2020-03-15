from google_speech_recognizer import GoogleSpeechRecognizer
from extract_region import find_speech_regions
from audio_convert import AudioOperation
from formatter import format_fulltext, format_srt


def main():
    recognizer = GoogleSpeechRecognizer(rate=44100, encoding="MP3")
    converter = AudioOperation("1.mp4")
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
    format_srt(transcripts, "./text.srt")
    format_fulltext(transcripts, "./text.txt")
    print("Full text file generated: ./text.txt")
    print("Subtitle text file generated: ./text.srt")


main()
