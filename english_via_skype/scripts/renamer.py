import os, time
from shutil import copyfile
path = "D:\English\english_via_skype\scripts"
print ("Pliki w folderze: ")
filenames = os.listdir(path)
print (filenames)
id = 51
for filename in filenames:
    names = str(filename).split(".docx")
    if len(names) == 2:
        oldname = names[0]
        newname_orig = "lesson_%d_%s_original.docx" % (id, oldname)
        newname_edit = "lesson_%d_%s_edit.docx" % (id, oldname)
        copyfile(filename, newname_orig)
        copyfile(filename, newname_edit)