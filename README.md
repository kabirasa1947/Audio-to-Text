# Audio-to-Text
Conver MP3 to text  V1 

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

    php Run the following command to execute the code: 
python <filename>.py

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


