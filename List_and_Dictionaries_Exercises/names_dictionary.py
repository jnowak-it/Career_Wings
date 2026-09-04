# 🇵🇱Do zmiennej names przypisano listę imion męskich. Stwórz słownik, którego kluczami będą pierwsze litery imion,
# a wartościami, wszystkie imiona zaczynające się na daną literę. Np. name_dict['P'] powinno zwrócić Paweł, Piotr.
# Uwaga: imiona w słowniku nie powinny się powtarzać!

# 🇬🇧The variable names holds a list of male first names. Create a dictionary whose keys are the first letters of the
# names, and whose values are all the names starting with that letter. For example, name_dict['P'] should return Paweł,
# Piotr. Note: the names in the dictionary should not repeat!

names = ['Paweł', 'Kewin', 'Ireneusz', 'Bolesław', 'Mateusz',
'Edward', 'Piotr', 'Jan', 'Denis', 'Amir', 'Igor', 'Borys',
'Robert', 'Ariel', 'Kuba', 'Rafał', 'Mateusz', 'Emanuel']
name_dict = {}

for name in names:
    male_name = name_dict.setdefault(name[0], set())
    male_name.add(name)

print(name_dict)
print(name_dict['P'])