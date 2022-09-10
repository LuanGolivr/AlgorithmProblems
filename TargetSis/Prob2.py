def solution(value):
    caching  = {0: 0, 1:1}
    idx = 2

    if value in caching:
        return "O numero {} pertence a sequência".format(value)
    
    while True:
        caching[idx] = caching[idx - 1] + caching[idx - 2]
        if caching[idx] > value:
            return "O numero {} não pertence a sequência.".formart(value)
        
        if caching[idx] == value:
            return "O numero {} pertence a sequência".format(value)
        
        idx += 1



number = int(input("Insert a number: "))
print(solution(number))