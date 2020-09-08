import matplotlib.pyplot as plt
import csv

# duomenu istraukimas is naujo failo

new_list = []
# cities = [] # sudaromas visu miestu sarasas
unique_cities = [] # sudaromas unikaliu miestu sarasas
cities_avg = [] # sudaromas vidurkiu sarasas
data = {} # sudaromas dictionary is dvieju sarasu
sum_Yangon, count_Yangon, avg_Yangon = 0, 0, 0
sum_Naypyitaw, count_Naypyitaw, avg_Naypyitaw = 0, 0, 0
sum_Mandalay, count_Mandalay, avg_Mandalay = 0, 0, 0

# idealiausias budas viska su dictionary daryt:

# masyvas su dictionary, generuojamas programiskai aisku:
dict = [{"city": {
         "name": 'Yangon',
         "sum": 0,
         "count": 0,
         "avg": 0
        }
    }
]
# print(dict[0]['city']['name'])
# dict[0]['city']['name'] = 'Vilnius'
# print(dict[0]['city']['name'])

with open('C:\Max\Code\supermarket_sales_new.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # sudaromas 2D sarasas
    for line in csv_reader:
        new_list.append(line)

    # sudaromas visu miestu sarasas
    # for i in range(len(new_list)):
    #     if i == 0: # nereikia headerio
    #         continue
    #     cities.append(new_list[i][0])

    # Cia Kernius sake kad galima sulipdyt i viena for visus if:
    for i in new_list:
        if i[0] == 'City':
            continue
        if i[0] not in unique_cities:
            # dict.append({"city": {"name": i[0]}})
            unique_cities.append(i[0])
        if i[0] == unique_cities[0]:
            # dict[0].sum += float(i[1])
            sum_Yangon += float(i[1])
            count_Yangon += 1
        elif i[0] == unique_cities[1]:
            sum_Naypyitaw += float(i[1])
            count_Naypyitaw += 1
        elif i[0] == unique_cities[2]:
            sum_Mandalay += float(i[1])
            count_Mandalay += 1

    # # sudaromas unikaliu miestu sarasas
    # for i in cities:
    #     if i not in unique_cities:
    #         unique_cities.append(i)
    #
    # # skaiciuojamas kiekvieno miesto vidurkis
    # for i in new_list:
    #     if i[0] == unique_cities[0]:
    #         # print(i[0], end=' ')
    #         # print(i[1])
    #         sum_Yangon += float(i[1])
    #         count_Yangon += 1
    #     elif i[0] == unique_cities[1]:
    #         # print(i[0], end=' ')
    #         # print(i[1])
    #         sum_Naypyitaw += float(i[1])
    #         count_Naypyitaw += 1
    #     elif i[0] == unique_cities[2]:
    #         # print(i[0], end=' ')
    #         # print(i[1])
    #         sum_Mandalay += float(i[1])
    #         count_Mandalay += 1

    # apskaiciuojami vidurkiai ir sudaromas vidurkiu sarasas
    avg_Yangon = round(sum_Yangon / count_Yangon, 2)
    avg_Naypyitaw = round(sum_Naypyitaw / count_Naypyitaw, 2)
    avg_Mandalay = round(sum_Mandalay / count_Mandalay, 2)
    cities_avg.append(avg_Yangon)
    cities_avg.append(avg_Naypyitaw)
    cities_avg.append(avg_Mandalay)

    # print('avg_Yangon: ' + str(avg_Yangon))
    # print('avg_Mandalay: ' + str(avg_Mandalay))
    # print('avg_Naypyitaw: ' + str(avg_Naypyitaw))

    # sudaromas dictionary is miestu ir vidurkiu sarasu
    data = dict(zip(unique_cities, cities_avg))

    print(data)

# grafiku vaizdavimas pagal istrauktus duomenis

plt.xkcd() # comics style

fig, (axs1, axs2, axs3) = plt.subplots(nrows=1, ncols=3, figsize=(9, 3), sharey=True)

axs1.bar(unique_cities, cities_avg)
axs2.scatter(unique_cities, cities_avg)
axs3.plot(unique_cities, cities_avg)

axs1.set_ylabel('Unit price')
axs2.set_xlabel('Miestai')

fig.suptitle('Unit price pagal miestus')

# pabandziau pavaizduoti bar values, bet atrodo baisiai
# for index, value in zip(unique_cities, cities_avg):
#      axs1.text(index, value, str(value))
#      axs2.text(index, value, str(value))
#      axs3.text(index, value, str(value))

plt.show()
