

class ParkSpace:
    def __init__(self):
        self.__stack = [];
        self.max_capacity = 1;
        self.timeout: float = 0; # for the purposes of randomly being removed

    
    def __repr__(self):
        if self.is_empty():
            return 'None'
        return f'{self.get_vehicle()}';


    def __getitem__(self):
        if self.is_empty():
            return None
        return self.__stack[0]


    def is_empty(self) -> bool:
        return len(self.__stack) == 0


    def __is_full(self) -> bool:
        return len(self.__stack) == 1



    def add_vehicle(self, something) -> None:
        if self.__is_full():
            raise OverflowError
        else:
            self.__stack.append(something)
            self.regenerate_timeout() # make the timeout random


    def pop_vehicle(self):
        if self.is_empty():
            raise IndexError
        else:
            lastVal = self.__stack[0]

            self.__stack.pop()
            self.regenerate_timeout() # make the timeout 0
            return lastVal
    

    def get_vehicle(self):
        if self.is_empty():
            # raise IndexError
            return f'None'
        else:
            return self.__stack[0]

    def regenerate_timeout(self) -> None:
        """  Generates 5 to 30 numbers (treated as seconds)
             update the self.timeout to this generated number
             if it is full, else set it to 0
            
        """
        from random import randrange
        if self.__is_full():
            self.timeout = randrange(5,30+1)
        else:
            self.timeout = 0







