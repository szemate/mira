import time


expected_time = input("How fast do you think you are? (in seconds) ")
if expected_time != "":
    expected_time = int(expected_time)

    input("Press enter to start!")
    start_time = time.time()

    input("Measuring... press enter to stop!")
    end_time = time.time()

    duration = end_time - start_time
    if expected_time * 0.8 <= duration <= expected_time * 1.2:
        print("You were right :)")
    else:
        print("You were wrong :(")
        print("It took you " + str(duration) + " seconds")
else:
    print("Enter a number please!")
