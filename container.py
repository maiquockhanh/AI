try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q


class PriorityQueue:
    def __init__(self):
        self.PQ = Q.PriorityQueue()

    def empty(self):
        return self.PQ.empty()

    def push(self, node):
        self.PQ.put(node)

    def push_update(self, node):  # Push and update cost if new cost smaller than old cost
        duplicate = False
        tmp_Q = Q.PriorityQueue()

        for i in range(self.PQ.qsize()):
            item = self.PQ.get()
            tmp_Q.put(item)

        for i in range(tmp_Q.qsize()):
            item = tmp_Q.get()
            if item[1] == node[1]:
                duplicate = True
                if item[0] > node[0]:
                    self.PQ.put(node)
                else:
                    self.PQ.put(item)
            else:
                self.PQ.put(item)

        if not duplicate:
            self.PQ.put(node)

    def pop(self):
        return self.PQ.get()
