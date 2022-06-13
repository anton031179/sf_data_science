# Выполните все действия, указанные в комментариях в файле
import numpy as np
mystery = np.array([12279., -26024., 28745., nan, 31244., -2365., -6974., -9212., nan, -17722., 16132., 25933., nan, -16431., 29810.])
print (mystery)
# Получите булевый массив с информацией о np.nan в массиве mystery
# True - значение пропущено, False - значение не пропущено
nans_index = np.isnan(mystery)
print(nans_index)
# В переменную n_nan сохраните число пропущенных значений
n_nan = 3

# Заполните пропущенные значения в массиве mystery нулями
mystery[np.isnan(mystery)] = 0
print(mystery)

# Поменяйте тип данных в массиве mystery на int32
mystery=np.int32(mystery)
print(mystery)

# Отсортируйте значения в массиве по возрастанию и сохраните
# результат в переменную array
array = np.sort(mystery)

# Сохраните в массив table двухмерный массив, полученный из массива array
# В нём должно быть 5 строк и 3 столбца. Причём порядок заполнения должен быть
# по столбцам! Например, 1, 2, 3, 4 -> 1    3
#                                      2    4
table = array.reshape((5, 3), order='F')
print(table)
#  Сохраните в переменную col средний столбец из table
col = table[:,1]
print(col)




    

