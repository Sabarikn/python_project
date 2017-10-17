import zipfile
import sys
zipp=sys.argv[1]
filenames=sys.argv[2:]
z=zipfile.ZipFile(zipp,'w',zipfile.ZIP_DEFLATED)
for f in filenames:
 z.write(f,compress_type=zipfile.ZIP_DEFLATED)

