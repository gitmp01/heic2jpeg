
import os
import sys
import subprocess
from os import listdir
from os.path import isfile, join

# Path
if len(sys.argv) != 2:
    print 'usage python c.py path_to_directory_containing_images'
else:
    mypath = sys.argv[1]
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    outdir = os.path.join(mypath, 'output')

    # Creates the output dir if it doesn't exists
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    else:
        print 'Output dir already exists.'
        exit(0)

    for file in onlyfiles:
        (name, ext) = os.path.basename(file).split('.')

        if ext == 'heic' or ext == 'HEIC':
            destination = os.path.join(outdir, name) + '.jpg'
            print destination
            source = os.path.join(mypath, file)
            print source
            # print ('converting   ',os.path.join(mypath, file))
            subprocess.call(['tifig', '-p', '-q', '100', source, destination])


