n = input('digite algo: ')
print('\033[7;32mo tipo primitivo deste valor é: ', type(n))
print('Só tem espaços?: ',  n.isspace())
print('É um numero?: ', n.isnumeric())
print('É alfabeto?: ', n.isalpha())
print('É alfanumerico?: ', n.isalnum())
print('Está em letras maiusculas?: ', n.isupper())
print('Está em letras minsculas?: ', n.islower())
print('Está capitalizada?: ', n.istitle())








