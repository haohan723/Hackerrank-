if __name__ == '__main__':
    N = int(input())

lt = []
for i in range(0,N):
    command_line = input().split(' ')
    command = command_line[0]
#print(int(command_line[1])

    if command == 'print':
        print(lt)
    elif command == 'insert':
        lt.insert(int(command_line[1]), int(command_line[2]))
    elif command == 'remove':
        lt.remove(int(command_line[1]))
    elif command == 'append':
        lt.append(int(command_line[1]))
    elif command == 'sort':
        lt.sort()   
    elif command == 'pop':
        lt.pop()
    elif command == 'reverse':
        lt.reverse()        
    elif command == 'count':
        lt.count(int(command_line[1]))
     
