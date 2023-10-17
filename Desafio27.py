# Ler o nome completo de uma pessoa, mostrar de seguida o primeiro e ultimo nome separadamente

nome = input( ' Escreve o teu nome completo ')

dividido = nome.split()

primeiro = dividido[0]
ultimo = dividido[-1]


print(' O teu primeiro nome é {} e o teu último nome é {}'.format(primeiro , ultimo))