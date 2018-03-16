import sys
from os.path import isfile

textFiles = sys.argv[1:]
if len(textFiles) != 2:
    print 'Please enter 2 txt file name.'
    sys.exit

if all(map(lambda fn: isfile(fn) and fn.endswith('.txt'), textFiles)):
    with open(textFiles[0]) as fp1, open(textFiles[1]) as fp2, open('result.txt', 'w') as fp:
        while True:
            line1 = fp1.readline()
            if line1:
                fp.write(line1)
            else:
                break
            line2 = fp2.readline()
            if line2:
                fp.write(line2)
            else:
                break
        fp3 = fp1 if line1 else fp2
        for line in fp3.readlines():
            fp.write(line)
else:
    print 'Please enter 2 txt file name.'
    sys.exit
