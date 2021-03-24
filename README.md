# universityCourseProgress

Track the team progress of a university course

## Usage

    usage: courseProgress.py [-h] [-c COURSE] [-o OUTPUT] [-p PROGRESS] [-v] <dtu_activity_file>

    positional arguments:
        <dtu_activity_file>   The name of the .csv file

    optional arguments:
    -h, --help              show this help message and exit
    -c COURSE, --course COURSE
                            The name of the course you are interested in
    -o OUTPUT, --output OUTPUT
                            Specifiy the custom file output, otherwise _result will be appended
    -p PROGRESS, --progress PROGRESS
                            Compare the progress to an older version [In development]
    -v, --verbose           Verbose output

Take a University teams .csv and filters to only the course you are interested in. Output as a .csv and ready for excel.

Additionally:

- Converts to standard percent and date format
