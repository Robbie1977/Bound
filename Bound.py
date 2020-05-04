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
         value = sys.argv[1]
            
    if (readdata[0][0][0] < 1):
        readdata[0][0][0] = value
    #if (readdata[1][0][0] < 1):
    #    readdata[1][0][0] = np.uint8(1)
    #if (readdata[0][1][0] < 1):
    #    readdata[0][1][0] = np.uint8(1)
    #if (readdata[0][0][1] < 1):
    #    readdata[0][0][1] = np.uint8(1)
    #if (readdata[1][1][1] < 1):
    #    readdata[1][1][1] = np.uint8(1)
    filesize = np.subtract(readdata.shape, 1)  
    if (readdata[filesize[0]][filesize[1]][filesize[2]] < 1):
        readdata[filesize[0]][filesize[1]][filesize[2]] = value
    #if (readdata[filesize[0]-1][filesize[1]-1][filesize[2]-1] < 1):
    #    readdata[filesize[0]-1][filesize[1]-1][filesize[2]-1] = np.uint8(1)
    #if (readdata[filesize[0]][filesize[1]-1][filesize[2]-1] < 1):
    #    readdata[filesize[0]][filesize[1]-1][filesize[2]-1] = np.uint8(1)
    #if (readdata[filesize[0]-1][filesize[1]][filesize[2]-1] < 1):
    #    readdata[filesize[0]-1][filesize[1]][filesize[2]-1] = np.uint8(1)
    #if (readdata[filesize[0]-1][filesize[1]-1][filesize[2]] < 1):
    #    readdata[filesize[0]-1][filesize[1]-1][filesize[2]] = np.uint8(1)
    #
    #if (readdata[0][filesize[1]][filesize[2]] < 1):
    #    readdata[0][filesize[1]][filesize[2]] = np.uint8(1)
    #if (readdata[filesize[0]][0][filesize[2]] < 1):
    #    readdata[filesize[0]][0][filesize[2]] = np.uint8(1)
    #if (readdata[filesize[0]][filesize[1]][0] < 1):
    #    readdata[filesize[0]][filesize[1]][0] = np.uint8(1)
    #if (readdata[0][0][filesize[2]] < 1):
    #    readdata[0][0][filesize[2]] = np.uint8(1)
    #if (readdata[filesize[0]][0][0] < 1):
    #    readdata[filesize[0]][0][0] = np.uint8(1)
    #if (readdata[0][filesize[1]][0] < 1):
    #    readdata[0][filesize[1]][0] = np.uint8(1)
    print('Saving result to %s...'% outfile)
    nrrd.write(outfile, readdata, header=header)

print('Done.')
