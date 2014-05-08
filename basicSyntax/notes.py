name = "Gabriel"
last_name = "Ferraz"

array = ["Paulo", "Christina","Marcela","Fabiana"]

dictionary = {'the_array': array, 'the_name': name, 'last_name': last_name}

array_two=[]

var = 0
for i in array:
    print array[var]
    var += 1
    if i == "Marcela":
        array_two.append(array[var])
        print array_two
        break

for i in range(0,4):
    print array[i]
