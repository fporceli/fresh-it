from PySimpleGUI import PySimpleGUI as sg
from conexao import *

querybuscarlicenca = "select * from lisensa"
cursor = con.cursor()
cursor.execute(querybuscarlicenca)
linhaslicenca = cursor.fetchall()

querybuscarrelatorio = "select * from infomanutencao"
cursorg = con.cursor()
cursor.execute(querybuscarrelatorio)
linhasrelatorio = cursor.fetchall()


def janela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('User', size=(8, 0), font="Verdana"), sg.Input(key='user', size=(17, 4), font="Verdana")],
        [sg.Text('Password', size=(8, 0), font="Verdana"), sg.Input(key='password', size=(24, 4), password_char='*')],
        [sg.Text('Usuario ou Senha incorretos!', visible=False, key='incorrect', )],
        [sg.Text('Você está acessando como:', font="Verdana")],
        [sg.InputCombo(['Funcionario', 'Coordenador', 'Administrador'], font="Verdana",
                       key='cargos')],
        [sg.Button('Login')]
    ]
    return sg.Window('Login', layout=layout, finalize=True)


def janela_principal():
    sg.theme('Reddit')
    # Aba Minhas Infos
    tabminhasinfos = [
        [sg.Image(r'C:\Users\PORCE\Desktop\Meus Arquivos\TCC\TCC\images\user.png')]
    ]
    tabminhasinfos += [
        [sg.Text(
            'Nome: {}\n\nCódigo FreshIT: {}\n\nCPF: {}\n\nCargo: {}'.format(linhaname[2], linhaname[0], linhaname[1],
                                                                            linhaname[3]), font="Verdana")] for
        linhaname in linhanome
    ]

    # Aba Meus Setores
    tabsetores = [
        # Linha 1
        [sg.Column([[sg.Button(linhaset[1], key='{}'.format(linhaset[1]), font="Verdana", size=(15, 2)),
                     sg.VerticalSeparator(pad=((10, 0), (0, 0)), color="none"),
                     sg.Text('Código do Setor: {} \nQuantidade de Ativos:{}\n\n '.format(linhaset[0], linhaset[2]),
                             size=(27, 2), font="Verdana")] for linhaset in linhasset], scrollable=True,
                   size=(480, 380))]

    ]
    tablicencas = [
        [sg.Column([[sg.Text(
            "Código: {}\nNome: {}\nData de Aquisição: {}\nData de Vencimento: {}\n________________________________________"
            .format(linhalicenca[0], linhalicenca[1], linhalicenca[2], linhalicenca[3]),
            font="Verdana")] for linhalicenca in linhaslicenca], scrollable=True, size=(500, 400))],
    ]
    tabrelatorio = [
        [sg.Column([[sg.Text(
            "Nova manutenção registrada.\n\nCódigo da manutenção: {}\nNome do equipamento: {}\nSetor do equipamento: {}\nStatus: {}\nTipo do equipamento: {}\nDescrição: {}\nFuncionário responsável: {}\n_______________________________________"
            .format(linharelatorio[0], linharelatorio[3], linharelatorio[7], linharelatorio[5], linharelatorio[4],
                    linharelatorio[6], linharelatorio[1]),
            font="Verdana")] for linharelatorio in linhasrelatorio], scrollable=True, size=(500, 400))],
    ]
    tabacoes = [
        [sg.Button('Logout', key='logout', font="Verdana")],
        [sg.Button('Editar Ativos', key='editativo', font="Verdana", visible=True)],
        [sg.Button('Editar Setores', font="Verdana", key='editset', visible=True)],
        [sg.Button('Editar Licenças', font="Verdana", key='editlic', visible=True)],
        [sg.Button('Registrar Manutenção', font="Verdana", key='editmanutencao', visible=True)],
    ]
    layout = [
        [sg.TabGroup([[sg.Tab('Minhas Informações', tabminhasinfos), sg.Tab('Meus Setores', tabsetores,
                                                                            key='meussetores'),
                       sg.Tab('Licenças', tablicencas), sg.Tab('Relatório', tabrelatorio, ),
                       sg.Tab('Ações', tabacoes, element_justification='center')]])]
    ]
    return sg.Window('Janela Principal', layout=layout, finalize=True, size=(500, 400))


