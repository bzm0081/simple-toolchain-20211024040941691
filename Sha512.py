import hashlib
theString = "this is the string to hash"
myHash = hashlib.sha512()
myHash.update(theString.encode('utf-8'))
myHashDigest = print(myHash.hexdigest())
myHash.update('info')
      
