
#exercicio = Sistema de analise de crédito 


#Lógica - O cliente deve ser maior de idade, a renda tem que ser maior ou igual a 1200 e o score deve ser maior que 400

#solicitar o nome do cliente 

Nome = input("Qual é o seu nome?")

#solicitar a idade 

Idade = int(input("Qual é a sua idade?"))

#Solicitar a renda

Renda = int(input("Qual é a sua renda mensal?"))

#Score 
Score = int(input("Qual é o seu Score?"))


#### MONTANDO A LÓGICA DE PROGRAMAÇÃO 

#Para ter o crédito aprovado todas as condições devem ser verdadeiras, a principal é a maior idade. 

# Analisando as condições

if Idade < 18 : #Validando se o cliente é maior que 18 anos
   print("Negado por idade") #Caso seja menor que 18 anos, irá retornar esta mensagem
else: # Se for maior que 18, ele irá validar a renda
   if Renda < 1200 : # Validando se a renda é manor que 1200
     print("Negado por renda") #Caso eja menor que 1200, irá retornar esta mensagem 
   else: #Se for maior que 1200, ele irá validar o score 
      if Score < 400 : # Validando se o score é menor que 400
         print("Infelizmente você foi reprovado") #Caso seja menor que 400
      else:
         print("Parabéns, você foi APROVADO!") #Caso seja maior que 400

      


