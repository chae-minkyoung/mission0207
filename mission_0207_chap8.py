import random
class tree_node():
    left=None
    right=None
    data=None
def preorder(node):
    if node == None:
        return
    print(node.data,end=' ')
    preorder(node.left)
    preorder(node.right)

if __name__=="__main__":
    sells=['레쓰비캔커피','도시락','삼각김밥','코카콜라','삼다수','츄파춥스']
    sells1=[random.choice(sells) for _ in range(20)]
    print('오늘 판매된 물건(중복O)-->',end=' ')
    for i in sells1:
        print(i,end=' ')
    print()
    node1=tree_node()
    root=node1
    node1.data=sells1[0]

    current=root
    for sell in sells1[1:]:
        current = root
        node=tree_node()
        node.data=sell
        while(True):
            if node.data<current.data:
                if current.left==None:
                    current.left=node
                else:
                    current=current.left
            elif node.data>current.data:
                if current.right==None:
                    current.right=node
                else:
                    current=current.right
            else:
                break
    print("오늘 판매된 물건(중복X)-->",end=' ')
    preorder(node1)



