
class ParkSpace:
    def __init__(self):
        self.__stack = [];
        self.max_capacity = 1;
        self.timer=0; # for the purposes of randomly being removed

    
    def __repr__(self):
        if self.__is_empty():
            return 'None'
        return f'{self.get_vehicle()}';


    def __is_empty(self) -> bool:
        return len(self.__stack) == 0


    def __is_full(self) -> bool:
        return len(self.__stack) == 1


    def add_vehicle(self, something) -> None:
        if self.__is_full():
            raise OverflowError
        else:
            self.__stack.append(something)


    def pop_vehicle(self):
        if self.__is_empty():
            raise IndexError
        else:
            lastVal = self.__stack[-1]

            self.__stack.pop()
            return lastVal
    

    def get_vehicle(self):
        if self.__is_empty():
            # raise IndexError
            return f'None'
        else:
            return self.__stack[0]






