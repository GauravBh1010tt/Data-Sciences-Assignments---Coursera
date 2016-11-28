import sys

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    d=sent_file.readlines()
    t=tweet_file.readlines()
    #print t[0].find("""source""")
    dic={}
    for i in d:
        s=i.split()
        if len(s)>2:
            if len(s)>3:
                dic[s[0]+" "+s[1]+" "+s[2]]=s[3]
            else:
                dic[s[0]+" "+s[1]]=s[2]
        else:
            dic[s[0]]=s[1]
    #print "yes",dic["no fun"]
    for i in t:
        text=i.find("text")
        val=0.0
        if text>0:
            text+=7
            source=i.find("""source""")-3
            tweet=i[text:source]
            for x in tweet.split():
                if x in dic.keys():
                    val=val+float(dic[x])
                    #print type(dic[x])
                    #print "yes",x,dic[x]
        print val
    #print dic["does not work"]
    #hw()
#    lines(sent_file)
 #   lines(tweet_file)

if __name__ == '__main__':
    main()
