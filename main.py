from old import Old
from young import Young

while(1):
    # Homepage

    print("Select User type:")
    print("1. Care-seeker")
    print("2. Care-taker")
    print("3. Close app")

    n = int(input())
    if n!= 3:
        print("\nPlease enter your id:")
        id = int(input())

    while(1):

        #Dashboard

        if n == 1:
            old = Old(id)
            print("\nWhat would you like to do?")
            print("1. See my profile")
            print("2. See requests")
            print("3. End caretaking period")
            print("Type any number to logout")

            x=int(input())
            print("\n")
            
            if x == 1:
                old.displayProfile()
            elif x == 2:
                old.seeRequests()
                print("\nIf you want to accept any, input the id of the profile. Else type '0'")
                request_id = int(input())
                if request_id != 0:
                    old.acceptRequest(id)
                else:
                    continue

            elif x == 3:
                end_id = old.caretaker
                person = Young(id)
                old.endPeriod(person)
            
            else:
                break

        elif n == 2:
            young = Young(id)
            print("\nWhat would you like to do?")
            print("1. See my profile")
            print("2. Find care-seeker")
            print("3. End caretaking period")
            print("Type any number to logout")

            x=int(input())
            print("\n")

            if x == 1:
                young.displayProfile()
            elif x == 2:
                if len(young) < 4:
                    young.seeProfiles()
                    print("\n If you want to send a request for care-taking, Please input the id. Else type '0'")
                    request_id = int(input())
                    if request_id != 0:
                        person = Old(request_id)
                        young.sendRequest(person)
                    else:
                        continue
                else:
                    print("You are taking enough care.")
            elif x == 3:
                print("Type the care-seeker's id.")
                end_id = int(input())
                person = Old(end_id)
                young.endPeriod(person)

            else:
                break

        elif n == 3:
            exit()
        else:
            print("enter valid input")