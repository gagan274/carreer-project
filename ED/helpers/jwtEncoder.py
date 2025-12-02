import json
import base64
import hashlib  # for password hashing
import hmac

def encodeData(jsonData):
    # Secret key
    secret_key = b"INp8IvdIyeMcoGAgFGoA61DdBglwwSqnXJZkgz8PSnwSK"

    # Header
    header = {"alg": "HS256", "typ": "JWT"}
    header_json = base64.urlsafe_b64encode(json.dumps(header).encode()).decode()

    # Claims set (Payload)
    
    claims_json = base64.urlsafe_b64encode(json.dumps(jsonData).encode()).decode()

    # Concatenate Header and Payload
    unsigned_token = header_json + "." + claims_json

    # Signature
    signature = hmac.new(secret_key, unsigned_token.encode(), hashlib.sha256)
    signature_base64 = base64.urlsafe_b64encode(signature.digest()).decode()

    # JWT token
    jwt_token = unsigned_token + "." + signature_base64

    return(jwt_token)



