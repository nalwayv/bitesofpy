""" 
Bite 71: Keep state in a class + make its instance callable
"""


class RecordScore():
    """RecordScore 
    
    Class to track a game's maximum score
    """
    def __init__(self):
        # save stored records
        self.record = []

    def __call__(self, value: int) -> int:
        """when called returns current max value"""
        self.record.append(value)
        return max(self.record)
