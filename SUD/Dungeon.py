from Room import Room

class Dungeon:
    def __init__(self):
        self.currentRoom = 0
        self.roomMap ={}

    def Init(self):
        print("And here you are \n ")
        self.roomMap["room 0"] = Room("room 0", "You are waiting alone by the reception desk of a grand yet empty castle. Should probably look around.", "room 1", "", "", "")
        self.roomMap["room 1"] = Room("room 1", "You have entered room 1","", "room 0", "room 3", "room 2")
        self.roomMap["room 2"] = Room("room 2", "You have entered room 2", "room 4", "", "", "")
        self.roomMap["room 3"] = Room("room 3", "You have entered room 3", "", "", "", "room 1")
        self.roomMap["room 4"] = Room("room 4", "You have entered room 4", "", "room 2", "room 5", "")
        self.roomMap["room 5"] = Room("room 5", "You have entered room 5", "", "room 1", "", "room 4")

        self.currentRoom = "room 0"

    def DisplayCurrentRoom(self):
        print(self.roomMap[self.currentRoom].desc)

        print("As you look around the room, you see a door that leads further into the castle. Where do you want to go?")
        exits = ["NORTH", "SOUTH", "EAST", "WEST"]
        exitStr = ""

        for i in exits:
            if self.roomMap[self.currentRoom].hasExit(i.lower()):
                exitStr += i + " "
        print(exitStr)

    def isValidMove(self, direction):
        return self.roomMap[self.currentRoom].hasExit(direction)

    def MovePlayer(self,direction):
        if self.isValidMove(direction):
            if direction == "north":
                self.currentRoom = self.roomMap[self.currentRoom].north
                print ("You walk north")
                return

            if direction == "south":
                self.currentRoom = self.roomMap[self.currentRoom].south
                print("You walk south")
                return

            if direction == "east":
                self.currentRoom = self.roomMap[self.currentRoom].east
                print("You walk east")
                return

            if direction == "west":
                self.currentRoom = self.roomMap[self.currentRoom].west
                print("You walk west")
                return