import sys
import chilkat


def zipFile(s_filename, s_zipname, b_passwordProtected, s_password=" "):
    zip = chilkat.CkZip()

    #  Any string unlocks the component for the 1st 30-days.
    success = zip.UnlockComponent("Anything for 30-day trial")
    if (success != True):
        print(zip.lastErrorText())
        sys.exit()

    success = zip.NewZip(s_zipname)
    if (success != True):
        print(zip.lastErrorText())
        sys.exit()

    zip.SetPassword(s_password)
    zip.put_PasswordProtect(b_passwordProtected)

    saveExtraPath = False
    #success = zip.AppendOneFileOrDir("/temp/hamlet.xml",saveExtraPath)
    success = zip.AppendOneFileOrDir(s_filename, saveExtraPath)

    success = zip.WriteZipAndClose()
    if (success != True):
        print(zip.lastErrorText())
        sys.exit()

    print("Zip Created!")



def zipFolder(s_dir, s_zipname, b_passwordProtected, s_password=" "):
    zip = chilkat.CkZip()

    #  Any string unlocks the component for the 1st 30-days.
    success = zip.UnlockComponent("Anything for 30-day trial")
    if (success != True):
        print(zip.lastErrorText())
        sys.exit()

    success = zip.NewZip(s_zipname)
    if (success != True):
        print(zip.lastErrorText())
        sys.exit()
    
    zip.SetPassword(s_password)
    zip.put_PasswordProtect(b_passwordProtected)

    #  Append a directory tree.  The call to AppendFiles does
    #  not read the file contents or append them to the zip
    #  object in memory.  It simply appends references
    #  to the files so that when WriteZip or WriteZipAndClose
    #  is called, the referenced files are streamed and compressed
    #  into the .zip output file.

    recurse = True
    success = zip.AppendFiles(s_dir, recurse)
    if (success != True):
        print(zip.lastErrorText())
        sys.exit()

    success = zip.WriteZipAndClose()
    if (success != True):
        print(zip.lastErrorText())
        sys.exit()

    print("Zip Created!")

    print("Zip Created!")











#zipFile("testfile.txt", "testzip.zip")





# Abandoned
"""
import subprocess

zp = subprocess.call(['7z', 'a', 'your password', '-y', 'myzip.zip'] + ['testfile.txt'])
"""


"""
#from lib import pyminizip
from lib import setup

level=4 #level of compression
pyminizip.compress("your file", "myzip.zip", "your password", level)
"""

"""
#import zipfile, os

import subprocess

output_filename = "test.txt"
src_folder = "D"

rc = subprocess.call(['7z', 'a', '-pP4$$W0rd', '-y', 'myarchive.7z'] + ['testfile.txt', 'second.file'])

#rc = subprocess.call(['7z', 'a', output_filename + '.zip', '-mx9', '-pSecret^)'] + [src_folder + '/'])
"""