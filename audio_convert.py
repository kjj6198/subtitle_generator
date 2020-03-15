import subprocess
import tempfile
import os
from moviepy.editor import ffmpeg_tools


class AudioOperation(object):
    def __init__(self, filename=''):
        self.filename = filename

    def convert(self):
        temp_file = tempfile.NamedTemporaryFile(suffix=".wav")
        ffmpeg_tools.ffmpeg_extract_audio(self.filename, temp_file)
        return temp_file.name

    # extract audio from video
    def extract_audio(self):
        temp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        ffmpeg_tools.ffmpeg_extract_audio(self.filename, temp_file.name)
        return temp_file.name

    # extract given region audio
    def extract(self, region):
        start_time, end_time = region
        start_time = max(0, start_time - 0.25)  # react time
        end_time += 0.25
        temp_file = tempfile.NamedTemporaryFile(suffix=".wav")
        # using ffmpeg to get certain region of sound
        cmd = [ffmpeg_tools.get_setting("FFMPEG_BINARY"), "-y", "-i", self.filename, "-ss", "{}".format(start_time), "-t", "{}".format(end_time - start_time), "-ab", "%dk" % 16000,
               "-ar", "%d" % 44100, temp_file.name]
        ffmpeg_tools.subprocess_call(cmd, logger=None)
        return temp_file.read()

    def output_extract_audio(self, regions):
        if not os.path.exists("regions"):
            os.mkdir("regions")

        for i, region in enumerate(regions):
            audio = self.extract(region)
            with open('regions/{index}.wav'.format(index=i), "wb") as audio_file:
                audio_file.write(audio)
