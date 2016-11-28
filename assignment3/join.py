import MapReduce
import sys



mr = MapReduce.MapReduce()


def mapper(record):
    # key: document identifier
    # value: document contents
    d=[]
    #if record
    key = record[1]
    #value = [record[0],record[1:]]
    value = record
    
    #words = value.split()
    #for w in words:
    #if w not in d:
    mr.emit_intermediate(key,value)
    #d.append(w)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #print list_of_values
    for i in list_of_values:
        if i[0]=='order':
            s=i[0:]
    #print s
    for v in list_of_values:
      total = []
      for k in s:
          total.append(k)
      #print total
      if v[0] != 'order':
          for i in v:
              total.append(i)
          #print total
          mr.emit(total)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
