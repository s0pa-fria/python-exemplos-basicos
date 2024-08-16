# Lista usando laço For
print(" ")
print("Lista de lojas")
print(" ")

lojas = ["Santo-André", "São Bernardo", "SCS", "Mauá", "Diadema" ]

# Listar usando laço com indice
for i, loja in enumerate(lojas,1):
    print(f"{i} - {loja}")
    print(" ")