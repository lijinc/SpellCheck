__author__ = 'LIJIN'


def editDistance(text1, text2):
    return _editDistance(text1,text2,len(text1),len(text2))

def _editDistance(text1,text2,n1,n2):
    data=[]
    for i in range(0,n1+1):
        data.append([0]*(n2+1))
    for i in range(0,n1+1):
        data[i][0]=i
    for j in range(0,n2+1):
       data[0][j]=j
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            sub=data[i-1][j-1]
            if text1[i-1]!=text2[j-1]:
                sub=sub+1
            data[i][j]=min(sub,data[i][j-1]+1,data[i-1][j]+1)
    return data[n1][n2]

