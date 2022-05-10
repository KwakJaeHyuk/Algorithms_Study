import random
from timeit import default_timer as timer


class Node(object):
    def __init__(self, key, parent):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent # 삭제를 하기 위해서는 부모가 누군지 알아야 한다.(결국 삭제를 한다는 것은 자식의 자리를 바꾼다는 의미이기 때문)
        
def insert(node, key, parent): # 각각의 노드들에 key값과 parent값들이 다 포함되어 있다.
    if node is None:
        node = Node(key, parent)    
            
        return node
    
    elif key < node.key:
        node.left = insert(node.left, key, node)
        
    elif key > node.key:
        node.right = insert(node.right, key, node)
        
    return node # root 노드 반환

def search(node, key):
    if node is None or node.key == key:
        return node
    if key < node.key:
        return search(node.left, key)
    else:
        return search(node.right, key)

def delete(root, val):
    
    # root:Node, val:int
    found = search(root, val)

    # 없는 경우
    if not found:
        print("삭제할 값이 트리에 없습니다!!")
    
    else:
        # 있는 경우
        if found == root:
            root = DELETE_NODE(found)
            
        elif found == found.parent.left:
            found.parent.left = DELETE_NODE(found)
            
        else:
            found.parent.right = DELETE_NODE(found)
                
        
def DELETE_NODE(node): # 바껴서 들어갈 노드
    if node.left == None and node.right == None:
        return None
    elif node.left != None and node.right == None:
        return node.left
    elif node.right != None and node.left == None:
        return node.right
    else: 
        s = node.right               
        while s.left != None:
            parent = s
            s = s.left
        node.key = s.key
        if s == node.right:
            node.right = s.right
        else:
            parent.left = s.right
        return node
    
    
x = random.sample(range(5000), 1000)
value = x[800]

root = None
for i in x:
    root = insert(root, i, None) # 처음 입력되는 parent값은 None으로 입력

start = timer()
found = search(root, value) # value값의 노드 정보

print(timer() - start)

if found is not None:
    print('value', value, 'found', found.key)
    print(True if found.key == value else False)

      
delete(root, value) # delete된 이후에도 같은 위치의 노드를 출력했을 때 같은 값이 나오는 지 확인

found = search(root, value)
print(found)

