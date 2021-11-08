def medians(nums1,nums2): #Создаем функцию
    if nums1 == '[]':
        n = len(nums2) #Смотрим количество элементов обьекта
        index = n//2
        if n%2:
            return sorted(nums2)[index] #Возвращаем отсортированный список
        return sum(sorted(nums2)[index-1:index+1])/2
    elif nums2 == '[]':

        m = len(nums1)
        index = m//2
        if m%2:
            return sorted(nums1)[index]
        return sum(sorted(nums1)[index-1:index+1])/2
    else:
        A_nums1 = nums1[1:-1] #В несколько строчек преобразуем в список, убирая все ненужное
        S_nums1 = (A_nums1.split(',')) #Как раз здесь убираем запятые
        i = iter(S_nums1) #Производим итерацию
        L_nums1 = list(iter(lambda: int(next(i)), None)) #Преобразуем в список
        A_nums2 = nums2[1:-1] #Делаем то же самое со вторым значением
        S_nums2 = (A_nums2.split(','))
        i = iter(S_nums2)
        L_nums2 = list(iter(lambda: int(next(i)), None))
        Spisok = [] #Создаем пустой список, а дальше просто наполняем его через цикл
        for j in range (len(L_nums2)):
            Spisok.append(L_nums2[j])
        for i in range (len(L_nums1)):
            Spisok.append(L_nums1[i])
        Spisok.sort()
        print(Spisok) #Выводим общий список
        n = len(Spisok)
        index = n//2
        if n%2:
            return sorted(Spisok)[index]
        return sum(sorted(Spisok)[index-1:index+1])/2

print ('')
nums1 = input('nums1 = ', )
nums2 = input('nums2 = ', )
print(medians(nums1,nums2))#Выводим медиану


#Как сделать необходимое время, я не знаю, увы(((
