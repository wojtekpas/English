import os, time
from shutil import copyfile
path = "D:\English\english_via_skype"
path_script = "%s\scripts" % path
path_original_doc = "%s\original_exercises\doc" % path
path_original_pdf = "%s\original_exercises\pdf" % path
path_solution_doc = "%s\solutions\doc" % path
path_solution_pdf = "%s\solutions\txt" % path
path_vocab = "%s\vocab" % path
print ("Pliki w folderze: ")
filenames = os.listdir(path_script)
print (filenames)
id = 141

for filename in filenames:
    if "py" in filename:
        continue
    filename_absolute = "%s\%s" % (path_script, filename)
    names = str(filename).split(".docx")
    if len(names) == 2:
        oldname = names[0]
        newname_orig = "%s\lesson_%d_%s_original.docx" % (path_original_doc, id, oldname)
        newname_edit = "%s\lesson_%d_%s_edit.docx" % (path_solution_doc, id, oldname)
        print newname_orig
        copyfile(filename_absolute, newname_orig)
        print newname_edit
        copyfile(filename_absolute, newname_edit)
    else:
        names = str(filename).split(".pdf")
        if len(names) == 2:
            oldname = names[0]
            newname = "%s\lesson_%d_%s.pdf" % (path_original_pdf, id, oldname)
            print newname
            copyfile(filename_absolute, newname)