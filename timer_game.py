import time


while True:
    expected_time = input("How fast do you think you are? (in seconds) ")
    if expected_time != "":
        expected_time = int(expected_time)

        input("Press enter to start!")
        start_time = time.time()

        input("Measuring... press enter to stop!")
        end_time = time.time()

        duration = round(end_time - start_time, 1)
        if expected_time * 0.8 <= duration <= expected_time * 1.2:
            print("You were right :)")
        else:
            print("You were wrong :(")
            print("It took you " + str(duration) + " seconds")

        answer = input("Do you want to play a new game? (y/n) ")
        if answer != "y":
            break
    else:
        print("Enter a number please!")
