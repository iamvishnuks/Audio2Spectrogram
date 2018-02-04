# Audio2Spectrogram
This tool can be used to convert mp3 to processable wav files, generate chunks of wav's and generate spectrograms.
## Installation
For this tool to work properly you need to install following packages in your machine:
1. sox
2. libsox-fmt-mp3
3. ffmpeg
4. python-tk

This packages has been installed and tested on Ubuntu 16.04.

After installing above packages using apt, install python packages required by this tool by running below command.

`pip install -r requirements.txt`

## Usage
This tool have 3 options,
1. mp3towav
2. mkchunks
3. spectrogram

If you set mp3towav flag then it will convert all your mp3 file in specified directory to wav, if you set mkchunks flag then it will cut the wavfile into different 10 seconds files and if you have set spectrogram flag then it will convert all wav files to 
it's spectrogram.

### example:

`python Audio2Spectrogram.py <path to mp3 files directory> --mp3towav --mkchunks --spectrogram`

It will convert mp3 to wav, create chunks and generate spectrograms.
