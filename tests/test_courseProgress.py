from courseProgress import courseProgress


def createActivityObject():
    activity = courseProgress.Activity(
        "course", "Course Name", "Ben User", "user@email.com", 0.9, False, "3/22/21"
    )

    return activity


def test_createActivityObject():

    activity = createActivityObject()
    assert activity.courseName == "Course Name"
