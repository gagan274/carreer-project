import jwt
import os
def tokenDecoder(token: str):

    decoded_data = jwt.decode(token,
                              key=b'INp8IvdIyeMcoGAgFGoA61DdBglwwSqnXJZkgz8PSnwSK',
                              algorithms=["HS256"])

    return decoded_data

