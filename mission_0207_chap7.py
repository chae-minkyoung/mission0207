import random
def enqueue(data):
    global size, queue, front, rear,count

    if (rear+1)%size == front:
        print("꽉 찼음.")
        return
    rear=(rear+1)%size
    queue[rear]=data
    count+=data[1]
    print(f'귀하의 대기 시간은 {count}분 입니다.')

def dequeue():
    global size,queue,front,rear,count

    if front==rear:
        print("비었음")
        return
    front=(front+1)%size
    data=queue[front]
    queue[front]=None
    count-=data[1]
    print(f'귀하의 대기 시간은 {count}분 입니다.')
    return data

if __name__=="__main__":
    size = 6
    queue = [None for _ in range(size)]
    front, rear = 0,0
    customers=[]
    count=0
    for _ in range(size-1):
        enqueue((random.choice([('사용',9),('고장',3),('환불',4),('기타',1)])))
        print(queue)


