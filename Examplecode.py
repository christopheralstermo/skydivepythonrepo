
from pylab import *

class Tracking:
    def __init__(self, emit_func, m, k):
        self.emit = emit_func
        self.running = False
        self.start = False
        self.therun = False
        self.m = 80
        self.g = 9.81
        self.k = 0.25
        self.sats = 0
        self.v0 = 3 + self.sats
        self.walk = 0
        self.theJump = 0
        self.dt = 0.01

        self.theTest = 0.0


    def run(self):
        if self.start:
            self.start = False
        self.start = True
        self.walk = 0
        while self.start:
            time.sleep(self.dt)
            self.emit('start', {'is_running': self.running})


    def the_running_exit(self):
        if self.therun == True:
            return
        self.therun = True
        while self.therun:
            self.walk += self.v0
            self.emit('thewalkdata', {'walk': self.walk})
            time.sleep(self.dt)


    def choke_the_game(self):
        self.therun = False
        self.start = False
        self.running = False


    def the_walking_exit(self, direction):
        if direction == "+":
            self.walk += self.v0
            self.emit('thewalkdata', {'walk': self.walk})
        elif direction == "-":
            self.walk -= self.v0
            self.emit('thewalkdata', {'walk': self.walk})


    def rotate(self):
        self.theRotation = 0
        while self.theRotation < 90:
            self.theRotation += 1
            self.emit('rotate', {'theturn': self.theRotation}),
            time.sleep(0.01)


    def a_horizontal(self, v):
        # her er resultatet a = (k*v**2
        pass

    def a(self, v):
        self.G = array([0.0, -self.m * self.g])
        abs_v = sqrt(v[0]** 2 + v[1]** 2)
        e_v = v / abs_v
        L = self.k * abs_v**2 * e_v
        aks = (self.G - L) / self.m
        return aks

    def falling(self):
        if self.running:
            return
        else:
            self.running = True
            self.v = array([self.v0, self.theJump])
            self.s = array([0.0, 0.0])

            t = 0.0
            while self.running == True:
            #while t < 8:
            #while self.s[1] >= -100 and self.running:

                the_acc = self.a(self.v)

                self.s += self.v * self.dt
                #self.v[0] = 2
                self.v += the_acc * self.dt
                t += self.dt

                #print(self.s[1])

                self.emit('data', {
                    'vx': round(self.v[0], 2),
                    'vy': round(self.v[1], 2),
                    'sx': round(self.s[0], 2),
                    'sy': round(self.s[1], 2),
                    'mountainSy': round(self.s[1], 2),
                    't': round(t, 2)
                })
                time.sleep(self.dt)
            self.choke_the_game()








#