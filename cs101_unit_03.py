#days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31]
#def how_many_days(month):
#    return  days_in_month[month-1]
#
#
#
#
#countries=[['China','Beijing',1350.],['India','Delhi',1210.],['Romania','Bucharest',21.],
#        ['United states','Washington',307.]]
#a=countries[2][2]
#b=countries[0][2]
#c=b/a
#
#
#stooges=['Moe','Larry','Curly']
#stooges[2]='shemp'
#
#
#
#p=[1,2,3]
#q=p
#
#p=['Osama','Ghufran phupa']
#
#
#
def replace_spy(a):
    a[2]=a[2]+1
    return a







def sum_list(q):
    result=0
    for e in q:
       result=result+e 
    return result 



def find_element(p,a):
    for idx, e in enumerate(p):
        if e==a:
            return idx
    return -1

input_list=["osama","ghufran phupa","nouman"]
target="ghufran phupa"
print find_element(input_list,target)
print list( enumerate(input_list))






def finds_element(p,a):
    if a in p:
        return p.index(a)
    else:
        -1


