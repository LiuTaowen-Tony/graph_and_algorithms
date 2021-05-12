import math

class MaxHeap:

    def __init__(self, length : int):
        self.raw_data = [(0, None)] * length
        self.next_pos = 0
    
    def __len__(self) -> int:
        return self.next_pos

    def __get_key(self, position : int) -> int:
        if position < self.next_pos:
            return self.raw_data[position][0]
        else:
            return -1

    def __swap(self, position1 : int , position2 : int):
        self.raw_data[position1], self.raw_data[position2] = (
                self.raw_data[position2], self.raw_data[position1]
            )
    
    def __r_pos(self, position : int) -> int:
        return position * 2 + 2

    def __l_pos(self, position : int) -> int:
        return position * 2 + 1

    def __percolate_up(self, position : int):
        if position == 0:
            return
        parent_position = math.floor((position - 1) / 2)
        if (self.__get_key(parent_position) < self.__get_key(position)):
            self.__swap(parent_position, position)
            self.__percolate_up(parent_position)

    def __fix_max_heap(self, position : int):
        # pre : position is a valid position
        r_pos = self.__r_pos(position)
        l_pos = self.__l_pos(position)
        r_key = self.__get_key(r_pos)
        l_key = self.__get_key(l_pos)

        if r_key > l_key and r_key > self.__get_key(position):
            self.__swap(position, r_pos)
            self.__fix_max_heap(r_pos)
        elif l_key > r_key and l_key > self.__get_key(position):
            self.__swap(position, r_pos) 
            self.__fix_max_heap(l_pos)

    def __build_max_heap(self, position : int):
        # O(n) rather than O(nlogn) (using add for n times)
        r_pos = self.__r_pos(position)
        l_pos = self.__l_pos(position)
        if l_pos < self.next_pos: # parent is not a leaf
            self.__build_max_heap(l_pos)
            if r_pos < self.next_pos: # right sub heap exist
                self.__build_max_heap(r_pos)
            self.__fix_max_heap(position)

    def add(self, item : Any, priority : int):
        # pre : priority >= 0
        element = (priority, item)
        if self.next_pos == len(self.raw_data):
            self.raw_data.append(element)
        else:
            self.raw_data[next_pos] = element
        self.next_pos += 1
        self.__percolate_up(self.next_pos)

    def poll(self) -> Any:
        self.__swap(0, self.next_pos)
        output = self.raw_data[self.next_pos][1] # item
        self.next_pos -= 1
        self.__fix_max_heap(0)
        return output

    @staticmethod
    def from_list(lst : list[int, Any]):
        max_heap = MaxHeap(0)
        max_heap.raw_data = lst[:]
        max_heap.position = len(lst)
        max_heap.__build_max_heap(0)
        return max_heap

    @staticmethod
    def heap_sort_ascending(lst : list[int]) -> list[int]:
        nlst = [(i, i) for i in lst]
        max_heap = MaxHeap.from_list(nlst)
        max_heap.__in_place_sort()
        nlst = [item for (priority, item) in max_heap.raw_data]
        return nlst

    def __in_place_sort(self):
        while(self.next_pos > 0):
            self.__swap(0, self.next_pos)
            self.next_pos -= 1
            self.__fix_max_heap(0)

    def to_ascending_list(self) -> list[Any]:
        nlst = []
        while(self.next_pos > 0):
            nlst.append(self.poll)
