import sys
import hashlib


filename = sys.argv[1]

try:
    f = open(filename, 'r')
except Exception as e:
    print(e)
    sys.exit()
file_data = f.readlines()
for line in file_data:
    hash = hashlib.md5(line.strip('\n').encode()).hexdigest()
    print('{0}: \t{1}'.format(line.strip('\n'), hash))
