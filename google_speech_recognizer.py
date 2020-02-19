from google.cloud import speech_v1p1beta1
from google.cloud.speech_v1p1beta1 import enums


class GoogleSpeechRecognizer(object):
    def __init__(self, language_code='zh-TW', rate=16000, encoding='FLAC'):
        self.language_code = language_code
        self.sample_rate = rate
        self.encoding = encoding
        self.client = speech_v1p1beta1.SpeechClient()

    def recognize(self, data):
        audio = {
            "content": data
        }
        response = self.client.recognize({
            "language_code": self.language_code,
            "sample_rate_hertz": self.sample_rate,
            "encoding": enums.RecognitionConfig.AudioEncoding[self.encoding],
        }, audio)
        return response.results
