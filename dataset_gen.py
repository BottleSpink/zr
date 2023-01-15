import scipy
from scipy.io import wavfile
import os
import copy
import json

def output_duration(length):
	hours = length // 3600 # calculate in hours
	length %= 3600
	mins = length // 60 # calculate in minutes
	length %= 60
	seconds = length # calculate in seconds

	return hours, mins, seconds

def write_json(new_data):
    filename = "/Users/krithiga.r/Documents/zrc/ZeroSpeech/datasets/2019/english/train.json"
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data.append(new_data)
        # Sets file's current position at offset.
        # convert back to json.
        file.seek(0)
    with open(filename, 'w') as json_file:
        json.dump(file_data, json_file, indent = 4)
        print(file_data)

if __name__ == "__main__":
    dataset_dir = "/Users/krithiga.r/Downloads/zrcdataset/english/"
    for filename in os.listdir(dataset_dir):
        filedata = []
        sample_rate, data = wavfile.read(os.path.join(dataset_dir, filename))
        len_data = len(data) # holds length of the numpy array
        t = len_data / sample_rate # returns duration but in floats

        hours, mins, seconds = output_duration(int(t))
        filedata = ["english/{}".format(filename,filename),0.0,0.59,"english/train/{}/{}".format(filename[:5],filename)]
        
        write_json(filedata)
        print('Total Duration: {}, {}:{}:{}'.format(filename, hours, mins, seconds))
  