# Audio-to-Text V1
Convert MP3 to text  V1 

# Audio Transcription

This Python script allows you to upload an audio file, transcribe it using the OpenAI Whisper API, and obtain the transcript.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python (version 3.6 or later)
- PyDub library (`pip install pydub`)
- tkinter library (`pip install tkinter`)
- FFmpeg library

You also need to have an OpenAI API key. Set your API key by replacing the placeholder in the script with your actual API key.

## Usage

1. Run the script `transcribe_audio.py`.
2. Select an MP3 file to upload and transcribe.
3. The script will divide the audio file into chunks (if necessary), translate the audio to English (if necessary), and transcribe the audio using the OpenAI Whisper API.
4. The resulting transcript will be displayed in the console.

## Files

- `transcribe_audio.py`: The main Python script for audio transcription.
- `README.md`: This readme file.
- `requirements.txt`: A file listing the required Python packages.

Step 1:
Install the required dependencies:

A. Ensure you have Python installed on your system.
   Open a command prompt or terminal and navigate to the project directory.
   Run the following command to install the required dependencies:
    
   pip install -r requirements.txt


B.Download FFmpeg:

  Go to the official FFmpeg website (https://ffmpeg.org/download.html).
  Download the FFmpeg executable appropriate for your operating system.
  Extract the downloaded archive to a known location on your computer.
  Set the path to the FFmpeg executable  (FFmpeg/bin)
  
  
Step 2:  
Update the code:
    Open the code file in a text editor.
    Set your OpenAI API key by replacing "YOUR_API_KEY" with your actual API key on the line:

    Here paste your Code: 
    openai.api_key = "YOUR_API_KEY"

Step 3:
Open a command prompt or terminal.
Navigate to the project directory.

    Run the following command to execute the code:  python <filename>.py

Step 4:
File selection:

A file dialog window will appear.
Select an MP3 file that you want to upload and transcribe.
Process execution:

The code will check the file size and language.
If the file size is above 25 MB, it will divide the audio file into chunks.
If the language is not English, it will translate the audio to English.
Finally, it will transcribe the audio and display the transcript.
View the transcript:

The transcript will be printed in the command prompt or terminal.
That's it! You have successfully run the code and obtained the audio transcript. 


If you encounter any issues or have additional questions, feel free to ask.


## License

This project is licensed under the [MIT License](LICENSE).





