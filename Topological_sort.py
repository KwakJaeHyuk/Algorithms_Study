def Topological_Sort(graph):
    N = len(graph) # dictionary의 key값의 개수
    stack = [] # 빈 리스트
    visited = [0 for _ in range(N)] # 배역안에 for문 동작

    for i in graph: # 이 for문은 graph dictionary의 key들의 개수를 사용
        if visited[i] == 0:
            DFS(i, stack, visited)
            
    answer = []                     ### 이 과정은 stack에 값이 잘 쌓아졌을 때 answer 리스트에 값을 pop해주는 과정이다.
    while len(stack) != 0:
        answer.append(stack.pop())
    print("최종 답: ", answer)
    
def DFS(v, stack, visited):
    visited[v] = 1
    for i in graph[v]: # dictionary로 선언된 graph이고 graph의 배열의 인덱스들은 key를 뜻하는 것이다.
        if visited[i] == 0: 
            DFS(i, stack, visited)
    stack.append(v) # stack에 값들을 append 해주는 과정


graph = {0: [1, 2, 3], 
         1: [4], 
         2: [4, 5], 
         3: [], 
         4: [6], 
         5: [1], 
         6: []}

Topological_Sort(graph)