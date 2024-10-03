#!/usr/bin/env python3

import shutil
import os

def main():
    #this will change the OS to start in a specific directory.
    os.chdir("/home/student/mycode/")
    # this line will create a copy of a file and call it a backup.
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
    #not sure why we are removing the directory, but it would look clean
    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    # The following line will create the directory if it does not exist already and a backup as well as the full tree.
    shutil.copytree("5g_research/", "5g_research_backup/")
if __name__ == "__main__":
    main()

