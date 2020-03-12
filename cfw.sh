#!/bin/bash

usage()
{
    echo "Help:   cfw file [-d destination] | [-h]"
    echo ""
    echo "        file:                 The file to copy from windows (only from desktop)"
    echo ""
    echo "        [-d | --destination]: The destination folder."
    echo "                              Without destination the destination folder is where it is called."
    echo ""
    echo "        [-h | --help]:        The helping page. (This page)"
}

##### Main
if [ $# -eq 1 ] || [ $# -eq 3 ]; then
    if [ "$filename" == "-h" ] || [ "$filename" == "--help" ]; then
        usage
        exit
    fi

    filename=$1
    shift
    
    if [ $# -eq 2 ] && ( [ "$1" == "-d" ] || [ "$1" == "--destination" ] ); then
        shift
        destination=$1
    else
        destination="$filename"
    fi
    cp -r "/mnt/c/Users/EpaG/Desktop/"$filename $destination
else
    usage
fi