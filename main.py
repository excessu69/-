import os
#Задание №1
path = os.path.join(os.getcwd(), 'cookbook.txt')
with open(path, encoding='utf-8') as f:
    cookbook = {}
    for string in f:
        dish = string.strip()
        ingredients_count = int(f.readline().strip())
        dish_dict = []  #
        for item in range(ingredients_count):
            ingredient_name, quantity, measure = f.readline().strip().split('|')
            dish_dict.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        cookbook[dish] = dish_dict
        f.readline()

print('Задача №1: ')
print(f'cook_book = {cookbook}')

#Задание №2
def get_shop_list_by_dishes(dishes, person_count):
    grocery_dict = {}
    for dishs in dishes:
        for ingredient in cookbook[dishs]:
            ingredient_list = dict([(ingredient['ingredient_name'],
                                     {'quantity': int(ingredient['quantity']) * person_count,
                                      'measure': ingredient['measure']})])
            if grocery_dict.get(ingredient['ingredient_name']) == 'None':
                _merger = (int(grocery_dict[ingredient['ingredient_name']]['quantity']) +
                           int(ingredient_list[ingredient['ingredient_name']]['quantity']))
                grocery_dict[ingredient['ingredient_name']]['quantity'] = _merger
            else:
                grocery_dict.update(ingredient_list)
    return grocery_dict


print('\nЗадача №2: ')
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))



#Задание №3
folder_path = "sorted"


file_names = os.listdir(folder_path)

files_content = []


for file_name in file_names:
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()
        files_content.append((file_name, len(file_content.split('\n')), file_content))

files_content.sort(key=lambda x: x[1])


result_file_path = "sorted/result.txt"


with open(result_file_path, 'w', encoding='utf-8') as result_file:
    for file_info in files_content:
        result_file.write(f"Файл: {file_info[0]}\nКоличество строк: {file_info[1]}\n")
        result_file.write(file_info[2])
        result_file.write("\n\n")



