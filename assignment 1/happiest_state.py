import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweets=[]
    sent = open(sys.argv[1])
    c=0
    with open(sys.argv[2]) as f:
        for line in f:
            tweets.append(json.loads(line))
    #print t[0].find("""source""")
    for i in tweets:
        if i.has_key("text"):
            if i["user"].has_key("location"):
                if i["place"] != None:
                #try:
                    #print i["user"]["location"]
                    #print "ohh yeahh", i["place"]["country"]
                    if i["place"]["country"].lower() == "united states" and i["place"]["country_code"].lower()=="us":
                        d=i["place"]["full_name"]
                        #print d,len(d[len(d)-2:])
                    #p=d.split()
                        if d[len(d)-2:].isupper() and c==0:
                            print d[len(d)-2:]
                            c=1
                    #if len(p)-1>0:
                    #    print p[len(p)-1]
                #except:
                    #continue

if __name__ == '__main__':
    main()
