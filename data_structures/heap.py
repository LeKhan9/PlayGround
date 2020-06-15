import heapq

class NumberHeap():
    def __init__(self, arr=None, is_max_heap=False):
        self.arr = arr or []
        self.is_max_heap = is_max_heap

        if self.is_max_heap:
            self.arr = [val * -1 for val in self.arr]

        if self.arr:
            heapq.heapify(self.arr)


    def push(self, itm):
        if self.is_max_heap:
            itm = itm * -1

        heapq.heappush(self.arr, itm)

    def pop(self):
        itm = heapq.heappop(self.arr)

        if self.is_max_heap:
            itm = -1 * itm

        return itm

    def get_top_n_items(self, n):
        if n > len(self.arr):
            n = len(self.arr)

        return [self.pop() for _ in range(n)]


    def __len__(self):
        return len(self.arr)
