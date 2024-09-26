# "Генераторы"
def all_variants(text):
    i = 1
    while i <= len(text):
        j = 0
        while j <= len(text) - i:
            yield text[j:j+i:1]
            j += 1
        i += 1

def all_variants_my(text):
    i = 0
    while i < len(text):
        j = i + 1
        while j <= len(text):
            yield text[i:j:1]
            j += 1
        i += 1

a = all_variants('abc')
b = all_variants_my('text')

for i in a:
    print(i)

print('Version #2')
for i in b:
    print(i)


#obj = func_generator(10)
#for i in obj:
#    print(i)