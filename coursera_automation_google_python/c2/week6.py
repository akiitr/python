#Python script for the reanming the old username to new username

#!/usr/bin/env python3

import sys,subprocess

f = open(sys.argv[1])
lines = f.readlines()
f.close()

for line in lines:
    line_new = line.strip().replace('jane','jdoe')
    sub_inputs = ["mv",line.strip(),line_new]
    subprocess.run(sub_inputs)

#Bash file for the finding the files to be ranamed

#!/bin/bash

touch oldFiles.txt
files=$(grep 'jane_' ~/data/list.txt | cut -d ' ' -f3)

for i in $files; do
        if test -e "/home/student-00-242fe9494c70$i"; then
                echo "file $i exists"
                echo "/home/student-00-242fe9494c70$i" >> oldFiles.txt
        else
                echo "file $i does not exist"
        fi
done
