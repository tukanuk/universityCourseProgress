#!/usr/bin/env python3

# import json
# import requests
import csv
import argparse
import datetime
# import time
# from shutil import copyfile

class Activity:
    """ An Activity Record """

    def __init__(self, courseType, courseName, name, email, progress, complete, lastAccesed):
        self.courseType = courseType
        self.courseName = courseName
        self.name = name
        self.email = email
        self.progress = float(progress)/100
        self.complete = (complete == "TRUE")

        # self.lastAccesed = lastAccesed
        self.lastAccesed = datetime.datetime.strptime(lastAccesed, '%Y-%m-%d')


    def printInfo(self):
        """ Print the Activity """
        print(f"""Type:     {self.courseType:25} Course:   {self.courseName:20}
Name:     {self.name:25} Email:    {self.email:20}
Progress: {self.progress * 100:>3.0f}{"%":22} Complete: {self.complete}
Accesed:  {self.lastAccesed.date()}\n""")

def sortActivities(activityList):
    # dateList = [activity.lastAccesed for activity in activityList]
    # dateList.sort()
    # print(dateList)

    sortedList = sorted(activityList, key=lambda activity : activity.lastAccesed)
    for s in sortedList:
        print(s.lastAccesed)


def main():
    print("")

    #   ./courseProgress.py -f team.csv -c "Course" -o result.csv 
    parser = argparse.ArgumentParser(description="Track the team progress of a university course")
    parser.add_argument("dtuActivityFile", nargs=1, metavar="<dtu_activity_file>", help="The name of the .csv file")
    parser.add_argument("-course", "-c", help="The name of the course you are interested in")
    parser.add_argument("-output", "-o", required=False, help="Specifiy the custom file output, otherwise _result will be appended")


    args = parser.parse_args()

    print(f"{'The args are:':35} {args}")


    # extract the args
    dtuActivityFile = args.dtuActivityFile[0]
    course = args.course

    if args.output != None:
        outputFileName = args.output
    else:
        outputFileName = f"{dtuActivityFile.split('.')[0]}_result.csv"

    print(f"{'The activity file is:':35} {dtuActivityFile}\n{'The course we are interested in is:':35} '{course}'\n{'The output will be:':35} {outputFileName}")


    dtuActivityList = []

    # open the dtu_activity file
    with open(dtuActivityFile, newline='', encoding='utf-8-sig') as csvfile:
        data = csv.DictReader(csvfile)
        print(f"{'Field check:':35} {data.fieldnames}")
        for row in data:
            # print(f"Course: {row['asset']}\t Name: {row['name']}\t Progress: {row['progress']}\t Last Accessed: {row['lastAccess']}")
            activity = Activity(row['type'], row['asset'], row['name'], row['email'], row['progress'], row['complete'], row['lastAccess'])
            # activity.printInfo()
            dtuActivityList.append(activity)



    # test the list
    # for item in dtuActivityList:
    #     item.printInfo()

    # filter the list
    if course != None:
        dtuActivityList = [act for act in dtuActivityList if act.courseName == course]
        # for act in dtuActivityList:
        #     print(act.printInfo())
    else:
        print("No filter applied")


    # sort for date
    dtuActivityList.sort(key=lambda activity: activity.lastAccesed, reverse=True)

    print()
    for d in dtuActivityList:
        d.printInfo()
    

    with open(outputFileName, mode="w", encoding="utf=8") as csvwriter:
        fieldnames = ['type', 'asset', 'name', 'email', 'progress', 'complete', 'lastAccess']
        writer = csv.DictWriter(csvwriter, fieldnames=fieldnames)

        writer.writeheader()
        for activity in dtuActivityList:
            writer.writerow({'type': activity.courseType, 'asset': activity.courseName, 'name': activity.name, 'email': activity.email, 'progress': activity.progress, 'complete': activity.complete, 'lastAccess': activity.lastAccesed})

if __name__ == "__main__":
     main()