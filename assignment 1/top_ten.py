import sys
import json
import operator

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweets=[]
    with open(sys.argv[1]) as f:
        for line in f:
            tweets.append(json.loads(line))
    #print t[0].find("""source""")
    dic={}
    d=[]
    for i in tweets:
        if i.has_key("text"):
            if i["entities"]["hashtags"]!=[]:
                d.append(i["entities"]["hashtags"])
    for k in d:
        for j in k:
            for p in j.keys():
                try:
                    if p=="text":
                        if j[p] not in dic.keys():
                            dic[j[p]]=1.0
                        else:
                            dic[j[p]] += 1.0
                except:
                    continue
    #print dic
    sort = sorted(dic.iteritems(),key=operator.itemgetter(1))
    sort.reverse()
    for freq in sort[0:10]:
        print str(freq[0]),freq[1]
    #print max(dic.itervalues())

if __name__ == '__main__':
    main()
