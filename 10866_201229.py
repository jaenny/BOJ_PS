import sys
def push_front(x) :
  deque.insert(0,x)

def push_back(x) :
  deque[len(deque):len(deque)] = [x]

def empty() :
  if len(deque) == 0 :
    return 1
  else :
    return 0

def pop_front() : 
  global deque
  if empty() == 1 :
    print(-1)
  else :
    print(deque[0])
    deque = deque[1::]

def pop_back() : 
  global deque
  if empty() == 1 :
    print(-1)
  else :
    print(deque[-1])
    deque = deque[:-1]

def size() :
  print(len(deque))

def front() :
  if empty() == 1 :
    print(-1)
  else : print(deque[0])

def back() :
  if empty() == 1:
    print(-1)
  else : print(deque[-1])

order = int(sys.stdin.readline())
deque=[]
L=[]
for i in range(order) :
  L=[x for x in sys.stdin.readline().split()]
  if L[0] == 'push_front' :
    push_front(L[1])
  elif L[0] == 'push_back' :
    push_back(L[1])
  elif L[0] == 'pop_front' :
    pop_front()
  elif L[0] == 'pop_back' :
    pop_back()
  elif L[0] == 'size' :
    size()
  elif L[0] == 'empty' :
    print(empty())
  elif L[0] == 'front' :
    front()
  elif L[0] == 'back' :
    back()