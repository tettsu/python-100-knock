#coding:utf-8

class Laser:
    def does(self):
        return "desintegrate"

class Claw:
    def does(self):
        return "crush"

class Gun:
    def does(self):
        return "shoot"


class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.gun = Gun()
    def does(self):
        return '''I have many attachments: My laser is to: %s, My claw is to: %s, My gun is to: %s ''' % (
            self.laser.does(),
            self.claw.does(),
            self.gun.does()
        )

robbie = Robot()
print(robbie.does())

