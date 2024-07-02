import json
import uuid


class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, uuid.UUID):
            return str(o)
        return super().default(o)
