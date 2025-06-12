=======================================================================================================================================================================
RECOMENDACOES!

1- no arquivo connect_redis.py configurar a conexao corretamente com o banco que voce criou!! SE NAO FIZER NAO VAI FUNCIONAR!
2- as consultas somente irao funcionar se voce ja tiver gerado os sorteios, entao lembre de rodar o arquivo que cria os sorteios PRIMEIRO!
3- ordem recomendada pra executar o programa(executar consulta antes de megasena nao funcionara pois voce precisa criar os dados primeiro):

- test_connection_redis.py 
- limpeza_redis.py 
- megasena_redis.py 
- consulta_redis.py  
(executar consulta antes de megasena nao vai funcionar pois voce precisa criar os dados primeiro,
 leia o proximo topico para entender melhor oque cada arquivo faz!)


=======================================================================================================================================================================
lISTA DE ARQUIVOS E OQUE ELES FAZEM!

connect_redis.py = configure aqui as suas credenciais no local indicado dentro do codigo pra acessar o banco de dados do redis.

megasena_redis.py = cria e salva no banco todos os sorteios.

test_connection_redis.py = testa pra ver se a sua conexao está funcionando adequadamente.

limpeza_redis.py = esse ele vai servir pra apagar seus sorteios criados caso ele tenha bugado na hora de criar os arquivos e bugarem, ai voce cria novamente os sorteios. (rode esse arquivo primeiro, para garantir que nao existe nenhum dado existente previamente.)

consulta_redis.py = esse arquivo possui funcoes para fazer consultas no banco, caso queira é só ir adicionando novas funcoes para ir consultando. 


=======================================================================================================================================================================
ENTENDENDO NOSSO BANCO REDIS

No banco de dados o codigo vai criar 2 grupos de chaves, 'sorteio' e 'data' em data: o nome do arquivo sera a data e dentro do arquivo deve conter o numero do sorteio... já em sorteio: o nome do arquivo sera o numero do sorteio e dentro do arquivo tera as informacoes como: numero do sorteio, data, numeros sorteados e total de ganhadores.


=======================================================================================================================================================================
INSTRUCOES PARA CONSEGUIR RODAR O PROGRAMA!

ETAPA 1: CRIAR O BANCO REDIS. 

1- criar uma conta no site do redis: https://redis.io/try-free/

2- logar no redis e criar um banco de dados:
- clique em criar banco de dados, selecione a versao gratis.
- coloque um nome para seu banco de dados (qualquer nome).
- selecione 1 host (eu utilizei a da aws mas voce pode usar qualquer uma).
- escolha a regiao mais perto pra ter uma melhor conexao.
- escolha o tipo: vamos utilizar o redis stack e nao memcached.

- pronto, seu banco esta criado!


=======================================================================================================================================================================
ETAPA 2: PEGAR SUAS CREDENCIAIS PARA CONEXAO.

1- obter as suas credenciais de acesso.

- selecione a aba databases.
- vai aparecer todos os bancos que voce criou, selecione o banco que voce criou na etapa 1 clicando no botao 'connect'.
- vai aparecer uma janela com varias opcoes de conexao diferente.
- voce deve clicar na opcao "Redis Client".
- selecione o tipo de client que voce vai usar, no projeto usamos Python.
- ele vai te dar esse codigo abaixo:

        """Basic connection example.
        """

        import redis

        r = redis.Redis(
            host='*************************************************',
            port=********,
            decode_responses=True,
            username="default",
            password="*******",
        )

        success = r.set('foo', 'bar')
        # True

        result = r.get('foo')
        print(result)
        # >>> bar





 - voce so precisa da parte abaixo:

    host='endereco_do_seu_banco_de_dados', 
    port= numero_da_porta,
    decode_responses=True,
    username="nome_do_seu_username",
    password="sua_senha",

- sua senha vai estar oculta, entao clique no icone pra mostrar os dados ocultos. 
- pegue as informacoes e coloque no local indicado no arquivo: connect_redis.py


=======================================================================================================================================================================
ETAPA 3: INSTALAR AS DEPENDENCIAS NA SUA MAQUINA.

1- se voce for rodar pelo vscode segue o passo abaixo, se for rodar pelo CMD veja o proximo passo: 

- RODAR VIA VSCODE

- abrir o terminal, selecione split terminal / command prompt
- o cmd vai abrir dentro do seu terminal do vscode, agora falta instalar as dependencias.

- rode o comando:
pip install redis

- apos finalizar rode o proximo comando:
pip install python-dotenv

-apos finalizar deve aparecer uma pastinha com nome de "venv" dentro do seu projeto que significa que foi instalado com sucesso.

- feche o terminar e abra novamente antes de executar o programa.

-------------------------------------------------------------------------------------------------------------------------------------
-  RODAR DIRETO NO CMD

- abra o cmd como administrador
- selecione a pasta do seu projeto usando o comando: cd c:\local_do_seu_projeto

- agora falta instalar as dependencias.

- rode o comando:
pip install redis

- apos finalizar rode o proximo comando:
pip install python-dotenv

-apos finalizar deve aparecer uma pastinha com nome de "venv" dentro do seu projeto que significa que foi instalado com sucesso.

- feche o cmd e abra novamente antes de executar o programa, lembre se de selecionar a pasta do seu projeto novamente usando o comando: cd c:\local_do_seu_projeto.


=======================================================================================================================================================================
ETAPA 4: RODAR O PROGRAMA.

1- pra rodar o programa vamos rodar o seguinte comando: .\venv\Scripts\activate
apos rodar o comando vai aparecer algo do tipo no console: 
(venv) C:\caminho_do_seu_projeto>
isso indica que voce ja esta rodando o projeto, agora so rodar os arquivos.


2- comando para rodar QUALQUER arquivo do projeto: python nome_do_arquivo.py

3- siga a ordem recomendada para o programa funcionar (esta dentro do topico RECOMENDACOES).
=======================================================================================================================================================================