def janela_principal2():
    sg.theme('Reddit')
    # Aba Minhas Infos
    tabminhasinfos = [
        [sg.Image(r'C:\Users\PORCE\Desktop\Meus Arquivos\TCC\TCC\images\user.png')]
    ]
    tabminhasinfos += [
        [sg.Text(
            'Nome: {}\n\nCódigo FreshIT: {}\n\nCPF: {}\n\nCargo: {}'.format(linhaname[2], linhaname[0], linhaname[1],
                                                                            linhaname[3]), font="Verdana")] for
        linhaname in linhanome
    ]

    # Aba Meus Setores
    tabsetores = [
        # Linha 1
        [sg.Column([[sg.Button(linhaset[1], key='{}'.format(linhaset[1]), font="Verdana", size=(15, 2)),
                     sg.VerticalSeparator(pad=((10, 0), (0, 0)), color="none"),
                     sg.Text('Código do Setor: {} \nQuantidade de Ativos:{}\n\n '.format(linhaset[0], linhaset[2]),
                             size=(27, 2), font="Verdana")] for linhaset in linhasset], scrollable=True,
                   size=(480, 380))]

    ]
    tablicencas = [
        [sg.Column([[sg.Text(
            "Código: {}\nNome: {}\nData de Aquisição: {}\nData de Vencimento: {}\n________________________________________"
            .format(linhalicenca[0], linhalicenca[3], linhalicenca[1], linhalicenca[2]), font="Verdana")] for
                    linhalicenca in linhaslicenca], scrollable=True, size=(500, 400))],
        [sg.Button('Voltar', font='Verdana', key='return')]
    ]
    tabrelatorio = [
        [sg.Column([[sg.Text(
            "Nova manutenção registrada.\n\nCódigo da manutenção: {}\nNome do equipamento: {}\nSetor do equipamento: {}\nStatus: {}\nTipo do equipamento: {}\nDescrição: {}\nFuncionário responsável: {}\n_______________________________________"
            .format(linharelatorio[0], linharelatorio[3], linharelatorio[7], linharelatorio[5], linharelatorio[4],
                    linharelatorio[6], linharelatorio[1]),
            font="Verdana")] for linharelatorio in linhasrelatorio], scrollable=True, size=(500, 400))],
    ]
    tabacoes = [
        [sg.Button('Logout', key='logout', font="Verdana")],
        [sg.Button('Editar Ativos', key='editativo', font="Verdana", visible=True)],
        [sg.Button('Editar Setores', font="Verdana", key='editset', visible=True)],
        [sg.Button('Registrar Manutenção', font="Verdana", key='editmanutencao', visible=True)],
    ]
    layout = [
        [sg.TabGroup([[sg.Tab('Minhas Informações', tabminhasinfos), sg.Tab('Meus Setores', tabsetores,
                                                                            key='meussetores'),
                       sg.Tab('Licenças', tablicencas), sg.Tab('Relatório', tabrelatorio, ),
                       sg.Tab('Ações', tabacoes, element_justification='center')]])]
    ]
    return sg.Window('Janela Principal', layout=layout, finalize=True, size=(500, 400))


def janela_principal3():
    sg.theme('Reddit')
    # Aba Minhas Infos
    tabminhasinfos = [
        [sg.Image(r'C:\Users\PORCE\Desktop\Meus Arquivos\TCC\TCC\images\user.png')]
    ]
    tabminhasinfos += [
        [sg.Text(
            'Nome: {}\n\nCódigo FreshIT: {}\n\nCPF: {}\n\nCargo: {}'.format(linhaname[2], linhaname[0], linhaname[1],
                                                                            linhaname[3]), font="Verdana")] for
        linhaname in linhanome
    ]

    # Aba Meus Setores
    tabsetores = [
        # Linha 1
        [sg.Column([[sg.Button(linhaset[1], key='{}'.format(linhaset[1]), font="Verdana", size=(15, 2)),
                     sg.VerticalSeparator(pad=((10, 0), (0, 0)), color="none"),
                     sg.Text('Código do Setor: {} \nQuantidade de Ativos:{}\n\n '.format(linhaset[0], linhaset[2]),
                             size=(27, 2), font="Verdana")] for linhaset in linhasset], scrollable=True,
                   size=(480, 380))]

    ]
    tablicencas = [
        [sg.Column([[sg.Text(
            "Código: {}\nNome: {}\nData de Aquisição: {}\nData de Vencimento: {}\n________________________________________"
            .format(linhalicenca[0], linhalicenca[3], linhalicenca[1], linhalicenca[2]), font="Verdana")] for
                    linhalicenca in linhaslicenca], scrollable=True, size=(500, 400))],
        [sg.Button('Voltar', font='Verdana', key='return')]
    ]
    tabrelatorio = [
        [sg.Column([[sg.Text(
            "Nova manutenção registrada.\n\nCódigo da manutenção: {}\nNome do equipamento: {}\nSetor do equipamento: {}\nStatus: {}\nTipo do equipamento: {}\nDescrição: {}\nFuncionário responsável: {}\n_______________________________________"
            .format(linharelatorio[0], linharelatorio[3], linharelatorio[7], linharelatorio[5], linharelatorio[4],
                    linharelatorio[6], linharelatorio[1]),
            font="Verdana")] for linharelatorio in linhasrelatorio], scrollable=True, size=(500, 400))],
    ]
    tabacoes = [
        [sg.Button('Logout', key='logout', font="Verdana")],
        [sg.Button('Editar Ativos', key='editativo', font="Verdana", disabled=False)],
        [sg.Button('Registrar Manutenção', font="Verdana", key='editmanutencao', visible=True)],
    ]
    layout = [
        [sg.TabGroup([[sg.Tab('Minhas Informações', tabminhasinfos), sg.Tab('Meus Setores', tabsetores,
                                                                            key='meussetores'),
                       sg.Tab('Licenças', tablicencas), sg.Tab('Relatório', tabrelatorio, ),
                       sg.Tab('Ações', tabacoes, element_justification='center')]])]
    ]
    return sg.Window('Janela Principal', layout=layout, finalize=True, size=(500, 400))


