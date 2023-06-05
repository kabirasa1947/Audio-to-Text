import openai
import subprocess
import os
from pydub import AudioSegment
from tkinter import Tk, filedialog

# Set your OpenAI API key
openai.api_key = "Your-OPENAPI-Key"

def upload_and_transcribe_audio():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if file_path:
        file_size_mb = os.path.getsize(file_path) / (1024 * 1024)  # Calculate file size in MB
        if file_size_mb > 25:
            chunk_audio(file_path)  # Divide the audio file into chunks
        if not is_english(file_path):
            file_path = translate_audio(file_path)  # Translate audio to English
        transcript = transcribe_audio(file_path)
        return transcript
    else:
        return None

def chunk_audio(file_path):
    base_path = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)
    file_name_without_ext = os.path.splitext(file_name)[0]

    output_dir = os.path.join(base_path, f"{file_name_without_ext}_chunks")
    os.makedirs(output_dir, exist_ok=True)

    chunk_size_bytes = 25 * 1024 * 1024  # 25 MB

    song = AudioSegment.from_mp3(file_path)

    chunks = []
    for i in range(0, len(song), chunk_size_bytes):
        chunks.append(song[i:i + chunk_size_bytes])

    for i, chunk in enumerate(chunks):
        chunk.export(os.path.join(output_dir, f"{file_name_without_ext}_chunk{i+1}.mp3"), format="mp3")

    print("Audio file divided into chunks.")

def is_english(file_path):
    cmd = ['ffprobe', '-i', file_path]
    output = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode()

    return "Stream #0:0(und): Audio: pcm_s16le" in output

def translate_audio(file_path):
    output_path = os.path.join(os.path.dirname(file_path), "translated_audio.mp3")

    cmd = ['ffmpeg', '-i', file_path, '-acodec', 'mp3', '-y', output_path]
    subprocess.call(cmd)

    print("Audio translated to English.")
    return output_path

def transcribe_audio(file_path):
    audio_file = open(file_path, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript

# Example usage
print("Select an MP3 file to upload and transcribe:")
transcript = upload_and_transcribe_audio()
if transcript:
    print("Transcript:", transcript)
