inp = {"rhdt":246,"ghdt":1246}
def left_rotate(inp1):

    k=inp[1:]+inp[:1]


    print(k)

def rot(inp1):
    k=inp[-1:]+inp[-2:-1]+inp[:-2]
    print(k)

for i,j in inp.items():
    # print(j)
    su=0
    j=str(j)
    inp1=i
    for i in range(len(str(j))):
        su+= int(j[i])**2
    # print(su)
    if su%2==0:
        print(left_rotate(inp1))
    else:
        print(rot(inp1))
    


