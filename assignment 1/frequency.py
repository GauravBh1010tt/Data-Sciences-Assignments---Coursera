import sys

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    t=tweet_file.readlines()
    #print t[0].find("""source""")
    dic={}
    count=0
    #print "yes",dic["no fun"]
    #print dic["does not work"]
    for i in t:
        text=i.find("text")
        if text>0:
            text+=7
            source=i.find("""source""")-3
            tweet=i[text:source]
            for x in tweet.split():
                count+=1
                if x not in dic.keys():
                    dic[x]=1
                else:
                    dic[x]=dic[x]+1
    for x in dic.keys():
        freq = float(float(dic[x])/float(count))
        print x,freq
    #print "count",count
    #print val   
    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
