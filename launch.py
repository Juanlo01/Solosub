from multiprocessing                    import Process
from modules.motors.motor_interface     import MotorInterface

"""
Initiates launch protocol for AUV
"""

if __name__ == '__main__':
    motor_interface = MotorInterface()

    motors = Process(target=motor_interface)
    motors.start()
    motors.join()
