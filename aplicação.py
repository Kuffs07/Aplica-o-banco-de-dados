from DB import DB
from datetime import datetime

db = DB()


def InserirUsuario():
    nome = input('Nome: ')
    email = input('Email: ')
    senha = input('Senha: ')
    data_criacao = datetime.today()
    inserir = f"INSERT INTO bancodedados(nome, email, senha, data_criacao) VALUES('{nome}', '{email}', '{senha}', " \
              f"'{data_criacao}'"
    result = db.ExecuteSQL(inserir)
    return result


def AlterarDados():
    ID_Participantes = int(input('Id do participante que deseja alterar: '))
    NovoNome = input('Novo Nome: ')
    NovoEmail = input('Novo Email: ')
    NovaSenha = input('Nova Senha: ')
    NovaData = datetime.today()
    alterar = f"UPDATE bancodedados SET nome = '{NovoNome}', email = '{NovoEmail}', senha = '{NovaSenha}', " \
              f"data_criacao = '{NovaData}' WHERE id_bancodedados = {ID_Participantes} "
    result = db.ExecuteSQL(alterar)
    return result


def RemoverDados():
    id_deletar = int(input('Qual ID do usuario que deseja deletar: '))
    deletar = f"DELETE FROM bancodedados WHERE id_bancodedados = {id_deletar}"
    result = db.ExecuteSQL(deletar)
    return result


def mostrarParticipantes():
    sql = f'SELECT * FROM bancodedados'
    result = db.ExecuteSQL(sql, True)
    for p in result:
        print(p)


while True:
    opcao = int(input('\nBanco de dados da Aplicação\n'
                      'Digite:\n1-Inserior Usuario\n2-Alterar Dados Usuario\n3-Remover Usuario\n'
                      '4-Mostrar Todos Usuarios\n5-SAIR\n'))
    if opcao == 1:
        InserirUsuario()
    elif opcao == 2:
        AlterarDados()
    elif opcao == 3:
        RemoverDados()
    elif opcao == 4:
        mostrarParticipantes()
    else:
        break
