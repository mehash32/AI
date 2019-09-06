# initial
im = 3
ic = 3
#final
fm =0
fc =0
#side
status = 0
#boat current locatiion
flag = 0
#boat grouping
select = 0
print("  ", fc)
def display(bpass1,bpass2):
    global fm
    global fc
    print("\n\n\n")
    for i in range(0,fm):
        print(" M ")
    for i in range (0,fc):
        print(" C ")
    if flag == 0:
        print("    ~~~~~WATER~~~~~<B0(",bpass1,",", bpass2,")AT >   ")
    else:
        print("        <BO(",bpass1,",", bpass2,")AT ~~~~~WATER~~~~~  ")
    for i in range (0,im):
        print(" M ", end = '')
    for i in range (0,ic):
        print(" C ", end = '')

def win():
    t = fc==3 and fm ==3
    return t

def solution():
    global  ic
    global im
    global fm
    global fc
    while win():
        if flag==0:
            if select ==1:
                display('C',' ')
                ic+=1
                break
            if select ==2:
                display('C','M')
                ic+=1
                im+=1
                break
            if (im-2 >ic and fm+2 >=fc) or (im-2) ==0:
                im = im -2
                select =1
                display('M',"M")
                flag = 1
            elif (ic-2<im and fm ==0 ) or (fc+2 <= fm or im == 0):
                ic = ic -2
                select =2
                display('C','C')
                flag = 1
            elif (ic -1 <= im -1)and (fm+1 > fc+1):
                ic = ic -1
                im = im -1
                select = 3
                display('M','C')
                flag = 1
            else:
                if select == 1:
                    display('M','M')
                    fm = fm+2
                    break
                if select ==2:
                    display('C','C')
                    fc = fc+2
                    break
                if select ==3:
                    display('M','C')
                    fc = fc=1
                    fm = fm +1
                    break
                if win():
                    if (fc > 1 and fm == 0 ) or im ==0:
                        fc = fc-1
                        select =1
                        display('C',' ')
                        flag =0
                    elif ic+2 >im:
                        fc = fc-1
                        fm = fm-1
                        select =2
                        display('C','M')
                        flag =0

print("MISSIONARIES AND CANNIBAL SOLUTION")
display(' ', ' ')
solution()
display(' ',' ')




