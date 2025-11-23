
from pylab import *

class Tracking:
    def __init__(self, emit_func, m, k):
        self.emit = emit_func
        self.running = False
        self.start = False
        self.therun = False
        self.m = 80
        self.g = 9.81
        self.k = 0.3
        self.v0 = 0.01
        self.walk = 0
        self.theJump = 0
        self.dt = 0.01

        self.theTest = 0.0

    def a(self, v):
        self.G = array([0.0, -self.m * self.g])
        abs_v = sqrt(v[0] ** 2 + v[1] ** 2)
        e_v = v / abs_v
        L = self.k * abs_v ** 2 * e_v
        return (self.G - L) / self.m


    def run(self):
        self.start = True
        self.walk = 0
        while self.start:
            time.sleep(self.dt)
            self.emit('start', {'is_running': self.running})


    def the_running_exit(self):

        if self.therun == True:
            self.therun = False
            self.start = False
        else:
            self.therun = True
            while self.therun:
                self.walk += 10
                self.emit('thewalkdata', {'walk': self.walk})
                time.sleep(self.dt)


    def the_walking_exit(self, direction):
        if direction == "+":
            self.walk += 5
            self.emit('thewalkdata', {'walk': self.walk})
        elif direction == "-":
            self.walk -= 5
            self.emit('thewalkdata', {'walk': self.walk})


    def falling(self):
        if self.running:
            return
        self.running = True
        self.v = array([self.v0, self.theJump])
        self.s = array([0.0, 0.0])

        t = 0.0
        #while self.running == True:
        while t < 1.4:

            the_acc = self.a(self.v)

            self.s += self.v * self.dt
            self.v += the_acc * self.dt
            t += self.dt
            self.emit('data', {
                'vx': round(self.v[0], 2),
                'vy': round(self.v[1], 2),
                'sx': round(self.s[0], 2),
                'sy': round(self.s[1], 2),
                't': round(t, 2)
            })
            time.sleep(self.dt)
        self.running = False








#