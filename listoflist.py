#Nama               : Ayyub Al Anshor
#NIM                : 24060122130054
#ListofList

P=['a','b','c','d']
Q=['a','c','e','g','i',['b','d','f','h']]
R=['a','b','c','d',['c','e','g','i']]
S=[]

def Isempty(L):
    return L==[]

def Tail(L):
    return L[1:]

def NbElm(L):
    if (Isempty(L)):
        return 0
    else:
        return 1 + NbElm(Tail(L))

def IsAtom(S):
    return type (S)==list 
       
def IsList(S):
    if type (S)==int:
        return False
    else:
        return 

def KonsLo(L,S):
    return L+S

def KonsL(S,L):
    return S+L

def First(S):
    if Isempty(S):
        return []
    else:
        return S[0]

def Head(S):
    return S[:-1]

def IsEqS(S1,S2):
    if Isempty(S1)and Isempty(S2):
        return True
    elif not Isempty(S1)and Isempty(S2):
        return False
    elif not Isempty(S1)and not Isempty(S2):
        if IsAtom(First(S1))and IsAtom(First(S2)):
            return First(S1)==First(S2)and IsEqS(Tail(S1),Tail(S2))
        elif IsList(First(S1)and IsList(First(S2))):
            return IsEqS(First(S1),First(S2))and IsEqS(Tail(S1),Tail(S2))
        else:
            return False

def IsMemberS(P,S):
    if(Isempty(S)):
        return False
    elif not Isempty(S):
        if IsAtom(First(S)):
            return P==First(S)
        elif IsList(First(S)):
            return IsMemberS(P, First(S)) or IsMemberS(P, Tail(S))

def Rember(a,S):
    if Isempty(S):
        return S
    elif  IsList(First(S)):
        return KonsLo (Rember(a,First(S)), Rember(a,Tail(S)))
    else :
        if First(S) == a:
            return Rember(a,Tail(S))
        else :
            return KonsLo (First(S),Rember(a,Tail(S)))

def Max2(a,b):
    if a>=b:
        return a
    else :
        b
def Max(S):
    if IsAtom(First(S)):
        return First(S)
    elif not IsAtom(First(S)):
        return Max(First(S))
    elif IsAtom(First(S)):
        return Max2(First(S),Max(Tail(S)))
    else :
        return Max2(Max(First(S),Max(Tail(S))))     
    


