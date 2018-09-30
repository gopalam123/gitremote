import hashlib
#path = 'D:\.mobile pics'
def md5sum(path, blocksize=65536):
    hash = hashlib.md5()
    with open(filename, "rb") as f:
        for block in iter(lambda: f.read(blocksize), b""):
            hash.update(block)
    return hash.hexdigest()
print md5sum(D:\.mobile pics)
#name=md5sum(sravan)
