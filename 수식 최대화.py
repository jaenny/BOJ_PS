from itertools import permutations

def solution(expression):
    answer = 0
    
    #연산자 우선순위
    priority = [('+', '-', '*'), ('+', '*', '-'), ('-', '+', '*'), ('-', '*', '+'), ('*', '+', '-'), 
('*', '-', '+')]

    #숫자와 연산자 분리
    calculation = []
    for s in expression :
        if s in '+-*' : 
            expression=expression.replace(s,' ')
            calculation.append(s)
    expre = expression.split()

    #최대 answer 구하기
    for pr in priority : #연산자 우선순위 모음에서 하나씩 가져오고
        later = expre.copy()
        cal = calculation.copy()
        for p in pr : #+,-,* 하나씩 가져오면서
            ex = later
            if p in cal : 
                for k in range(cal.count(p)) :
                    i = cal.index(p)
                    if p == '+' : 
                        later[i] = int(ex[i])+int(ex[i+1])
                        later[i+1] = "remove"
                    elif p == '-' :
                        later[i] = int(ex[i])-int(ex[i+1])
                        later[i+1] = "remove"
                    else :
                        later[i] = int(ex[i])*int(ex[i+1])
                        later[i+1] = "remove"
                    later.remove("remove"); cal.remove(p)
        if answer < abs(later[0]) : answer = abs(later[0])
    return answer