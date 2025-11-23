import eventlet
from socketio import Server, WSGIApp
from TheDive import Tracking

eventlet.monkey_patch()

sio = Server(cors_allowed_origins="*")
app = WSGIApp(sio)



sim = Tracking(sio.emit, m=1, k=0)

@sio.on('test')
def test_simulation(sid):
    sim.test()

@sio.on('run')
def start_simulation(sid):
    (sio.start_background_task(sim.run))

@sio.on('fall')
def falling_simulation(sid):
    sim.falling()

@sio.on('walkright')
def wr_simulation(sid):
    sim.the_walking_exit("+")

@sio.on('walkleft')
def wl_simulation(sid):
    sim.the_walking_exit("-")

@sio.on('thebigrun')
def run_out(sid):
    sim.the_running_exit()

@sio.on('exitjump')
def the_exit(sid):
    sim.theJump = 1

@sio.on('stop')
def stop_simulation(sid):
    sim.running = False
    sim.start = False

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 8000)), app)