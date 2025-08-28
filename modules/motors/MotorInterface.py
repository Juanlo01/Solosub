

class motorClass:

    """ 
    Controls the motors 
    """

    def motor():
        """ Starts the motors """
        try:
            print('Motor Process: \033[32mOnline') 
        except:
            print('Motor Process: \033[31mOffline')
    
