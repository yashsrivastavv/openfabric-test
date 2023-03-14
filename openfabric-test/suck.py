inp='9@a42&516'
count=0
global num 
def follow_odd(inp):
    num=''
    for i in range(len(inp)):
        if inp[i].isnumeric() :
            num+=inp[i]
    # print(num)
    ev=''
    od=''
    for i in range(len(num)):
        g=int(num[i])
        if g%2==0:
            ev+=str(g)
        else:
            od+=str(g)
    # print(ev,od)
    final=''
    for i in range(len(ev)):
        final+=ev[i]
        final+=od[i]
    print(final)


def follow_even(inp):
    n=''
    for i in range(len(inp)):
        if inp[i].isnumeric() :
            n+=inp[i]
    print(n)
    ev=''
    od=''
    for i in range(len(n)):
        g=int(n[i])
        if g%2==0:
            ev+=str(g)
        else:
            od+=str(g)
    # print(ev,od)
    final=''
    for i in range(len(ev)):
        final+=od[i]
        final+=ev[i]
    print(final)


for i in range(len(inp)):
    if inp[i].isalnum():
        pass
    else:
        count+=1
# print(count)

if count%2==0:
    follow_odd(inp)
else:
    follow_even(inp)