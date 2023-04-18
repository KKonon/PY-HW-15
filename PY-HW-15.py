# Сжать массив, удалив из него все элементы, величина которых находится в интервале [а, b].
# Освободившиеся в конце массива элементы заполнить нулями.

Blist = [5,2,3,7,9]

for i in Blist:

   if len(Blist) == 5:
      del Blist[1:4]

   if len(Blist) != 5:
      Blist.insert(2,0)

   if len(Blist) == 5:
      print(Blist)