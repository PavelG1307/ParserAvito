# f = open('ids.ini', mode = 'r')
# ids = f.readlines()
# f = open('unique_ids.ini', mode = 'w')
# unique_id = []
# for id in ids:
#     if id not in unique_id:
#         unique_id.append(id)
#         f.write(id)
 
f = open('unique_ids.ini', mode = 'r')
ids = f.readlines()
f = open('ids_new.ini', mode = 'r')
ids_new = f.readlines()


count = 0
count2 = 0
for id in ids_new:
    if id not in ids:
        id = id.strip()
        count+=1
        print(f'{id} нет в старом')

for id in ids:
    if id not in ids_new:
        id = id.strip()
        count2+=1
        print(f'{id} нет в новом')

print(f'В старом нет {count}, в новом нет {count2}')