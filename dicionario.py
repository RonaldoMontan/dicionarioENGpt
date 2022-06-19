import psycopg2

resposta = ''#variavel vazia para entrar no loop
id = 'default'

#=========Conectadno com o BANCO DE DADOS=========

conexao = psycopg2.connect( host = 'local',
                            database = 'dic',
                            user = 'root',
                        password = '123')

while resposta in 'sS':

    palavraIngles = str(input("Qual palavra em inglês você quer armazenar?  "))
    primeiraLetra = palavraIngles[0]#pega a letra na posição zero
    traducao = str(input(f'Qual é a tradução da palavra {palavraIngles} ?  '))

    print(primeiraLetra, palavraIngles, traducao)

    #auxilio nos comandos de SQL
    cursor = conexao.cursor()
    
    #=====Verificando se a palavra existe no banco=====    
    cursor.execute(f"""select * from {primeiraLetra} where {primeiraLetra} like '{palavraIngles}'""")
    linhas = cursor.fetchall()#armazena linha encorntrada no banco dedados
    
    
    if len(linhas) == 0:#if faz a leitura das linhas, se não tiver registrou ou seja 0 insere nova palavra,
        #=====Inserindo registro no banco=====
        cursor.execute(f"""insert into {primeiraLetra} values({id}, '{palavraIngles}', '{traducao}');""")
        print('===== Palavra inserida com sucesso... =====') 
        conexao.commit()           
        
    else: #se a consulta retornou registo ou seja 1 não insere nobanco
        print('\n=====Palavra já existe no banco de dados!!=====\n')
        print(f'\n{linhas}\n')   
        
   resposta = str(input('Deseja continuar ?'))#controle do loop, qualquer letra diferente de sS sai do loop
    
cursor.close()
conexao.close()