def janela_ativos():
    sg.theme('Reddit')
    layout = [
        [sg.Column([[sg.Text(
            'Código: {}\nNome do Ativo: {}\nTipo: {}\nData de Compra: {}\nStatus: {}\nQuantidade: {}\nValor pago: {}\n_____________________________'
            .format(linhasat[0], linhasat[1], linhasat[2], linhasat[3], linhasat[4], linhasat[5], linhasat[6]),
            font="Verdana")]
                    for linhasat in linhasativos], scrollable=True, size=(450, 330))],
        [sg.Button('Voltar', key='return', font="Verdana")]
    ]

    return sg.Window('Ativos', layout=layout, finalize=True, size=(450, 400))


def add_ativos():
    sg.theme('Reddit')
    layout = [
        [sg.Text(
            'Você atualmente está EXCLUINDO um ativo. Lembrando que depois de confirmada, essa ação não tera volta.\nPor favor, digite o código do ativo que deseja excluir!',
            key='msginfo2', visible=False)],
        [sg.Text('Código do Ativo', font="Verdana", key='txtcodativo', visible=True), sg.Input(key='inputcodativo',
                                                                                               size=(11, 1))],
        [sg.Text('Nome', font="Verdana", key='txtnome', visible=True, ), sg.Input(key='novonomeativo',
                                                                                  size=(50, 1), disabled=False)],
        [sg.Text('Tipo', font="Verdana", visible=True, key='txttipo'), sg.Input(key='novotipoativo',
                                                                                size=(30, 1), disabled=False)],
        [sg.Text('Data de Aquisição', font="Verdana", visible=True, key='txtdata'), sg.Input(key='novodataativo',
                                                                                             size=(11, 1),
                                                                                             disabled=False)],
        [sg.Text('Código do Setor', font="Verdana", key='txtcodset', visible=True), sg.Input(key='inputcodset',
                                                                                             size=(11, 1),
                                                                                             disabled=False)],
        [sg.Text('Status: ', font="Verdana", key='txtstatus', visible=True),
         sg.InputCombo(['Ativo', 'Inativo'], font="Verdana", key='statusativo', disabled=False)],
        [sg.Text('Quantidade:', font="Verdana", key='txtqtd', visible=True),
         sg.Input(key='inputqtd', size=(3, 1), disabled=False)],
        [sg.Text('Valor Pago', font="Verdana", key='txtvalorpago', visible=True), sg.Input(key='inputvalor',
                                                                                           size=(11, 1),
                                                                                           disabled=False)],
        [sg.Text('Algum dos valores inseridos são inválidos!', key='error', visible=False),
         sg.Text('Ativo ja Existente!', key='error2', visible=False),
         sg.Text('Setor não encontrado!', key='error3', visible=False)],
        [sg.Button('Adicionar ativo', key='add', font="Verdana"), sg.Button('Excluir', key='excluir', font="Verdana"),
         sg.Button('Cancelar', key='return', font="Verdana")]
    ]
    return sg.Window('Editar ativos', layout=layout, finalize=True)


def add_ativos2():
    sg.theme('Reddit')
    layout = [
        [sg.Text(
            'Você atualmente está EXCLUINDO um ativo. Lembrando que depois de confirmada, essa ação não tera volta.\nPor favor, digite o código do ativo que deseja excluir!',
            key='msginfo2')],
        [sg.Text('Código do Ativo', font="Verdana", key='txtcodativo'), sg.Input(key='inputcodativo',
                                                                                 size=(11, 1))],
        [sg.Text('Ativo não encontrado!', key='error2', visible=False)],
        [sg.Button('Excluir', key='excluir2', font="Verdana"), sg.Button('Cancelar', key='return', font="Verdana")],
    ]
    return sg.Window('Editar ativos', layout=layout, finalize=True)


def confirmar_ativo_novo():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Deseja mesmo confirmar essa ação?', font="Verdana")],
        [sg.Button('Confirmar', font="Verdana", key='confirmativo'),
         sg.Button('Cancelar', key='return', font="Verdana"), ]
    ]
    return sg.Window('Editar ativos', layout=layout, finalize=True)


def confirmar_edit_novo():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Deseja mesmo confirmar essa ação?', font="Verdana")],
        [sg.Button('Confirmar', font="Verdana", key='confirmativo'),
         sg.Button('Cancelar', key='return', font="Verdana"), ]
    ]
    return sg.Window('Editar ativos', layout=layout, finalize=True)


def confirmar_exclusao():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Deseja mesmo confirmar essa ação?', font="Verdana")],
        [sg.Button('Confirmar', font="Verdana", key='confirmativo'),
         sg.Button('Cancelar', key='return', font="Verdana"), ]
    ]
    return sg.Window('Editar ativos', layout=layout, finalize=True)


