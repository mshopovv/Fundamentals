first_list = input().split(', ')
second_list = input().split(', ')

third_list = [first_string for first_string in first_list if any(first_string in second_string for second_string in second_list)]

# third_list = []
#
# for word1 in first_list:
#     for word2 in second_list:
#         if word1 in third_list:
#             continue
#         elif word1 in word2:
#             third_list.append(word1)

print(third_list)