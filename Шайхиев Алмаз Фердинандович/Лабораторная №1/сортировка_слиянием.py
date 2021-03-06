def mergeSort(alist):
    print("Разделение эллементов массива: ",alist)
    #деление массива,пока каждый эллемент не станет отдельным эллементом
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        #рекурсивный вызов функции
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        #перестановка в массиве
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
        #последний эллемент в массиве
        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Слияние эллементов массива: ",alist)

N = int(input("Введите кол-во эллементов массива:"));
alist =[]
for i in range (N):
    new_element = int(input())
    alist.append(new_element)
mergeSort(alist)
print(alist)