def janela_edit_set():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Você atualmente está ADICIONANDO um setor!\nPreencha os campos requisitados', key='txtmsginfo1',
                 visible=True),
         sg.Text('Você atualmente está EDITANDO um setor!\nPreencha os campos requisitados', key='txtmsginfo2',
                 visible=False), sg.Text(
            'Você atualmente está EXCLUINDO um editando!\nAo confirmar essa ação, não terá mais volta\nPreencha os campos requisitados',
            key='txtmsginfo3', visible=False)],
        [sg.Text('Código do Setor ', key='txtcodset', font='Verdana'),
         sg.Input(key='inputcodset2', size=(10, 1), font='Verdana')],
        [sg.Text('Nome do setor ', key='txtnomeset', visible=True, font='Verdana'),
         sg.Input(key='inputnomeset', size=(10, 1), font='Verdana')],
        [sg.Text('Algum dos valores inseridos são inválidos!', key='error', visible=False),
         sg.Text('Esse setor ja existe', key='error2', visible=False),
         sg.Text('Setor não encontrado', key='error3', visible=False)],
        [sg.Button('Adicionar', key='addset', visible=True, font='Verdana'),
         sg.Button('Editar', key='editset', visible=True, font='Verdana'),
         sg.Button('Editar', key='editset2', visible=False, font='Verdana'),
         sg.Button('Cancelar', key='return', font='Verdana')],
    ]
    return sg.Window('Editar Setores', layout=layout, finalize=True)


def confirmar_add_set():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Deseja mesmo confirmar essa ação?', font="Verdana")],
        [sg.Button('Confirmar', font="Verdana", key='confirmset'),
         sg.Button('Cancelar', key='return', font="Verdana"), ]
    ]
    return sg.Window('Editar Setores', layout=layout, finalize=True)


def confirmar_edit_set():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Deseja mesmo confirmar essa ação?', font="Verdana")],
        [sg.Button('Confirmar', font="Verdana", key='confirmset'),
         sg.Button('Cancelar', key='return', font="Verdana"), ]
    ]
    return sg.Window('Editar Setores', layout=layout, finalize=True)


def confirmar_exc_set():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Deseja mesmo confirmar essa ação?', font="Verdana")],
        [sg.Button('Confirmar', font="Verdana", key='confirmset'),
         sg.Button('Cancelar', key='return', font="Verdana"), ]
    ]
    return sg.Window('Editar Setores', layout=layout, finalize=True)


def janela_edit_lic():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Você atualmente está ADICIONANDO uma licença\n Preencha os campos requisitados', key='msginfo1'),
         sg.Text('Você atualmente está EDITANDO uma licença\n Preencha os campos requisitados', visible=False,
                 key='msginfo2'),
         sg.Text('Você atualmente está EXCLUIND uma licença\n Preencha os campos requisitados', visible=False,
                 key='msginfo3')],
        [sg.Text('Código da Licença ', key='txtcodlic', font="Verdana"),
         sg.Input(key='inputcodlic', size=(30, 1), font="Verdana", )],
        [sg.Text('Nome da Licença ', key='txtnomelic', visible=True, font="Verdana"),
         sg.Input(key='inputnomelic', size=(20, 1), font="Verdana")],
        [sg.Text('Data de Compra', key='txtdataclic', visible=True, font="Verdana"),
         sg.Input(key='inputdataclic', size=(11, 1), font="Verdana", disabled=False)],
        [sg.Text('Validade', key='txtvalvlic', visible=True, font="Verdana"),
         sg.Input(key='inputdatavlic', size=(11, 1), font="Verdana", disabled=False)],
        [sg.Button('Adicionar', key='addlic', visible=True, font="Verdana"),
         sg.Button('Editar', key='editlic', visible=True, font="Verdana"),
         sg.Button('Editar', key='editlic2', visible=False, font="Verdana"),
         sg.Button('Cancelar', key='return', font="Verdana")],
        [sg.Text('Algum dos valores inseridos são inválidos!', key='error', visible=False)],
    ]
    return sg.Window('Editar Licenças', layout=layout, finalize=True)


def confirmar_add_lic():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Deseja mesmo confirmar essa ação?', font="Verdana")],
        [sg.Button('Confirmar', font="Verdana", key='confirmlic'),
         sg.Button('Cancelar', key='return', font="Verdana"), ]
    ]
    return sg.Window('Editar Licenças', layout=layout, finalize=True)


def confirmar_edit_lic():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Deseja mesmo confirmar essa ação?', font="Verdana")],
        [sg.Button('Confirmar', font="Verdana", key='confirmlic'),
         sg.Button('Cancelar', key='return', font="Verdana"), ]
    ]
    return sg.Window('Editar Licenças', layout=layout, finalize=True)


