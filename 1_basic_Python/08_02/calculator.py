
class Calculator:
    def __init__(self):
        pass 

    def add(self, *args):
        total = 0
        for i in args:
            total+=i
        return total
    
    def get_history(self):
        pass 

def hello_world():
    print("helloWorld")