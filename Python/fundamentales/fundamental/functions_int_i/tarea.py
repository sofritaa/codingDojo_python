x = [ [5,2,3], [10,8,9] ]
estudiantes = [
{'first_name': 'Michael', 'last_name' : 'Jordan'},
{'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

estudiantes[0]['last_name'] = "Bryant"
print(estudiantes)

directorio_deportes['fútbol'][0] = 'andres'
print(directorio_deportes['fútbol'])

z[0]['y'] = 30
print(z)

#2
def iterateDictionary(some_list):
    for dictionary in some_list:
        for key, value in dictionary.items():
            print(f"{key} - {value}")

estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary(estudiantes)

#3
def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        if key_name in dictionary:
            print(dictionary[key_name])
estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary2('first_name', estudiantes)
iterateDictionary2('last_name', estudiantes)

#4
def printInfo(some_dict):
    for key, value in some_dict.items():
        print(f"{len(value)} {key.upper()}")
        for item in value:
            print(item)
        print()
dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)
