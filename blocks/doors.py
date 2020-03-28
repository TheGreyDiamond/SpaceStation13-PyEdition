doorCycle = ["closed","opening","open","closing"]
class externalDoor():
    def __init__(self):
        self.texture = ".\\textures\\door\\external\\closed.png"
        self.state = "closed"
        self.cycle = 0
        self.type = "door"
        self.health = 100
        self.needsAnimation = False
        self.animationStarted = False
        self.animationFrame = 0
        self.animationFrameAmount = 5
        self.animationTime = 0

    def setState(self, newState):
        if newState in doorCycle:
            self.state = newState
        self.updateTexture()


    def updateTexture(self):
        if (self.state == "closed"):
            self.texture = ".\\textures\\door\\external\\closed.png"
            self.needsAnimation = False
            self.animationStarted = False
            self.cycle = 0
            self.animationFrame = 0
        elif (self.state == "open"):
            self.texture = ".\\textures\\door\\external\\open.png"
            self.needsAnimation = False
            self.animationStarted = False
            self.cycle = 2
            self.animationFrame = 0
        elif (self.state == "opening"):
            self.texture = ".\\textures\\door\\external\\opening-s.png"
            self.needsAnimation = True
            self.animationStarted = False
            self.cycle = 1
            self.animationFrame = 1
        elif (self.state == "closing"):
            self.texture = ".\\textures\\door\\external\\closing-s.png"
            self.needsAnimation = True
            self.animationStarted = False
            self.cycle = 3
            self.animationFrame = 0
        else:
            raise Exception("Unknow door state set")

    def tick(self):
        if(self.animationFrame == self.animationFrameAmount):
            if(self.state == "opening"):
                self.setState("open")
            elif(self.state == "closing"):
                self.setState("closed")

    def calcAnimationPos(self):
        if(self.animationFrame == 0):
            return(0, 0, 32, 32)
        elif(self.animationFrame == 1):
            return (32, 0, 32, 32)
        elif (self.animationFrame == 2):
            return (0, 32, 32, 32)
        elif (self.animationFrame == 3):
            return (32, 32, 32, 32)
        elif (self.animationFrame == 4):
            return (0, 64, 32, 32)
        elif (self.animationFrame == 5):
            return (32, 64, 32, 32)
        else:
            print("UNKNOW FUCKING STATE YOU IDIOT")
            print(self.animationFrame)

    def nextFrame(self):
        if(self.animationFrame < self.animationFrameAmount):
            self.animationFrame -=- 1
        else:
            self.animationFrame = 0


    def cycleState(self):
        if(self.cycle < 3):
            self.setState(doorCycle[self.cycle+1])
        else:
            self.setState(doorCycle[0])
            self.cycle = 0
