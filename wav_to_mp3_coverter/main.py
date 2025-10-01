import os
from pydub import AudioSegment

def convert_wav_to_mp3(source_folder, target_folder, bitrate="320k"):
    """
    Converts all WAV files in source_folder to MP3 in target_folder
    with high quality (320kbps by default).
    """
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".wav"):
            wav_path = os.path.join(source_folder, filename)
            mp3_filename = os.path.splitext(filename)[0] + ".mp3"
            mp3_path = os.path.join(target_folder, mp3_filename)

            audio = AudioSegment.from_wav(wav_path)
            audio.export(mp3_path, format="mp3", bitrate=bitrate)
            print(f"Converted: {wav_path} -> {mp3_path}")

# Example usage:
# convert_wav_to_mp3("wav_folder", "mp3_folder")