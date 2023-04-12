def solution(commands):
    answer = []
    info = dict()           # info[(r, c)][0] = parent of (r, c)
                            # info[(r, c)][1] = children of (r, c) only if (r, c) is parent else empty list
    value = [['' for _ in range(51)] for _ in range(51)]
    for i in range(1,51):
        for j in range(1,51):
            info[(i, j)] = [(i,j), []]
    
    def update_1(r, c, value1):
        parent = info[(r,c)][0]
        value[parent[0]][parent[1]] = value1
    
    def update_2(value1, value2):
        for i in range(1,51):
            for j in range(1,51):
                if value[i][j] == value1:
                    value[i][j] = value2
    
    def merge(r1,c1,r2,c2):
        if (r1, c1) == (r2, c2):
            return
        
        p1 = info[(r1,c1)][0]
        p2 = info[(r2,c2)][0]
        if (p1[0], p1[1]) == (p2[0], p2[1]):
            return
        
        parent_merge(p1, p2)
    
    def unmerge(r, c):
        # 2. 부모의 자식 -> 같은 set 들 모두 각자 자신을 부모로 만듦 (unmerge)
        # 3. 각 value는 없앰(부모만 value 남아있을 것 이다.)
        # 1. value r, c에 할당
        parent = info[(r,c)][0]
        val = value[parent[0]][parent[1]]
        value[parent[0]][parent[1]] = ''
        for child in info[(parent[0],parent[1])][1]:
            info[(child[0],child[1])][0] = (child[0], child[1])
        
        info[(parent[0], parent[1])][1] = []
        value[r][c] = val
    
    def parent_merge(Parent, Child):
        # 1. value update
        v1 = value[Parent[0]][Parent[1]]
        v2 = value[Child[0]][Child[1]]
        if v1 == '':
            value[Parent[0]][Parent[1]] = v2
        value[Child[0]][Child[1]] = ''
        
        # 2. info update
        info[(Child[0],Child[1])][0] = (Parent[0], Parent[1])
        for child in info[(Child[0], Child[1])][1]:
            info[(child[0], child[1])][0] = (Parent[0], Parent[1])
        
        info[(Parent[0],Parent[1])][1].append((Child[0], Child[1]))
        info[(Parent[0],Parent[1])][1].extend(info[(Child[0],Child[1])][1])
        info[(Child[0],Child[1])][1] = []
        
        
    def my_print(r, c):
        parent = info[(r,c)][0]
        v = value[parent[0]][parent[1]]
        if v == '':
            answer.append("EMPTY")
        else:
            answer.append(v)
    
    for cmd in commands:
        cmd_list = list(cmd.split())
        if len(cmd_list) == 4:
            update_1(int(cmd_list[1]), int(cmd_list[2]), cmd_list[3])
        
        elif len(cmd_list) == 5:
            merge(int(cmd_list[1]), int(cmd_list[2]), int(cmd_list[3]), int(cmd_list[4]))
        
        else:
            if cmd_list[0] == "UPDATE":
                update_2(cmd_list[1], cmd_list[2])
            elif cmd_list[0] == "UNMERGE":
                unmerge(int(cmd_list[1]), int(cmd_list[2]))
            else:
                my_print(int(cmd_list[1]), int(cmd_list[2]))
                
        print("cmd :", cmd)
        print("info 1, 4")
        print(info[(1,4)])
        # for i in range(1,5):
        #     print(*value[i])
        # print()
        
        
    
    return answer