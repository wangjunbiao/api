from eth_keys import keys
import base64


def sign_message_with_static_key(message):
    pk = _generate_static_private_key()
    signature = pk.sign_msg(message)
    signature_bytes = signature.to_bytes()
    return signature_bytes


def generate_static_public_address():
    pk = _generate_static_private_key()
    public_address = pk.public_key.to_checksum_address().lower()
    return public_address


def generate_test_authorization(message=''):
    signature = sign_message_with_static_key(message)
    headers = {
        "Authorization": "Signature {}".format(base64.b64encode(signature))
    }

    return {
        'headers': headers,
        'public_address': generate_static_public_address()
    }


def _generate_static_private_key():
    return keys.PrivateKey(b'\x01' * 32)
