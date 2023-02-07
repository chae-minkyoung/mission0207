def dequeue():
    global size, front, rear, queue
    if rear == front:
        print("비엇습니다")
        return
    data=queue[0]
    for i in range(1,size):
        queue[i-1]=queue[i]
        queue[i]=None
    rear-=1
    print(f'{data} 님 식당에 들어감')
def enqueue(data):
    global size, front, rear, queue
    if rear==size-1:
        print("꽉찼습니다.")
        return
    rear+=1
    queue[rear]=data

if __name__ == "__main__":
    rear,front=-1,-1
    size=5
    queue=[None for _ in range(size)]
    customers= ['정국','뷔','지민','진','슈가']
    for customer in customers:
        enqueue(customer)
    for _ in range(size):
        print(f'대기줄 상태 : {queue}')
        dequeue()
    print(f'대기줄 상태 : {queue}')
    print('식당 영업 종료!')








