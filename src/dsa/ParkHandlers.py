
class ParkBldg:
    def __init__(self, length, width):
        self.num_of_lanes: int = 0;


class ParkLane:
    def __init__(self):
        self.

    def randomize_alis(self, speed):
        pass



class ParkSpace:
    def __init__(self):
        self.__stack = [];
        self.max_capacity = 1;


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
            raise IndexError
        else:
            return self.__stack[-1]


    def __is_empty(self) -> bool:
        return len(self.__stack) == 0


    def __is_full(self) -> bool:
        return len(self.__stack) == self.max_capacity


    def __str__(self):
        return f'{self.__stack}';


