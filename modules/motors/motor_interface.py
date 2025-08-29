from colorama import Fore, Style, init

class MotorInterface:

    """ 
    Motor Control Interface 
    """

    def __init__(self):
        """ Initializes the MotorInterface Class """
        init() # Initialize colorama

    def __call__(self):
        """ Make instance callable for multiprocessing """
        self.start()

    def start(self):
        """ Starts Motor Process """
        try:
            print(f'Motor Process: {Fore.GREEN}Online{Style.RESET_ALL}') 
        except Exception as e:
            print(f'Motor Process: {Fore.RED}Offline - {e}{Style.RESET_ALL}')
    
