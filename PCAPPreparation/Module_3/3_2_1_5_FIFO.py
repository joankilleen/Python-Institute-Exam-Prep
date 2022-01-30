import traceback


class QueueError(Exception):  # Choose base class for the new exception.
    def __init__(self, message):
        super().__init__(message)


class Queue:
    def __init__(self):
        self.__stk = []

    def put(self, elem):
        self.__stk.append(elem)

    def get(self):
        if len(self.__stk) == 0:
            raise QueueError("Cannot 'get' on an empty queue!")
        val = self.__stk[0]
        self.__stk.pop(0)
        return val

    def get_length(self):
        return len(self.__stk)

    def get_stack(self):
        return self.__stk


class SuperQueue(Queue):

    def isempty(self):
        return len(self.get_stack()) == 0


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")

print(que.__dict__)
internal_dict = que.__dict__
que.__dict__['_Queue__stk'] = 'Test'
print(que.__dict__)
