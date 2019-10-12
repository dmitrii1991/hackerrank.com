string = input()

def work(string):
    data = ['(', ')', '{', '}', '[', ']']
    data_end = {'(': ')', '{': '}', '[': ']'}
    bracket = []
    end = None
    
    for i, letter in enumerate(string):
        if letter in data[::2]:
            end = (data_end[letter], i)
            bracket.append(end)       
        elif letter in data[1::2]:
            if end is None or letter != end[0]:
                return i + 1 # вывод ошибки
            else:
                del bracket[-1]
                end = bracket[-1] if bracket else None   
    if bracket:
        return bracket[-1][1] + 1
    return 'Success'
    
print(work(string)
