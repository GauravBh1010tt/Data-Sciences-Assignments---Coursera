import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""
g_list={}
r_list={}
mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    d=[]
    #if record
    key = record[0]
    #value = [record[0],record[1:]]
    value = record[1]
    if key not in g_list.keys():
        g_list[key]=[value]
        r_list[key]=[value]
    else:
        g_list[key].append(value)
        r_list[key].append(value)
    #words = value.split()
    #for w in words:
    #if w not in d:
    mr.emit_intermediate(key,value)
    #d.append(w)

def reducer(key, list_of_values):
    print key,"list",list_of_values
    #print g_list[key]
    if g_list.has_key(key):
        #print "has key"
        for i in g_list[key]:
            #print "i",i
            if g_list.has_key(i):
                for k in g_list[i]:
                    #print "k",k
                    if key == k:
                        #print "yes",k
                        r_list[key].remove(i)
                        #print g_list
    #print g_list
    #total=0
    #for v in list_of_values:
      #total += v
    c=0
    print g_list[key]
    for val in r_list[key]:
        #if c<r_list.__len__():
            #c+=1
        mr.emit((key,val))
        mr.emit((val,key))
        #if c==r_list.__len__():
         #   for val in r_list[key]:
          #      mr.emit((val,key))
    #print r_list[key]
    #mr.emit((key,1))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
