produtos = {}
print ("---Cadastre seus produtos:")
cod = input("    Digite o código: ")
while cod !='':
    preco = float(input("    Digite o preço: "))
    produtos[cod] = preco
    cod = input("    Digite o código: ")

print ("---Fim do cadastro\n")
print ("---Produtos cadastrados---")
for cod in produtos.keys():
    print (f"Produto {cod} --- R$ {produtos[cod]:6.2f}")

