nome = input('Digite o teu nome: ').upper
valid_idade = False
while valid_idade == False:
       idade = input('Digite a tua idade: ')
       try:
              idade = int(idade)
              if idade <= 0:
                     print( 'Somente numeros positivos são aceitos')
              else:
                     valid_idade = True
       except:
              print('Somente numeros inteiros')
v_sexo = False
while v_sexo == False:
       sexo = input('Digite o teu sexo:(F ou M) ').lower()
       if sexo != 'm' and sexo != 'f':
              print ('Somente será aceito as letras F ou M ')
       else:
              v_sexo = True
valid_mes = False
while valid_mes == False:
       mes = input ( 'Em que mes você nasceu? Coloque o numero p.ex. 1- Janeiro , 2 - Fevereiro, etc. ')
       try:
              mes = int(mes)
              if mes <= 0 or mes > 12:
                     print('Digite somente valores possiveis entre 1 e 12')
              else:
                     valid_mes = True
       except:
              print('Digite apensas o numero do mes sem: letra, zero na frente e entre 1 e 12')
       
opiniao = input('O que você achou do meu projeto e o que você melhoraria nele?\n')
print ('Bem - vindo '+ nome.title() + 'agradecemos a tua colaboração\n')
print ('Criamos um email para você : '+ nome + '@email.com.br')




