import random
from timeit import default_timer as timer


class Node(object):
    def __init__(self, key, parent):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent # 삭제를 하기 위해서는 부모가 누군지 알아야 한다.(결국 삭제를 한다는 것은 자식의 자리를 바꾼다는 의미이기 때문)
        
def insert(node, key):
    if node is None:
        node = Node(key, node)
    elif key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

def search(node, key):
    if node is None or node.key == key:
        return node
    if key < node.key:
        return search(node.left, key)
    
    return search(node.right, key)

def delete(value, node):
    
    # node = Node(root, node.parent)
       
    # print(type(node.parent))
    # print(type(node.left))
    if value == node.key:
        node = DELETE_NODE(node)
    
    
    # val = node.key 과정이 필요
    # -1, None
    #
    #
    #
    elif value == node.parent.left:
        node.parent.left = DELETE_NODE(node)
        # 부모 -> 자식
        # 자식 -> 부모
        temp = DELETE_NODE(node) # 이어줄 노드를 찾음
        node.parent.left = temp
        temp.paranet = node
    
    
    else:
        value.parent.right = DELETE_NODE(node)
        
        
    return node
        
def DELETE_NODE(node):
    if node.left == None and node.right == None:
        return None
    
    elif node.left != None and node.right == None:
        return node.left
    
    elif node.right != None and node.left == None:
        return node.right
    
    else: # 크기가 바로 다음인 노드를 찾는다. 따라서 오른쪽에 있는 노드들 중에 제일 작은 노드를 찾는다.
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
    root = insert(root, i)

start = timer()
found = search(root, value)


print(timer() - start)

if found is not None:
    print('value', value, 'found', found.key)
    print(True if found.key == value else False)

        
node = delete(value, root) # delete된 이후에도 같은 위치의 노드를 출력했을 때 같은 값이 나오는 지 확인
if found is not None:
    print('value', value, 'found', found.key)
    print(True if found.key == value else False)
    