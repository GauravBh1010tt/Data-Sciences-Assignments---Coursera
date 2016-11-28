import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
    key = record[0]
    #value = [record[0],record[1:]]
    value = record[1]
    #print key
    value = value[0:value.__len__()-10]
    #g_value[value]=key
    mr.emit_intermediate(value,1)
    #d.append(w)

def reducer(key, list_of_values):
    #print key,"list",list_of_values.__len__()
    mr.emit(key)
    

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
