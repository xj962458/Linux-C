'''
            --  对排序算法进行了一个封装，方便调用 --

    sorts类：

        _swap：      交换数组中两个位置的私有方法
        selectSort： 选择排序法的一个实现
        insertSort： 插入排序法的实现
        insertSortOptimize：对插入排序的一个优化
        bubbleSort： 优化后的冒泡排序
        _insertSort：对数组区间进行优化插入排序，定义这个方法的主要目的是为后面
            高级排序算法优化作准备，当n比较小的时候，优化后的插入排序比归并排序和
            快速排序都来得快
        QKSort2Way： 快速排序的双路实现
        QKSort1Way： 快速排序的单路实现
        mergeSort：  归并排序算法的实现

        Made by JinFan  -- 2019.09.25
'''




class sorts:

    def __init__(self):
        pass

    def _swap(self, arr, i, j):

        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def selectSort(self, arr):

        for i in range(len(arr)):
            minIndex = i
            for j in range(i+1, len(arr)):
                if arr[minIndex] > arr[j]:
                    minIndex = j
            if minIndex != i:
                self._swap(arr, minIndex, i)

    def insertSort(self, arr):

        for i in range(1, len(arr)):
            for j in range(i, 0, -1):
                if arr[j] < arr[j-1]:
                    self._swap(arr, j, j-1)
                else:
                    break

    def insertSortOptimize(self, arr):

        for i in range(1, len(arr)):
            temp = arr[i]
            a = []
            for j in range(i, 0, -1):
                if arr[j-1] > temp:
                    arr[j] = arr[j-1]
                    a.append(j-1)
                else:
                    a.append(j)
                    break
            arr[a[-1]] = temp

    def bubbleSort(self, arr):

        n = len(arr)
        for i in range(1, n):
            for j in range(n-1):
                if arr[j] > arr[j+1]:
                    self._swap(arr, j, j+1)
                    n = j+1

    def _insertSort(self, arr, l, r):

        for i in range(l+1, r+1):
            temp = arr[i]
            a = []
            for j in range(i, 0, -1):
                if arr[j - 1] > temp:
                    arr[j] = arr[j - 1]
                    a.append(j - 1)
                else:
                    a.append(j)
                    break
            arr[a[-1]] = temp

    def QKSort2Way(self, arr):

        self._QKSort2Way(0, len(arr)-1, arr)

    def _QKSort2Way(self, l, r, arr):

        if r-l <= 15:
            self._insertSort(arr, l, r)  # 高级排序的统一优化
            return
        i = l
        j = r
        temp = arr[i]

        while i != j:
            while arr[j] >= temp and i < j:
                j -= 1
            while arr[i] <= temp and i < j:
                i += 1
            if i < j:
                self._swap(arr, i, j)
        arr[l] = a[i]
        a[i] = temp
        self._QKSort2Way(l, i-1, arr)
        self._QKSort2Way(i+1, r, arr)

    def QKSort1Way(self, arr):

        self._QKSort1Way(arr, 0, len(arr)-1)

    def _QKSort1Way(self, arr, l, r):

        if r-l <= 15:
            self._insertSort(arr, l, r)  # 高级排序的统一优化
            return
        p = self._partition(arr, l, r)

        self._QKSort1Way(arr, l, p)
        self._QKSort1Way(arr, p+1, r)

    def _partition(self, arr, l, r):

        temp = arr[l]
        j = l
        for i in range(l+1, r+1):
            if arr[i] < temp:
                self._swap(arr, j+1, i)
                j += 1
        self._swap(arr, l, j)

        return j

    def mergeSort(self, arr):

        self._mergeSort(arr, 0, len(arr)-1)

    def _mergeSort(self, arr, l, r):

        if r-l <= 15:
            self._insertSort(arr, l, r)  # 高级排序的统一优化
            return
        mid = (l+r) // 2
        self._mergeSort(arr, l, mid)
        self._mergeSort(arr, mid+1, r)

        if arr[mid] > arr[mid+1]:
            self._mergeSort_(arr, l, mid, r)

    def _mergeSort_(self, arr, l, mid, r):

        b = arr[l:r+1]
        i, j = l, mid+1
        for k in range(l, r+1):
            if i > mid:
                arr[k] = b[j-l]
                j += 1
            elif j > r:
                arr[k] = b[i-l]
                i += 1
            elif b[i-l] < b[j-l]:
                arr[k] = b[i-l]
                i += 1
            else:
                arr[k] = b[j-l]
                j += 1


# 测试
if __name__ == "__main__":

    s = sorts()
    a = [9, 1, 8, 2, 7, 3, 6, 5, 2, 2, 9, 9, 9, 9, 9, 9, 9, 9]
    s.mergeSort(a)
    print(a)
    a = [9, 1, 8, 2, 7, 3, 6, 5, 2, 2, 9, 9, 9, 9, 9, 9, 9, 9]
    s.QKSort2Way(a)
    print(a)
    a = [9, 1, 8, 2, 7, 3, 6, 5, 2, 2, 9, 9, 9, 9, 9, 9, 9, 9]
    s.QKSort1Way(a)
    print(a)
    a = [9, 1, 8, 2, 7, 3, 6, 5, 2, 2, 9, 9, 9, 9, 9, 9, 9, 9]
    s.bubbleSort(a)
    print(a)
    a = [9, 1, 8, 2, 7, 3, 6, 5, 2, 2, 9, 9, 9, 9, 9, 9, 9, 9]
    s.insertSortOptimize(a)
    print(a)
    a = [9, 1, 8, 2, 7, 3, 6, 5, 2, 2, 9, 9, 9, 9, 9, 9, 9, 9]
    s.selectSort(a)
    print(a)
    a = [9, 1, 8, 2, 7, 3, 6, 5, 2, 2, 9, 9, 9, 9, 9, 9, 9, 9]
    s.insertSort(a)
    print(a)
    print("---------------------")
    print('success!')
