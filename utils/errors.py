

class ConfigNotFoundError(Exception):
    def __init__(self, message="the config file not found!", detailed_message=None):
        super().__init__(message)
        self.detailed_message = detailed_message
    
    def __str__(self):
        if self.detailed_message:
            return f"{self.args[0]}: {self.detailed_message}"
        return super().__str__()