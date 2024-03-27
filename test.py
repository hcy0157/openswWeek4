#0 : stu, 1: nam, 2~4, 5:sum 6:ave
slist = [[],[],[],[],[]]

def get_info(scout):
    stu_number = input("학번 :")
    slist[scout].append(stu_number)
    stu_name = input("이름 :")
    slist[scout].append(stu_name)
    eng = int(input("영어 점수 : "))
    slist[scout].append(eng)
    c_lan = int(input("C-언어 : "))
    slist[scout].append(c_lan)
    py_lan = int(input("파이썬 : ")) 
    slist[scout].append(py_lan)
    sum = eng+c_lan+py_lan
    slist[scout].append(sum)
    ave = sum/3
    slist[scout].append(ave)
    
def grade(count):
    if(slist[count][6] >= 90):
        slist[count].append("A") 
    elif(slist[count][6] >= 80):
        slist[count].append("B") 
    elif(slist[count][6] >= 70):
        slist[count].append("C") 
    elif(slist[count][6] >= 60):
        slist[count].append("D")
    else:
         slist[count].append("F")
    
def order(count):
    for i in range(0, count-1):
        t = i
        for j in range(1, count):
            if(slist[t][6]<slist[j][6]):
                t = j
        slist[i],slist[t] = slist[t], slist[i]

def pla(count):
    for i in range(count):
        if (i==0):
            slist[i].append(1)
        elif(slist[i][5] == slist[i-1][5]):
            slist[i].append(slist[i-1][8])
        else:
            slist[i].append(i+1)

def print_out(count):
    print(slist[count][0],"\t", slist[count][1], "\t  %3d " %slist[count][2], " %3d " %slist[count][3], " %3d " %slist[count][4] , " %3d " %slist[count][5], " %.2f " %slist[count][6], " %c " %slist[count][7], " %2d " %slist[count][8] )

member = 5 #학생 수
for i in range(member):
    get_info(i)
    grade(i)

order(member)
pla(member)

print("\n       성적관리 프로그램\n")
print("==="*20)
print("학번 \t 이름 \t 영어  C-언어  파이썬  총점  평균  학점  등수")
print("==="*20)
for i in range(member):
    print_out(i)





