#Produto cartesiano
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]


#1) Gera uma lista de tuplas organizadas por cor e, em seguida, por tamanho.
tshirts_sorted = [sorted((color, size)) for color in colors for size in sizes]
