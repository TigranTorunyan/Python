class SortList:
    
   # sorting_algorithms = {'bubble':bubble_sort, 'insertion': insertion_sort, 'merge': merge_sort, 'quick': quick_sort}
    
    def __init__(self, cont: list):
        self.cont = cont


    def bubble_sort(self):
        length = len(self.cont)
        for i in range(length):
            for j in range(length - 1):
               if self.cont[j] > self.cont[j+1]:
                   self.cont[j], self.cont[j+1] = self.cont[j+1], self.cont[j]
        return self.cont

 
    def insertion_sort(self):
        length = len(self.cont)
       
        for idx in range(1, length):
            while 0 < idx and self.cont[idx] < self.cont[idx - 1]:
                self.cont[idx], self.cont[idx-1] = self.cont[idx-1], self.cont[idx]
                idx -= 1

        return self.cont


    def merge_sort(self):
        if len(self.cont) > 1:
            mid = len(self.cont)//2
            L = self.cont[:mid]
            R = self.cont[mid:]
            
            leftsorter = SortList(L)
            leftsorter.merge_sort()
            rightsorter = SortList(R)
            rightsorter.merge_sort()

            i = j = k = 0
            
            while i < len(L) and j < len(R):
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

    
    def quick_sort(self, start, end):
        if start < end:
            pivot = self.partition(self.cont,start,end)
            self.quick_sort(start,pivot-1)
            self.quick_sort(pivot+1,end)

    def partition(self,array,start,end):
        x = array[end]
        i = start-1
        for j in range(start, end+1, 1):
             if array[j] <= x:
                 i += 1
                 if i<j:
                     z = array[i]
                     array[i] = array[j]
                     array[j] = z    
        return i
    
    
    def sorting(self, algm: str):
        return self.algm() 
        #return sorting_algorithms[algm]()
       

    def __repr__(self):
        return "{0}".format(self.cont)

if __name__ == '__main__':
    l = [45,1,3,7,6,59,42,22,11,6]
    exp = SortList(l)
    print("BEFORE -", exp)
    exp.merge_sort()
    print("AFTER - ", exp)
    '''ex = SortList([45,1,3,7,6,22,11,9])
    ex.sorting('bubble_sort')
    print(ex)
    p = SortList([1,3,7,6,59,42,22,11,6])
    p.sorting('quick_sort')
    print(p)
    e = SortList([15,45,1,3,7,6,59,42,22,11,6])
    e.sorting('insertion_sort') 
    print(e)'''      
