from multiprocessing import Process
from modules.motors.motorInterface import motorClass

"""
Initiates launch protocol for AUV
"""

if __name__ == '__main__':
    motors = Process(target=motorClass.motor, args=())
    motors.start()
    motors.join()
