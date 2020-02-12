# список покупок
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']

print('Я должен сделать', len(shoplist), 'покупок')

print('Покупки:', end='')  # end это тоже самоу что и \n отступ строки
for item in shoplist:
    print(item, end='')

print('\nТакже нужно купить риса.')
shoplist.append('рис')
print('Теперь мой список покупок таков:', shoplist)

print('Отсортирую-ка я свой список')
shoplist.sort()
print('Отсортированный список покупок выглядит так:', shoplist)

print()