def reg_manutencao():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Você atualmente está REGISTRANDO uma Manutenção\n Preencha os campos requisitados', key='msginfo1'),
         sg.Text('Você atualmente está EXCLUINDO uma manutenção\n Preencha os campos requisitados', visible=False,
                 key='msginfo2')],
        [sg.Text('Código da Manutenção', key='txtcodmanu', font="Verdana"),
         sg.Input(key='inputcodmanu', size=(30, 1), font="Verdana", )],
        [sg.Text('Código do Funcionário', key='txtcodfunc', visible=True, font="Verdana"),
         sg.Input(key='inputcodfuncmanu', size=(20, 1), font="Verdana")],
        [sg.Text('Código do Equipamento', key='txtcodequip', visible=True, font="Verdana"),
         sg.Input(key='inputcodequipmanu', size=(11, 1), font="Verdana", disabled=False)],
        [sg.Text('Código do Defeito', key='txtcoddefeito', visible=True, font="Verdana"),
         sg.Input(key='inputdefeito', size=(11, 1), font="Verdana", disabled=False)],
        [sg.Text('Código de funcionário inválido!', key='error', visible=False),
         sg.Text('Código de equipamento inválido!', key='error2', visible=False),
         sg.Text('Código de defeito inválido!', key='error3', visible=False),
         sg.Text('Código de manutenção ja existente!', key='error4', visible=False),
         sg.Text('Código de manutenção inválido!', key='error5', visible=False)],
        [sg.Button('Adicionar', key='addmanutencao', visible=True, font="Verdana"),
         sg.Button('Excluir', key='excmanutencao', visible=True, font="Verdana"),
         sg.Button('Excluir', key='excmanutencao2', visible=False, font="Verdana"),
         sg.Button('Cancelar', key='return', font="Verdana")],
    ]
    return sg.Window('Registrar Manutenção', layout=layout, finalize=True)


def confirmar_manutencao():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Deseja mesmo confirmar essa ação?', font="Verdana")],
        [sg.Button('Confirmar', font="Verdana", key='confirmmanu'),
         sg.Button('Cancelar', key='return', font="Verdana"), ]
    ]
    return sg.Window('Manutenção', layout=layout, finalize=True)


def confirmar_exc_manutencao():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Deseja mesmo confirmar essa ação?', font="Verdana")],
        [sg.Button('Confirmar', font="Verdana", key='confirmmanu'),
         sg.Button('Cancelar', key='return', font="Verdana"), ]
    ]
    return sg.Window('Manutenção', layout=layout, finalize=True)


# Declarações de Janelas
janela1, janela2, janela3, janela4, janela5, janela6, janela7, janela8, janela9, janela10, janela11, janela12, janela13, janela14, janela15, janela16, janela17, janela18, janela19, janela20 = janela_login(), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None

