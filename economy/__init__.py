import os
from os.path import exists

if os.path.exists('economy_data.json')==False:
    print('Economy file not found. Please download the file from GitHub or create one.\nIf you create a file, name it "economy_data.json" and in the file do this:\n[\n\n]')