import pdb
pdb.set_trace()
a= 12%3
b=ord('a')%ord('a')
c=(ord('z')+3)%ord('z')

print a,b,c



d=7%7
print d

def hash_string(keyword,buckets):
    h=0
    for c in keyword:
        h=(h+ord(c))
        remainder= h%buckets
    return remainder
#making empty hastable
def make_hasthable(nbuckets):
    i=0
    table=[]
    while i<nbuckets:
        table.append([])
    return table
#making empty hastable with for loop
def make_hashtable2(nbuckets):
    table=[]
    for entry in range (0,nbuckets):
        table.append([])
    return table

#Finding buckets
def hashtable_get_bucket(htable,key):
    return htable[hash_string(key, len(htable))]


#add elements to the hashtable
def hashtable_add(htable,key,value):
    bucket=hashtable_get_bucket(htable,key)
    bucket.append([key,value])

def hashtable_lookup(htable,key):
    bucket=hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0]==key:
            return entry[1]
    return None


def hashtable_update(htable,key,value):
    bucket=hastbale_get_bucket(htable,key)
    for entry in bucket:
        if entry[0]==key:
            entry[1]=value
            return
    bucket.append([key,value])













    

    

    



    

    

    



    

    

    





    

    

    



    

    





    

    

    



    

    

    



    

    

    





    

    

    



    

    





    

    

    



    

    

    



    

    

    





    

    

    



    

    





    

    

    



    

    

    



    

    

    





    

    

    



    

    





    

    

    



    

    

    



    

    

    





    

    

    



    

    





    

    

    



    

    

    



    

    

    





    

    

    



    

    





    

    

    



    

    

    



    

    

    





    

    

    



    

    





    

    

    



    

    

    



    

    

    





    

    

    



    

    

    



    

    

    

