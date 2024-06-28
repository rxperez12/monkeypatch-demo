# Function that takes class and adds speak method
def add_speech(cls):
    cls.speak = lambda self, message: print(message)
    return cls

# Adding method to class with decorator
@add_speech
class RithmInstructor:
    def __init__(self, name):
        self.name = name

# Example
teacher = RithmInstructor('Joel')
teacher.speak('Document your code!!!!')

ta = RithmInstructor('Brian')
ta.speak('Starbucks breakfast burritos are good')

######################################################################
# Testing monkey patch
######################################################################


def mock_get_data_from_api():
    # Return some mock data
    return {"key": "value"}

# Use monkey patching to replace the original function with the mock function
get_data_from_api = mock_get_data_from_api
