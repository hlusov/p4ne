import glob

PATH = 'C:\\Users\\laser\\Downloads\\config_files\\config_files\\'

files = glob.glob(PATH + '*.log')
iplist = set()

for file in files:
    with(open(file)) as f:
        for line in f:
#            print(line)
            if line.find("ip address") == 1:
               iplist.add(line.replace("ip address", "").strip())

for i in iplist:
    print(i)

