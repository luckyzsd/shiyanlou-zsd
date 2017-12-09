def strcount(str):
    chardict={}
    print(str)
    #charlist=set(str)
    for char in str:
        print(char)
        c=chardict.get(char)
        print(c)
        if c is None:
            chardict[char]=1
        else:
            chardict[char]+=1
            #print('c='+str(c))
    print(chardict)

if __name__=='__main__':
    s=input('Enter your string:')
    strcount(s)