while True:
    window, event, values = sg.read_all_windows()
    if window == janela1:
        user = str(values['user'])
        password = str(values['password'])
    if window == janela1 and event == sg.WINDOW_CLOSED:
        break
    if window == janela2 and event == sg.WINDOW_CLOSED:
        break
    if window == janela3 and event == sg.WINDOW_CLOSED:
        break
    if window == janela2 and event == 'logout':
        break
    if window == janela16 and event == 'logout':
        break
    if window == janela17 and event == 'logout':
        break
    if window == janela1 and event == 'Login':
        if window == janela1 and values['cargos'] == 'Administrador':
            querylogin = "select codFunc, senha, funcao from funcionarios where codFunc = {} and senha = '{}' and funcao = 'Administrador'".format(
                user, password)
            cursora = con.cursor()
            cursora.execute(querylogin)
            cursora.fetchall()
            queryexibirinfos = "select * from funcionarios where codFunc = '{}' and senha = '{}'".format(user, password)
            cursor = con.cursor()
            cursor.execute(queryexibirinfos)
            linhanome = cursor.fetchall()
            for linhaname in linhanome:
                querybuscarset = "select * from setores"
                cursor = con.cursor()
                cursor.execute(querybuscarset)
                linhasset = cursor.fetchall()
                if cursora.rowcount == 1:
                    janela2 = janela_principal()
                    janela1.hide()
                else:
                    window.Element('incorrect').Update(visible=True)
        if window == janela1 and values['cargos'] == 'Coordenador':
            querylogin2 = "select codFunc, senha, funcao from funcionarios where codFunc = {} and senha = '{}' and funcao = 'Coordenador'".format(
                user, password)
            cursorb = con.cursor()
            cursorb.execute(querylogin2)
            cursorb.fetchall()
            queryexibirinfos = "select * from funcionarios where codFunc = '{}' and senha = '{}'".format(user, password)
            cursor = con.cursor()
            cursor.execute(queryexibirinfos)
            linhanome = cursor.fetchall()
            for linhaname in linhanome:
                querybuscarset = "select * from setores where codSetor = {}".format(linhaname[5])
                cursor = con.cursor()
                cursor.execute(querybuscarset)
                linhasset = cursor.fetchall()
            if cursorb.rowcount == 1:
                janela16 = janela_principal2()
                janela1.hide()
            else:
                window.Element('incorrect').Update(visible=True)
        if window == janela1 and values['cargos'] == 'Funcionario':
            querylogin3 = "select codFunc, senha, funcao from funcionarios where codFunc = {} and senha = '{}' and funcao = 'Funcionario'".format(
                user, password)
            cursorc = con.cursor()
            cursorc.execute(querylogin3)
            cursorc.fetchall()
            queryexibirinfos = "select * from funcionarios where codFunc = '{}' and senha = '{}'".format(user, password)
            cursor = con.cursor()
            cursor.execute(queryexibirinfos)
            linhanome = cursor.fetchall()
            for linhaname in linhanome:
                querybuscarset = "select * from setores where codSetor = {}".format(linhaname[5])
                cursor = con.cursor()
                cursor.execute(querybuscarset)
                linhasset = cursor.fetchall()
            if cursorc.rowcount == 1:
                janela17 = janela_principal3()
                janela1.hide()
            else:
                window.Element('incorrect').Update(visible=True)
        if window == janela1 and values['cargos'] == '':
            window.Element('incorrect').Update(visible=True)
    if window == janela2:
        for linhaset in linhasset:
            if window == janela2 and event == '{}'.format(linhaset[1]):
                querybuscarativos = "select * from equipamentos where codSetor = {}".format(linhaset[0])
                cursor.execute(querybuscarativos)
                linhasativos = cursor.fetchall()
                janela3 = janela_ativos()
            if window == janela16 and event == '{}'.format(linhaset[1]):
                querybuscarativos = "select * from equipamentos where codSetor = {}".format(linhaset[0])
                cursor.execute(querybuscarativos)
                linhasativos = cursor.fetchall()
                janela3 = janela_ativos()
            if window == janela17 and event == '{}'.format(linhaset[1]):
                querybuscarativos = "select * from equipamentos where codSetor = {}".format(linhaset[0])
                cursor.execute(querybuscarativos)
                linhasativos = cursor.fetchall()
                janela3 = janela_ativos()
    if window == janela2 and event == 'editativo':
        janela4 = add_ativos()
    if window == janela16 and event == 'editativo':
        janela4 = add_ativos()
    if window == janela3 and event == 'return':
        janela3.hide()
    if window == janela4 and event == 'add':
        novocodativov = int(values['inputcodativo'])
        novonomeativov = str(values['novonomeativo'])
        novotipoativov = str(values['novotipoativo'])
        novodataativov = str(values['novodataativo'])
        novostatusativov = str(values['statusativo'])
        inputcodsetv = str(values['inputcodset'])
        inputqtdv = int(values['inputqtd'])
        inputvalorpago = float(values['inputvalor'])
        queryverifset = "select codSetor from setores where codSetor = {}".format(inputcodsetv)
        cursor = con.cursor()
        cursor.execute(queryverifset)
        cursor.fetchall()
        if cursor.rowcount != 1:
            window.Element('error').Update(visible=False)
            window.Element('error2').Update(visible=False)
            window.Element('error3').Update(visible=True)
        elif cursor.rowcount == 1:
            queryverifativo = "select codEquip from equipamentos where codEquip = '{}'".format(novocodativov)
            cursor = con.cursor()
            cursor.execute(queryverifativo)
            cursor.fetchall()
            if values['novonomeativo'] == '' or values['novotipoativo'] == '' or values['novodataativo'] == '':
                window.Element('error').Update(visible=True)
                window.Element('error2').Update(visible=False)
                window.Element('error3').Update(visible=False)
            if cursor.rowcount == 1:
                window.Element('error').Update(visible=False)
                window.Element('error2').Update(visible=True)
                window.Element('error3').Update(visible=False)
            elif cursor.rowcount != 1:
                janela5 = confirmar_ativo_novo()
    elif window == janela4 and event == 'return':
        janela4.hide()
    if window == janela5 and event == 'confirmativo':
        queryaddativo = "INSERT INTO `equipamentos` (codEquip, nomeEquip, tipoEquip, dataCompra, statusEquip, quantidadeEquip, valorPago, codSetor) VALUES ({},'{}','{}', '{}','{}', {}, {}, {})".format(
            novocodativov, novonomeativov, novotipoativov, novodataativov, novostatusativov, inputqtdv, inputvalorpago,
            inputcodsetv, )
        cursor = con.cursor()
        cursor.execute(queryaddativo)
        con.commit()
        janela4.hide()
        janela5.hide()
    if window == janela4 and event == 'excluir':
        janela14 = add_ativos2()
        janela4.hide()
    if window == janela14 and event == 'excluir2':
        editcodativov = str(values['inputcodativo'])
        queryverfiativo = "select codEquip from equipamentos where codEquip = {} ".format(editcodativov)
        cursor = con.cursor()
        cursor.execute(queryverfiativo)
        linhas = cursor.fetchall()
        if cursor.rowcount == 1:
            janela7 = confirmar_exclusao()
        else:
            window.Element('error2').Update(visible=True)
    if window == janela14 and event == 'return':
        janela14.hide()
        janela2.un_hide()
    if window == janela7 and event == 'confirmativo':
        queryexcluirativo = "DELETE FROM equipamentos WHERE codEquip = {}".format(editcodativov)
        cursor.execute(queryexcluirativo)
        con.commit()
        janela2.un_hide()
        janela7.hide()
        janela14.hide()
    if window == janela7 and event == 'return':
        janela7.hide()
    elif window == janela5 and event == 'return':
        janela5.hide()
    # CRUD dos setores
    if window == janela2 and event == 'editset':
        janela8 = janela_edit_set()
    if window == janela8 and event == 'return':
        janela8.hide()
        janela2.un_hide()
    if window == janela8 and event == 'addset':
        editcodset = str(values['inputcodset2'])
        editnomeset = str(values['inputnomeset'])
        queryverifset = "select codSetor from setores where codSetor = {}".format(editcodset)
        cursor = con.cursor()
        cursor.execute(queryverifset)
        cursor.fetchall()
        if cursor.rowcount == 1:
            window.Element('error').Update(visible=False)
            window.Element('error2').Update(visible=True)
        elif cursor.rowcount != 1:
            if values['inputcodset2'] == '' or values['inputnomeset'] == '':
                window.Element('error').Update(visible=True)
                window.Element('error2').Update(visible=False)
            else:
                janela9 = confirmar_add_set()
    if window == janela9 and event == 'confirmset':
        queryaddset = "insert into setores (codSetor ,nomeSetor, qtdEquipamentos) values ('{}', '{}', 0)".format(
            editcodset, editnomeset)
        cursor.execute(queryaddset)
        con.commit()
        janela2.un_hide()
        janela9.hide()
        janela8.hide()
    if window == janela9 and event == 'return':
        janela9.hide()
    if window == janela8 and event == 'editset':
        window.Element('editset').Update(visible=False)
        window.Element('addset').Update(visible=False)
        window.Element('editset2').Update(visible=True)
        window.Element('txtmsginfo1').Update(visible=False)
        window.Element('txtmsginfo2').Update(visible=True)
    if window == janela8 and event == 'editset2':
        editcodset = str(values['inputcodset2'])
        editnomeset = str(values['inputnomeset'])
        queryverifset = "select codSetor from setores where codSetor = {}".format(editcodset)
        cursor = con.cursor()
        cursor.execute(queryverifset)
        cursor.fetchall()
        if cursor.rowcount != 1:
            window.Element('error').Update(visible=False)
            window.Element('error3').Update(visible=True)
        elif cursor.rowcount == 1:
            if values['inputcodset2'] == '' or values['inputnomeset'] == '':
                window.Element('error').Update(visible=True)
                window.Element('error3').Update(visible=False)
            else:
                janela10 = confirmar_add_set()
    if window == janela10 and event == 'return':
        janela10.hide()
    if window == janela10 and event == 'confirmset':
        queryeditset = "UPDATE setores SET nomeSetor = '{}' WHERE codSetor = {}".format(editnomeset, editcodset)
        cursor = con.cursor()
        cursor.execute(queryeditset)
        con.commit()
        janela10.hide()
        janela8.hide()
        janela2.un_hide()
    # CRUD Licenças
    if window == janela2 and event == 'editlic':
        janela12 = janela_edit_lic()
        janela2.hide()
    if window == janela12 and event == 'return':
        janela12.hide()
        janela2.un_hide()
    if window == janela12 and event == 'addlic':
        editcodlic = str(values['inputcodlic'])
        editnomelic = str(values['inputnomelic'])
        editdataclic = str(values['inputdataclic'])
        editdatavlic = str(values['inputdatavlic'])
        queryveriflic = "select codLisensa from lisensa where codLisensa = '{}'".format(editcodlic)
        cursor = con.cursor()
        cursor.execute(queryveriflic)
        cursor.fetchall()
        if cursor.rowcount == 1:
            window.Element('error').Update(visible=True)
        else:
            janela13 = confirmar_add_lic()
    if window == janela13 and event == 'return':
        janela13.hide()
    if window == janela13 and event == 'confirmlic':
        queryaddlic = "INSERT INTO lisensa (codLisensa, dataCompra, validade, NomeLisensa) VALUES ('{}', '{}', '{}', '{}');".format(
            editcodlic, editdataclic, editdatavlic, editnomelic)
        cursor = con.cursor()
        cursor.execute(queryaddlic)
        con.commit()
        janela13.hide()
        janela12.hide()
        janela2.un_hide()
    if window == janela12 and event == 'editlic':
        window.Element('msginfo1').Update(visible=False)
        window.Element('msginfo2').Update(visible=True)
        window.Element('addlic').Update(visible=False)
        window.Element('editlic').Update(visible=False)
        window.Element('editlic2').Update(visible=True)
        window.Element('inputdataclic').Update(disabled=True)
        window.Element('inputdatavlic').Update(disabled=True)
    if window == janela12 and event == 'editlic2':
        editcodlic = str(values['inputcodlic'])
        editnomelic = str(values['inputnomelic'])
        queryveriflic = "select codLisensa from lisensa where codLisensa = '{}'".format(editcodlic)
        cursor = con.cursor()
        cursor.execute(queryveriflic)
        cursor.fetchall()
        con.commit()
        if cursor.rowcount == 1:
            janela15 = confirmar_edit_lic()
        else:
            window.Element('error').Update(visible=True)
    if window == janela15 and event == 'confirmlic':
        queryeditlic = "UPDATE lisensa SET NomeLisensa = '{}' where codLisensa = '{}'".format(editnomelic, editcodlic)
        cursor = con.cursor()
        cursor.execute(queryeditlic)
        cursor.fetchall()
        con.commit()
        janela15.hide()
        janela12.hide()
        janela2.un_hide()
    if window == janela15 and event == 'return':
        janela15.hide()
    # Crud Manutenção
    if window == janela2 and event == 'editmanutencao':
        janela18 = reg_manutencao()
    if window == janela16 and event == 'editmanutencao':
        janela18 = reg_manutencao()
    if window == janela18 and event == 'addmanutencao':
        inputcodmanuv = int(values['inputcodmanu'])
        inputcodfuncmanuv = int(values['inputcodfuncmanu'])
        inputcodequipmanuv = int(values['inputcodequipmanu'])
        inputdefeitov = int(values['inputdefeito'])
        queryverifmanu = "select codManutencao from manutencao where codManutencao = {}".format(inputcodmanuv)
        cursord = con.cursor()
        cursord.execute(queryverifmanu)
        cursord.fetchall()
        queryveriffunc = "select codFunc from funcionarios where codFunc = {}".format(inputcodfuncmanuv)
        cursor = con.cursor()
        cursor.execute(queryveriffunc)
        cursor.fetchall()
        queryverifativo = "select codEquip from equipamentos where codEquip = {}".format(inputcodequipmanuv)
        cursorb = con.cursor()
        cursorb.execute(queryverifativo)
        cursorb.fetchall()
        queryverifdefeito = "select codDefeito from relatoriosdef where codDefeito = {}".format(inputdefeitov)
        cursorc = con.cursor()
        cursorc.execute(queryverifdefeito)
        cursorc.fetchall()
        if cursor.rowcount != 1:
            window.Element('error').Update(visible=True)
            window.Element('error2').Update(visible=False)
            window.Element('error3').Update(visible=False)
            window.Element('error4').Update(visible=False)
        elif cursor.rowcount == 1:
            if cursorb.rowcount != 1:
                window.Element('error').Update(visible=False)
                window.Element('error2').Update(visible=True)
                window.Element('error3').Update(visible=False)
                window.Element('error4').Update(visible=False)
            elif cursorb.rowcount == 1:
                if cursorc.rowcount != 1:
                    window.Element('error').Update(visible=False)
                    window.Element('error2').Update(visible=False)
                    window.Element('error3').Update(visible=True)
                    window.Element('error4').Update(visible=False)
                elif cursorc.rowcount == 1:
                    if cursord.rowcount == 1:
                        window.Element('error').Update(visible=False)
                        window.Element('error2').Update(visible=False)
                        window.Element('error3').Update(visible=False)
                        window.Element('error4').Update(visible=True)
                    else:
                        janela19 = confirmar_manutencao()
    if window == janela18 and event == 'return':
        janela18.hide()
    if window == janela19 and event == 'return':
        janela19.hide()
    if window == janela19 and event == 'confirmmanu':
        queryaddmanu = "INSERT INTO manutencao (codManutencao, codFunc, codEquip, codDefeito) VALUES ('{}', '{}', '{}', '{}')".format(
            inputcodmanuv, inputcodfuncmanuv, inputcodequipmanuv, inputdefeitov)
        cursor = con.cursor()
        cursor.execute(queryaddmanu)
        con.commit()
        janela19.hide()
        janela18.hide()
    if window == janela18 and event == 'excmanutencao':
        window.Element('msginfo1').Update(visible=False)
        window.Element('msginfo2').Update(visible=True)
        window.Element('excmanutencao').Update(visible=False)
        window.Element('excmanutencao2').Update(visible=True)
        window.Element('addmanutencao').Update(visible=False)
        window.Element('txtcodfunc').Update(visible=False)
        window.Element('txtcodequip').Update(visible=False)
        window.Element('txtcoddefeito').Update(visible=False)
        window.Element('inputcodfuncmanu').Update(visible=False)
        window.Element('inputcodequipmanu').Update(visible=False)
        window.Element('inputdefeito').Update(visible=False)
    if window == janela18 and event == 'excmanutencao2':
        inputcodmanuv = int(values['inputcodmanu'])
        queryverifmanu = "select codManutencao from manutencao where codManutencao = {}".format(inputcodmanuv)
        cursord = con.cursor()
        cursord.execute(queryverifmanu)
        cursord.fetchall()
        if cursord.rowcount == 1:
            janela20 = confirmar_exc_manutencao()
        else:
            window.Element('error5').Update(visible=True)
    if window == janela20 and event == 'return':
        janela20.hide()
    if window == janela20 and event == 'confirmmanu':
        querydeletmanutencao = "delete from manutencao where codManutencao = {}".format(inputcodmanuv)
        cursorf = con.cursor()
        cursorf.execute(querydeletmanutencao)
        con.commit()
        janela20.hide()
        janela18.hide()