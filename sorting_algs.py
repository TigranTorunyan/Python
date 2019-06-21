class SortList:
    sorting_algorithms = {
        'bubble':buble_sort,
        'insertion':insertion_sort,
        'merge':merge_sort,
        'quick':quick_sort
    }
    
    def __init__(self, cont: list):
        self.cont = cont


    def bubble_sort(self):
        length = len(self.cont)
        for i in range(length):
            for j in range(length - 1):
               if self.cont[j] > slef.cont[j+1]:
                   self.cont[j], self.cont[j+1] = self.cont[j+1], self.cont[j]
        return self.cont

 
    def insertion_sort(self):
        length = len(self.cont)
        for idx in range(1, length):
            while 0 < idx and self.cont[idx] < self.cont[idx - 1]:
                self.cont[j], self.cont[j-1] = self.cont[j-1], self.cont[j]
                idx -= 1
        return self.cont


    def merge_sort(self):
        if len(self.cont) > 1:
            mid = len(self.cont)//2
            L = self.cont[:mid]
            R = self.cont[mid:]
            
            merge_sort(L)
            merge_sort(R)

            i = j = k = 0
            
            while i < len(L) and j < len(R)
                if L[i] < R[j]:
                    self.cont[k] = L[i]
                    i += 1
                else:
                    self.cont[k] = R[j]
                    j += 1
                k += 1
            
             while i < len(L):
                 self.cont[k] = L[i]
                 i += 1
                 k += 1

             while j < len(R):
                 self.cont[k] = R[j]
                 j += 1
                 k += 1
        return self.cont

    
    def quick_sort(self):
        less = []
        equal = []
        greater = []

        if len(array) > 1:
            pivot = array[0]
            for x in array:
                if x < pivot:
                    less.append(x)
                elif x == pivot:
                    equal.append(x)
                elif x > pivot:
                    greater.append(x)
            return quick_sort(less) + equal + quick_sort(greater)  
        else: 
            return array
    
    def sorting(self, algm: str):
        return sorting_algorithms.get(algm) 


if __name__ == '__main__':
    exp = SortList([45,1,3,7,6,59,42,22,11,6])
    exp.sorting('merge')
    print(exp)
    ex = SortList([45,1,3,7,6,22,11,9])
    ex.sorting('bubble')
    print(ex)
    p = SortList([1,3,7,6,59,42,22,11,6])
    p.sorting('quick')
    print(p)
    e = SortList([15,45,1,3,7,6,59,42,22,11,6])
    e.sorting('insertion') 
    print(e)      
