import json
from utils.encoder import Encoder


def serialize_data(data, is_singular=False):
    return json.loads(json.dumps(list(data), cls=Encoder)) if not is_singular else json.loads(json.dumps(
        data, cls=Encoder))
