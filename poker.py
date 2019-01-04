import itertools
import random
values={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
def v(h):
    return values[h]
def fourofakind(hand):
    h=[hand[i][0] for i in xrange(5)]
    l=list(set(h))
    if len(l)==2:
        k=0
        for i in xrange(2):
            if h.count(l[i])==4:
                return 1
        return 0
    return 0
def fullhouse(hand):
    h=[hand[i][0] for i in xrange(5)]
    l=list(set(h))
    if len(l)==2:
        k1=0
        k2=0
        for i in xrange(2):
            if h.count(l[i])==3:
                k1+=1
            if h.count(l[i])==2:
                k2+=1
        if k1==1 and k2==1:
            return 1
        return 0
    return 0
def flush(hand):
    h=[hand[i][1] for i in xrange(5)]
    if len(list(set(h)))==1:
        return 1
    return 0
def straight(hand):
    h=sorted([hand[i][0] for i in xrange(5)],key=v)
    if h==['2','3','4','5','A']:
        return 1
    k=values[h[0]]
    for i in xrange(1,5):
        if k+i!=values[h[i]]:
            return 0
    return 1
def threeofakind(hand):
    h=[hand[i][0] for i in xrange(5)]
    l=list(set(h))
    if len(l)==3:
        k=0
        for i in xrange(3):
            if h.count(l[i])==3:
                k+=1
        if k==1:
            return 1
        return 0
    return 0
def twopair(hand):
    h=[hand[i][0] for i in xrange(5)]
    l=list(set(h))
    if len(l)==3:
        k=0
        for i in xrange(3):
            if h.count(l[i])==2:
                k+=1
        if k==2:
            return 1
        return 0
    return 0        
def onepair(hand):
    h=[hand[i][0] for i in xrange(5)]
    l=list(set(h))
    if len(l)==4:
        return 1
    return 0
def evaluate_hand(hand):
    if straight(hand) and flush(hand):
        return 9
    if fourofakind(hand):
        return 8
    if fullhouse(hand):
        return 7
    if flush(hand):
        return 6
    if straight(hand):
        return 5
    if threeofakind(hand):
        return 4
    if twopair(hand):
        return 3
    if onepair(hand):
        return 2
    return 1
def tiebreaker(hand1,hand2,rank):
    h1=sorted([hand1[i][0] for i in xrange(5)],key=v)
    h2=sorted([hand2[i][0] for i in xrange(5)],key=v)
    if rank==9 or rank==5:
        m1=values[h1[4]]
        m2=values[h2[4]]
        if h1[4]=='A' and h1[3]=='5':
            m1=5
        if h2[4]=='A' and h2[3]=='5':
            m2=5
        if m1>m2:
            return hand1
        elif m1<m2:
            return hand2
        else:
            return "split"
    elif rank==8:
        l1=list(set(h1))
        l2=list(set(h2))
        for i in xrange(2):
            if h1.count(l1[i])==4:
                m11=values[l1[i]]
            else:
                m12=values[l1[i]]
            if h2.count(l2[i])==4:
                m21=values[l2[i]]
            else:
                m22=values[l2[i]]
        if m11>m21:
            return hand1
        elif m11<m21:
            return hand2
        else:
            if m12>m22:
                return hand1
            elif m12<m22:
                return hand2
            else:
                return "split"
    elif rank==7:
        l1=list(set(h1))
        l2=list(set(h2))
        for i in xrange(2):
            if h1.count(l1[i])==3:
                m11=values[l1[i]]
            else:
                m12=values[l1[i]]
            if h2.count(l2[i])==3:
                m21=values[l2[i]]
            else:
                m22=values[l2[i]]
        if m11>m21:
            return hand1
        elif m11<m21:
            return hand2
        else:
            if m12>m22:
                return hand1
            elif m12<m22:
                return hand2
            else:
                return "split"
    elif rank==6 or rank==1:
        m1=values[h1[4]]
        m2=values[h2[4]]
        if m1>m2:
            return hand1
        elif m1<m2:
            return hand2
        else:
            for i in xrange(3,-1,-1):
                if values[h1[i]]>values[h2[i]]:
                    return hand1
                elif values[h1[i]]<values[h2[i]]:
                    return hand2
            return "split"
    elif rank==4:
        m1=[None,None,None]
        m2=[None,None,None]
        l1=list(set(h1))
        l2=list(set(h2))
        j1=1
        j2=1
        for i in xrange(3):
            if h1.count(l1[i])==3:
                m1[0]=l1[i]
            if h1.count(l1[i])==1:
                m1[j1]=l1[i]
                j1+=1
            if h2.count(l2[i])==3:
                m2[0]=l2[i]
            if h2.count(l2[i])==1:
                m2[j2]=l2[i]
                j2+=1
        m1=list(m1[0])+sorted(m1[1:],key=v)
        m2=list(m2[0])+sorted(m2[1:],key=v)
        if values[m1[0]]>values[m2[0]]:
            return hand1
        elif values[m1[0]]<values[m2[0]]:
            return hand2
        else:
            if values[m1[1]]>values[m2[1]]:
                return hand1
            elif values[m1[1]]<values[m2[1]]:
                return hand2
            else:
                if values[m1[2]]>values[m2[2]]:
                    return hand1
                elif values[m1[2]]<values[m2[2]]:
                    return hand2
                else:
                    return "split"
    elif rank==3:
        m1=[None,None,None]
        m2=[None,None,None]
        l1=list(set(h1))
        l2=list(set(h2))
        j1=0
        j2=0
        for i in xrange(3):
            if h1.count(l1[i])==1:
                m1[2]=l1[i]
            if h1.count(l1[i])==2:
                m1[j1]=l1[i]
                j1+=1
            if h2.count(l2[i])==1:
                m2[2]=l2[i]
            if h2.count(l2[i])==2:
                m2[j2]=l2[i]
                j2+=1
        m1=sorted(m1[:2],key=v)+list(m1[2])
        m2=sorted(m2[:2],key=v)+list(m2[2])
        if values[m1[0]]>values[m2[0]]:
            return hand1
        elif values[m1[0]]<values[m2[0]]:
            return hand2
        else:
            if values[m1[1]]>values[m2[1]]:
                return hand1
            elif values[m1[1]]<values[m2[1]]:
                return hand2
            else:
                if values[m1[2]]>values[m2[2]]:
                    return hand1
                elif values[m1[2]]<values[m2[2]]:
                    return hand2
                else:
                    return "split"
    elif rank==2:
        l1=list(set(h1))
        l2=list(set(h2))
        s1=[]
        s2=[]
        for i in xrange(4):
            if h1.count(l1[i])==2:
                m1=values[l1[i]]
            if h2.count(l2[i])==2:
                m2=values[l2[i]]
            if h1.count(l1[i])==1:
                s1.append(values[l1[i]])
            if h2.count(l2[i])==1:
                s2.append(values[l2[i]])
        if m1>m2:
            return hand1
        elif m1<m2:
            return hand2
        else:
            s1=sorted(s1)
            s2=sorted(s2)
            for i in xrange(2,-1,-1):
                if s1[i]>s2[i]:
                    return hand1
                elif s1[i]<s2[i]:
                    return hand2
            return "split"
def better_hand(hand1,hand2):
    r1=evaluate_hand(hand1)
    r2=evaluate_hand(hand2)
    if r1>r2:
        return hand1
    elif r2>r1:
        return hand2
    else:
        return tiebreaker(hand1,hand2,r1)
        
def get_best_hand(hand,h):
    p=list(itertools.combinations(hand+h,5))
    maxi=list(p[0])
    for i in xrange(1,len(p)):
        b=better_hand(maxi,list(p[i]))
        if b!="split" and b!=maxi:
            maxi=b
    return maxi        
suit=['c','d','h','s']
deck=[]
for r in values.keys():
    for s in suit:
        deck.append(r+s)
hand1=['Jh','4c']
hand2=['Qc','Td']
deck.remove(hand1[0])
deck.remove(hand1[1])
deck.remove(hand2[0])
deck.remove(hand2[1])
list_of_hands=list(itertools.combinations(deck,5))
winsofhand1=0
winsofhand2=0
split=0
for j in xrange(1000):
    i=random.randint(0,len(list_of_hands)-1)
    h1=get_best_hand(list(list_of_hands[i]),hand1)
    h2=get_best_hand(list(list_of_hands[i]),hand2)
    res=better_hand(h1,h2)
    if res==h1:
        winsofhand1+=1
    elif res==h2:
        winsofhand2+=1
    else:
        split+=1
s=winsofhand1+winsofhand2+split
print "Hand1= ",hand1
print "Hand2= ",hand2
print "Winning percentage of ",hand1,":-",(winsofhand1+0.0)*100/s
print "Winning percentage of ",hand2,":-",(winsofhand2+0.0)*100/s
print "split",(split+0.0)*100/s

print
flop=random.sample(deck,3)
print "Flop",flop
for f in flop:
    deck.remove(f)
list_of_hands=list(itertools.combinations(deck,2))
winsofhand1=winsofhand2=split=0
for j in xrange(len(list_of_hands)):
    h1=get_best_hand(list(list_of_hands[j])+flop,hand1)
    h2=get_best_hand(list(list_of_hands[j])+flop,hand2)
    res=better_hand(h1,h2)
    if res==h1:
        winsofhand1+=1
    elif res==h2:
        winsofhand2+=1
    else:
        split+=1
s=winsofhand1+winsofhand2+split
print "Hand1= ",hand1
print "Hand2= ",hand2
print "Winning percentage of ",hand1,":-",(winsofhand1+0.0)*100/s
print "Winning percentage of ",hand2,":-",(winsofhand2+0.0)*100/s
print "split",(split+0.0)*100/s

print
turn=random.sample(deck,1)
print "Turn",turn
print "Hand",flop+turn
deck.remove(turn[0])
list_of_hands=deck
winsofhand1=winsofhand2=split=0
for j in xrange(len(list_of_hands)):
    h1=get_best_hand([list_of_hands[j]]+flop+turn,hand1)
    h2=get_best_hand([list_of_hands[j]]+flop+turn,hand2)
    res=better_hand(h1,h2)
    if res==h1:
        winsofhand1+=1
    elif res==h2:
        winsofhand2+=1
    else:
        split+=1
s=winsofhand1+winsofhand2+split
print "Hand1= ",hand1
print "Hand2= ",hand2
print "Winning percentage of ",hand1,":-",(winsofhand1+0.0)*100/s
print "Winning percentage of ",hand2,":-",(winsofhand2+0.0)*100/s
print "split",(split+0.0)*100/s

print
river=random.sample(deck,1)
print "River",river
print "Hand",flop+turn+river
deck.remove(river[0])
list_of_hands=deck
winsofhand1=winsofhand2=split=0
h1=get_best_hand(flop+turn+river,hand1)
h2=get_best_hand(flop+turn+river,hand2)
res=better_hand(h1,h2)
if res==h1:
    winsofhand1+=1
elif res==h2:
    winsofhand2+=1
else:
    split+=1
s=winsofhand1+winsofhand2+split
print "Hand1= ",hand1
print "Hand2= ",hand2
print "Winning percentage of ",hand1,":-",(winsofhand1+0.0)*100/s
print "Winning percentage of ",hand2,":-",(winsofhand2+0.0)*100/s
print "split",(split+0.0)*100/s
