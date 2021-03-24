#!/usr/bin/env python3


# TODO: Add unit tests.
# TODO: implement the --progress  function. Make sure both files are filtered and then look for name == name
#       then diff progress , add progress column
#       then diff lastAccess, add lastChecked column
# TODO: modify complete column to show TRUE if progress is greater than 95% (people skip the endings)
# TODO: Add course picker. If there is no -c flag Scan the file, list the courses, provide choice

import csv
import argparse
import datetime


class Activity:
    """ An Activity Record """

    def __init__(self, courseType, courseName, name, email, progress, complete, lastAccesed):
        self.courseType = courseType
        self.courseName = courseName
        self.name = name
        self.email = email
        self.progress = round(float(progress)/100, 2)
        self.complete = (complete == "true")
        self.lastAccesed = datetime.datetime.strptime(lastAccesed, '%m/%d/%y')

    def printInfo(self):
        """ Print the Activity """
        print(f"""Type:     {self.courseType:25} Course:   {self.courseName:20}
Name:     {self.name:25} Email:    {self.email:20}
Progress: {self.progress * 100:>3.0f}{"%":22} Complete: {self.complete}
Accesed:  {self.lastAccesed.date()}\n""")


def main():
    print("")

    #   ./courseProgress.py -f team.csv -c "Course" -o result.csv
    parser = argparse.ArgumentParser(
        description="Track the team progress of a university course")
    parser.add_argument("dtuActivityFile", nargs=1,
                        metavar="<dtu_activity_file>", help="The name of the .csv file")
    parser.add_argument(
        "-c", "--course", help="The name of the course you are interested in")
    parser.add_argument("-o", "--output", required=False,
                        help="Specifiy the custom file output, otherwise _result will be appended")
    parser.add_argument("-p", "--progress", required=False,
                        help="Compare the progress to an older version")
    parser.add_argument("-v", "--verbose",
                        help="Verbose output", action='store_true')

    args = parser.parse_args()

    # print(f"{'The args are:':35} {args}")

    # extract the args
    dtuActivityFile = args.dtuActivityFile[0]
    course = args.course
    verbose = args.verbose
    dtuProgressFile = args.progress

    if args.output != None:
        outputFileName = args.output
    else:
        outputFileName = f"{dtuActivityFile.split('.')[0]}_result.csv"

    if verbose:
        print(f"{'The activity file is:':35} {dtuActivityFile}\n{'The course we are interested in is:':35} '{course}'\n{'The output will be:':35} {outputFileName}")\

    dtuActivityList = []

    # open the dtu_activity file
    with open(dtuActivityFile, newline='', encoding='utf-8-sig') as csvfile:
        data = csv.DictReader(csvfile)
        if verbose:
            print(f"{'Field check:':35} {data.fieldnames}")
        for row in data:
            activity = Activity(row['type'], row['asset'], row['name'],
                                row['email'], row['progress'], row['complete'], row['lastAccess'])
            dtuActivityList.append(activity)

    # filter the list
    if course != None:
        dtuActivityList = [
            act for act in dtuActivityList if act.courseName == course]
    else:
        print("No filter applied")

    # sort for date
    dtuActivityList.sort(
        key=lambda activity: activity.lastAccesed, reverse=True)

    print()
    # a formatted list of records for verbose output
    for d in dtuActivityList:
        if verbose:
            d.printInfo()

    # if there are matches output to file
    if len(dtuActivityList) > 0:
        with open(outputFileName, mode="w", encoding="utf=8") as csvwriter:
            fieldnames = ['type', 'asset', 'name', 'email',
                          'progress', 'complete', 'lastAccess']
            writer = csv.DictWriter(csvwriter, fieldnames=fieldnames)

            writer.writeheader()
            for activity in dtuActivityList:
                writer.writerow({'type': activity.courseType, 'asset': activity.courseName, 'name': activity.name, 'email': activity.email,
                                'progress': activity.progress, 'complete': activity.complete, 'lastAccess': activity.lastAccesed})
    else:
        print("There were no matches found. Does the course match exactly?")


if __name__ == "__main__":
    main()
