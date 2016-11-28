import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

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
    #value = record[0]
    #words = value.split()
    #for w in words:
    #if w not in d:
    mr.emit_intermediate(key,1)
    #d.append(w)

def reducer(key, list_of_values):
    #print s
    total=0
    for v in list_of_values:
      total += v
    mr.emit((key,total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
