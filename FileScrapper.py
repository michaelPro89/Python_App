import shutil
import fileinput
import os

# @author Michal Switala
#
# You can reach me out on : https://github.com/michaelPro89

class FileScrapper:

    def __init__(self):
        pass

    def copy(self, file, file_destiny):
        shutil.copy("./dir/vagrant3/{file}".format(file=file), file_destiny)

    def edit_files(self, file1):
        print("Im inside editing files")
        for line in fileinput.FileInput(file1, inplace=1):
            if 'VM_OWNER="PLEASE-CHANGE-ME"' in line:
                # line = line.rstrip()
                line = line.replace("PLEASE-CHANGE-ME", 'michal.switala')
                print line
            else:
                print("test_line")

    def create_Bootstrap(self, original, new, username, userid):

        input = open(original, "rt")

        # save new copy of file over here :
        output = open(new, "wt")

        for line in input:

            if 'VM_OWNER="PLEASE-CHANGE-ME"' in line:

                output.write(line.replace('PLEASE-CHANGE-ME', username))

            elif 'SERVER_ID="PLEASE-CHANGE-ME"' in line:

                output.write(line.replace('PLEASE-CHANGE-ME', str(userid)))

            else:
                output.write(line)

        input.close()
        output.close()

    def create_Vagrantfile(self, original, new, sync_folder_path):

        input = open(original, "rt")

        # create a new copy of file over here :
        output = open(new, "wt")

        for line in input:

            if 'devs.synced_folder "~/src", "/dir/vagrant/my_src"' in line:

                output.write(line.replace('~/src', sync_folder_path))

            else:
                output.write(line)

        input.close()
        output.close()

    def deleteFile(self, filepath):
        os.remove(filepath)

    def renameFile(self, oldfile, newfile):

        os.rename(oldfile, newfile)
