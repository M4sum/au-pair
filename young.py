from data import OldProfile, YoungProfile
oldprofiles = OldProfile()
youngprofiles = YoungProfile()

class Young:

    caretaking = []

    def __len__(self):
        return len(self.caretaking)

    def __init__(self, id):
        self.id=id
        self.name = (profile['name'] for profile in youngprofiles if profile['id'] == id)
        self.occupation = (profile['occupation'] for profile in youngprofiles if profile['id'] == id)
        self.gender = (profile['gender'] for profile in youngprofiles if profile['id'] == id)
        self.caretaking = (profile['caretaking'] for profile in youngprofiles if profile['id'] == id)
        self.caretaking = []

    def displayProfile(self):
        for profile in youngprofiles:
            if profile['id'] == self.id:
                print("id: ", self.id)
                print("Name: ", profile["name"])
                print("Occupation: ", profile["occupation"])
                print("Gender: ", profile["gender"])
                print("Caretaking id's: ", profile["caretaking"])
                print("\n")

    def seeProfiles(self):
        caretaking = self.caretaking
        #if self.len(caretaking) < 4:
        for profile in oldprofiles:
            print("id: ", self.id)
            print("Name: ", profile["name"])
            print("Age: ", profile["age"])
            print("Gender: ", profile["gender"])
            print("Care duartion: ", profile["care_duration_in_weeks"])
            print("Caretaker id: ", profile["caretaker"])
            print("\n")

    def sendRequest(self, person):
        person.requests.append(self.id)
        print("A request has been sent")

    def endPeriod(self, person):
        print(self.caretaking)
        if id in self.caretaking:
            self.caretaking.remove(id)
            person.caretaker = 0
            print("The period has been ended.")
        else:
            print("This is the wrong id")