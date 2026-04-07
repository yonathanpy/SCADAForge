import hashlib

CHAIN = []

def record(entry):
    prev = CHAIN[-1]["hash"] if CHAIN else "0"
    raw = f"{prev}{entry}".encode()
    h = hashlib.sha256(raw).hexdigest()
    block = {"entry": entry, "hash": h}
    CHAIN.append(block)
    return block
