from datetime import datetime
from courseProgress import courseProgress


def createActivityObject():
    activity = courseProgress.Activity(
        "course", "Course Name", "Ben User", "user@email.com", 0.9, "false", "3/22/21"
    )

    return activity


def test_createActivityObject():

    activity = createActivityObject()
    assert activity.courseName == "Course Name"
    assert activity.complete == False
    assert datetime.strftime(activity.lastAccesed, '%m/%d/%y') == "03/22/21"
