import glob

PATH = 'C:\\Users\\laser\\Downloads\\config_files\\config_files\\'

files = glob.glob(PATH + "*.log")

for file in files:
    print(file)
