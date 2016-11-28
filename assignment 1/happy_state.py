import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweets=[]
    sent = open(sys.argv[1])
    with open(sys.argv[2]) as f:
        for line in f:
            tweets.append(json.loads(line))
    #print t[0].find("""source""")
    dic={}
    count=0
    for i in tweets:
        if i.has_key("text"):
            if i["user"].has_key("location"):
                try:
                    #print i["user"]["location"]
                    #print "ohh yeahh", i["place"]["country"]
                    if i["place"]["country"].lower() == "united states" or i["place"]["country_code"].lower()=="us":
                        d=i["user"]["location"]
                        p=d.split()
                        #print "fuck",p,len(p)-1
                        if len(p)-1>0:
                            print p[len(p)-1]
                except:
                    continue

                
if __name__ == '__main__':
    main()
