sarasas = [3, 7, 5, 10, 1]

# for i in sarasas:
#     for k in sarasas:
#         print(f'({i}, {k})')
#         if i < k or i == k:
#             continue
#         print(k)

# for i in sarasas:
#     for k in sarasas:
#         if i > k:
#             temp = i
#             i = k
#             k = temp
#             print(i)
#         else:
#             continue

for k in range(1, 5):
    for i in range(5):
        if i < 4:
            if sarasas[i] > sarasas[i + 1]:
                temp = sarasas[i]
                sarasas[i] = sarasas[i + 1]
                sarasas[i + 1] = temp
print(sarasas)

# for i in range(5):
#     while sarasas[i] > sarasas[i+1]:
#         if i >= 4:
#             continue
#         else:
#             temp = sarasas[i]
#             sarasas[i] = sarasas[i+1]
#             sarasas[i+1] = temp
#             print(sarasas[i])
#     else:
#         print(sarasas[i])