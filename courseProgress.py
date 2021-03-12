#!/usr/bin/env python3

# import json
# import requests
import csv
import argparse
# import time
# from shutil import copyfile

def main():
    print("Here we go")

    #   ./courseProgress.py -f team.csv -c "Course" -o result.csv 
    parser = argparse.ArgumentParser(description="Track the team progress of a university course")
    parser.add_argument("dtuActivityFile", nargs=1, metavar="<dtu_activity-file>", help="The name of the .csv file")
    parser.add_argument("-course", "-c", help="The name of the course you are interested in")
    parser.add_argument("-output", "-o", required=False, help="Specifiy the custom file output, otherwise _result will be appended")


    args = parser.parse_args()

    print(f"The args are: {args}")


    # extract the args
    dtuActivityFile = args.dtuActivityFile[0]
    course = args.course

    if args.output != None:
        outputFileName = args.output
    else:
        outputFileName = f"{dtuActivityFile[0].split()[0]}_result.csv"

    print(f"The activty file is {dtuActivityFile}, the course we are interested in is {course} and the output will be {outputFileName}")


    # open the dtu_activity file
    with open(dtuActivityFile, newline='') as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            print(f"Course: {row['asset']}\t Name: {row['name']}\t Progress: {row['progress']}\t Last Accessed: {row['lastAccess']}")


    print(data)

if __name__ == "__main__":
     main()