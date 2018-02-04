import os
import glob
import subprocess
import argparse
from pydub import AudioSegment
from pydub.utils import make_chunks
from scipy.io import wavfile
from matplotlib import pyplot as plt
from PIL import Image

def mp3towav(path):
  files=glob.glob(path+'*.mp3')
  if len(files)==0:
    return 10
  for file in files:
    mp=file
    wa=file.replace('mp3','wav')
    subprocess.call(['sox', mp, '-e', 'mu-law','-r', '16k', wa, 'remix', '1,2'])

def makechunks(path):
  waves=glob.glob(path+'*.wav')
  if len(waves)==0:
    return 10
  for i in waves:
    w=i
    myaudio=AudioSegment.from_file(i,'wav')
    chunk_length_ms=10000
    chunks=make_chunks(myaudio,chunk_length_ms)
    print chunks
    for i,chunk in enumerate(chunks):
        chunk_name = w.split('.')[0]+"chunk{0}.wav".format(i)
        print chunk_name
        print "exporting", chunk_name
        chunk.export(chunk_name, format="wav")

def graph_spectrogram(wav_file):
    rate, data = get_wav_info(wav_file)
    print type(data),len(data)
    nfft = 256  # Length of the windowing segments
    fs = 256    # Sampling frequency
    pxx, freqs, bins, im = plt.specgram(data, nfft,fs)
    print "pxx : ",len(pxx)
    print "freqs : ",len(freqs)
    print "bins : ",len(bins)
    #plt.axis('on')
    #plt.show()
    plt.axis('off')
    plt.savefig(wav_file.split('.')[0]+'.png',
                dpi=100, # Dots per inch
                frameon='false',
                aspect='normal',
                bbox_inches='tight',
                pad_inches=0) # Spectrogram saved as a .png
    im=Image.open(wav_file.split('.')[0]+'.png')
    rgb_im=im.convert('RGB')
    rgb_im.save(wav_file.split('.')[0]+'.jpg')
    if os.path.exists(wav_file.split('.')[0]+'.png'):
      os.remove(wav_file.split('.')[0]+'.png')

def get_wav_info(wav_file):
    rate, data = wavfile.read(wav_file)
    return rate, data
      
def wav2spectrogram(path):
  waves=glob.glob(path+'*.wav')
  if len(waves)==0:
    return 10
  for f in waves:
    try:
      print "Generating spectrograms.."
      graph_spectrogram(f)
    except Exception as e:
      print "Something went wrong while generating spectrogram: ",e
  

if __name__=='__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('path',help="Specify the path to the music directory")
  parser.add_argument('--mkchunks',help="Set this flag if you want to make chunks of waves",action="store_true")
  parser.add_argument('--mp3towav',help="Set this flag if you want to convert mp3 to wav",action="store_true")
  parser.add_argument('--spectrogram',help="Set this flags  to create spectrograms",action="store_true")
  args=parser.parse_args()
  if args.mp3towav:
    print "Path : ",args.path
    try:
      r=mp3towav(args.path)
      if r==10:
        print "No mp3 files in specified directory"
      else:
        print "All mp3 files processed completely"
    except Exception as e:
      print "Something went wrong :",e
  if args.mkchunks:
    print "Searching for wav files in :",args.path
    try:
      r=makechunks(args.path)
      if r==10:
        print "No wav files in given path"
      else:
        print "Completed successfully"
    except Exception as e:
      print "Something went wrong : ",e
  if args.spectrogram:
    print "Finding files in : ",args.path
    try:
      r=wav2spectrogram(args.path)
      if r==10:
        print "No wav files found in the given path"
      else:
        print "All mp3 files processed completely"
    except Exception as e:
      print "Something went wrong: ",e

