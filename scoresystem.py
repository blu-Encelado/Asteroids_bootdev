
class ScoreSystem:

    def __init__(self):
        
        self.__start_point = 0
        
    
    def add_point(self, point):

        self.__start_point += point
    
    def return_score(self):
        
        return self.__start_point