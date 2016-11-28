import MapReduce
import sys


mr = MapReduce.MapReduce()

def mapper(record):
    # key: document identifier
    # value: document contents
    i=record[1]
    j=record[2]
    if record[0]=='a':
        for k in range(0,5):
            mr.emit_intermediate((i,k),record)
    else:
        for k in range(0,5):
            mr.emit_intermediate((k,j),record)
    #d.append(w)

def reducer(key, list_of_values):
    total=[]
    #print key,"list",list_of_values
    for val in list_of_values:
        if val[0]=='a':
            for val1 in list_of_values:
                if val1[0]=='b':
                    if val[2]==val1[1]:
                        total.append(val[3]*val1[3])
    #print key[0],key[1],sum(total)
    mr.emit((key[0],key[1],sum(total)))
    
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
