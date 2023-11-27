# lst = [(1, 2), (3, 4)]
#
# print({
#     nums[0]: nums[1]
#     for nums in lst
# })

text = "Всем привет как дела тра та та"
pure_text = text.lower().replace('', '')
uniq_letters = set(pure_text)
letters = {
    letter: pure_text.count(letter)
    for letter in set(pure_text)
}

print(letters)
