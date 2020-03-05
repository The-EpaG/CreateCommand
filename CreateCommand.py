import os, stat
try:
    fileName = input('File to convert in command (bash): ')

    #input file
    if os.path.exists(fileName) == False or os.path.isfile(fileName) == False:
        print('Error: this is a directory or not exist.')
        quit()
    inputFile = open(fileName, 'r')
    if inputFile.readable() == False:
        print('Error: not redable.')
        quit()
    rows = inputFile.readlines()
    inputFile.close

    #output file
    finalName = fileName[: len(fileName) - 3 ]
    outputFileName = 'add' + finalName.replace(finalName[0],finalName[0].upper()) + 'Command.sh'
    outputFile = open(outputFileName, 'w')

    outputFile.write('#!/bin/bash\n')
    for row in rows:
        row = row.rstrip('\n')
        row = row.replace('\"', '\\\"')
        row = row.replace('$', '\$')
        outputFile.write('echo \"' + row + '\" >> ' + finalName + '\n')
    outputFile.write('sudo mv ' + finalName +  ' /usr/bin/' + finalName + '\n')
    outputFile.write('sudo chmod +x /usr/bin/' + finalName + '\n')
    outputFile.write('echo \"To use the new program type: ' + finalName +'\"\n')
    outputFile.write('sudo rm ' + outputFileName)
    outputFile.flush()
    outputFile.close()
    os.chmod(outputFileName, stat.S_IRWXU)
    print('DONE: for add the command execute \"./' + outputFileName + '\".')
except (KeyboardInterrupt, SystemExit):
    quit()
    