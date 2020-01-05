from data import OldProfile, YoungProfile
oldprofiles = OldProfile()
youngprofiles = YoungProfile()

class Old:
    caretaker = 0
    requests = []

    def __init__(self, id):
        self.id = id
        self.name = (profile['name'] for profile in oldprofiles if profile['id'] == id)
        self.age = (profile['age'] for profile in oldprofiles if profile['id'] == id)
        self.gender = (profile['gender'] for profile in oldprofiles if profile['id'] == id)
        self.caretaker = (profile['caretaker'] for profile in oldprofiles if profile['id'] == id)

    def displayProfile(self):
        for profile in oldprofiles:
            if profile['id'] == self.id:
                print("id: ", self.id)
                print("Name: ", profile["name"])
                print("Age: ", profile["age"])
                print("Gender: ", profile["gender"])
                print("Care duartion: ", profile["care_duration_in_weeks"])
                print("Caretaker id: ", profile["caretaker"])
                print("\n")

    def seeRequests(self):
        if self.requests:
            print("Available caretakers")
            for profile in youngprofiles:
                if profile['id'] in self.requests:
                    print("id: ", self.id)
                    print("Name: ", profile["name"])
                    print("Occupation: ", profile["occupation"])
                    print("Gender: ", profile["gender"])
                    print("Caretaking id's: ", profile["caretaking"])
                    print("\n")
        else:
            print("No requests")

    def acceptRequest(self, person):
        if self.caretaker == 0:
            self.caretaker = id
            person.caretaking.append(id)
        else:
            print('Sorry, You already have a caretaker.')

    def endPeriod(self, person):
        if self.caretaker !=0:
            id = self.caretaker
            self.caretaker = 0
            person.caretaking.remove(id)
            print("You now don't have a caretaker.")
        else:
            print("You don't have a caretaker")
