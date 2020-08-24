import mmh3
import hashlib

def get_hash(i,value):
    if(i == 0):
        i = -12345
    #https://stackoverflow.com/questions/11954086/which-hash-functions-to-use-in-a-bloom-filter
    hash1 = hashlib.sha256()
    hash1.update(value.encode('utf-8'))
    return int(hash1.hexdigest(),16) + (i*mmh3.hash128(value))

class CountSketch:
    table = {}
    max_length = 100000

    def __init__(self,num_hashes,max_length):
        for i in range(num_hashes):
            self.table[i] = [0] * max_length

        self.max_length = max_length

    def increment(self,value):
        for i in range(len(self.table)):
            self.table[i][get_hash(i,value)%max_length]+=1

    def get_min_count(self,value): 
        counts = [0]*len(self.table)
        for i in range(len(self.table)):
            counts[i] = self.table[i][get_hash(i,value)%max_length]
        print('Finding min of ',counts)
        return min(counts)
 
    def __str__(self):
        res = ''
        for key in self.table:
            res+='\n'+str(key)+'='+str(self.table[key])

        return res
            

max_length = 30
hashes = 7

cms = CountSketch(hashes,max_length)
print(cms)

cms.increment('a')
print(cms)
print(cms.get_min_count('a'))

for i in range(10):
    cms.increment('a')
print(cms)
print(cms.get_min_count('a'))

for i in range(10):
    cms.increment('e')
print(cms)
print(cms.get_min_count('a'))