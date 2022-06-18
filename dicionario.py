import psycopg2

resposta = ''#variavel vazia para entrar no loop
id = 'default'

while resposta in 'sS':

    palavraIngles = str(input("Qual palavra em inglês você quer armazenar?  "))
    primeiraLetra = palavraIngles[0]#pega a letra na posição zero

    traducao = str(input(f'Qual é a tradução da palavra {palavraIngles} ?  '))

    print(primeiraLetra, palavraIngles, traducao)

    #=========Conectadno com o BANCO DE DADOS=========

    conexao = psycopg2.connect( host = 'local',
                            database = 'dic',
                            user = 'root',
                        password = '123')

    #auxilio nos comandos de SQL
    cursor = conexao.cursor()
    cursor.execute(f"""insert into {primeiraLetra} values({id}, '{palavraIngles}', '{traducao}');""")
    
    print('===== Palavra inserida com sucesso... =====')
    conexao.commit()
    cursor.close()
    conexao.close()

    resposta = str(input('Deseja continuar ?'))#controle do loop
