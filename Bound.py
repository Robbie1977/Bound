import numpy as np
import sys
import nrrd

reload(sys)  
sys.setdefaultencoding('utf8')

if (len(sys.argv) < 3):
    print('Error: missing arguments!' )
    print('e.g. python Bound.py 0-255 inputfile.nrrd [outputfile.nrrd]')
else:
    if (len(sys.argv) > 3):
        outfile = str(sys.argv[3])
    else:
        outfile = str(sys.argv[2])
            
    print('Adding boundary markers to %s...'% str(sys.argv[2]))
    readdata, header = nrrd.read(str(sys.argv[2]))
    if (header['type'] == 'uint8'):
         value = np.uint8(sys.argv[1])
    elif (header['type'] == 'uint16'):
         value = np.uint8(sys.argv[1])
    else:
         print('encoding issue!')
         print(header['type'])
         value = np.uint8(sys.argv[1])
            
    if (readdata[0][0][0] < value):
        readdata[0][0][0] = value
    filesize = np.subtract(readdata.shape, 1)  
    if (readdata[filesize[0]][filesize[1]][filesize[2]] < value):
        readdata[filesize[0]][filesize[1]][filesize[2]] = value
    print('Saving result to %s...'% outfile)
    nrrd.write(outfile, readdata, header=header)

print('Done.')
