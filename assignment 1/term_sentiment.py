import sys
#import stopwords
import string

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
    dic_s={}
    for i in d:
        s=i.split()
        if len(s)>2:
            if len(s)>3:
                #print "yes"
                dic[s[0]+" "+s[1]+" "+s[2]]=s[3]
            else:
                dic[s[0]+" "+s[1]]=s[2]
        else:
            dic[s[0]]=s[1]
    #print "yes",dic["no fun"]
    #print dic["does not work"]
    for i in t:
        text=i.find("text")
        val=0.0
        if text>0:
            text+=7
            source=i.find("""source""")-3
            tweets=i[text:source]
            tweet=''
            no=['.','"',',',':',';','?','/']
            #print "bf", tweets
            for i in tweets:
                #print i
                if i.isalpha() or i not in no:
                    tweet+=i
                if i == ' ':
                    tweet+=' '
            #print "bf", tweet
            #bre  
            for x in tweet.split():
                if x in dic.keys():
                    val=val+float(dic[x])
                    #print type(dic[x])
                    #print "yes",x,dic[x]
            for x in tweet.split():
                if x not in dic.keys():
                    if x not in dic_s.keys():
                        dic_s[x]=val
                    else:
                        dic_s[x] = float(dic_s[x]) + val
            for x in tweet.split():
                #if x=='@JonasBrothers':
                 #   print x
                  #  bre
                #if x[0].isalnum():
                if x in dic_s.keys():
                    print x,dic_s[x]
                else:
                    print x,dic[x]
                #if x=='@JonasBrothers':
                 #   bre
        #print val   
   # hw()
   # lines(sent_file)
   # lines(tweet_file)

if __name__ == '__main__':
    main()
