TIPOS = ["Rampa de acesso", "Piso Tátil", "Calçada danificada", "Semáforo sonoro", "Outro"]
denuncias = []

def ler_inteiro(mensagem, minimo, maximo):
    while True:
        try:
            valor = int(input(mensagem))
            if minimo <= valor <= maximo:
                return valor
        except ValueError:
            pass
        print(f"Entrada inválida. Digite um número de {minimo} a {maximo}.")


def classificar(gravidade):
    if gravidade >= 4:
        return "URGENTE"
    elif gravidade == 3:
        return "Moderada"
    else:
        return "Baixa"


def cadastrar():
    local = input("Local (rua/bairro): ").strip().title()
    while not local:
        local = input("O local não pode ficar vazio. Local: ").strip().title()

    print("Tipo de problema:")
    for i, tipo in enumerate(TIPOS, 1):
        print(f"{i} - {tipo}")
    tipo = TIPOS[ler_inteiro("Escolha o tipo: ", 1, len(TIPOS)) - 1]
    gravidade = ler_inteiro("Gravidade (1 = leve, 5 = impede o acesso): ", 1, 5)

    denuncias.append([local, tipo, gravidade])
    print(f"Denúncia registrada! Classificação: {classificar(gravidade)}")


def carregar_exemplos():
    denuncias.extend([
        ["Av. Paulista", "Rampa de acesso", 5],
        ["Av. Paulista", "Piso Tátil", 4],
        ["Centro", "Calçada danificada", 3],
        ["Vila Maria", "Semáforo sonoro", 2],
        ["Av. Paulista", "Calçada danificada", 4],
    ])
    print("5 denúncias de exemplo carregadas.")


def relatorio():
    if not denuncias:
        print("Nenhuma denúncia cadastrada ainda.")
        return

    print(f"\n{'Local':<18}{'Tipo':<22}{'Grav.':<7}Classificação")
    print("-" * 60)
    for local, tipo, gravidade in denuncias:
        print(f"{local:<18}{tipo:<22}{gravidade:<7}{classificar(gravidade)}")

    total = len(denuncias)
    media = sum(d[2] for d in denuncias) / total
    locais = [d[0] for d in denuncias]
    local_critico = max(set(locais), key=locais.count)
    urgentes = sum(1 for d in denuncias if classificar(d[2]) == "URGENTE")
    percentual = urgentes / total * 100

    print("\n--- INDICADORES ---")
    print(f"Total de denúncias: {total}")
    print(f"Gravidade média: {media:.1f}")
    print(f"Local com mais denúncias: {local_critico} ({locais.count(local_critico)})")
    print(f"Denúncias urgentes: {urgentes} ({percentual:.0f}%)")
    print("Quantidade por tipo:")
    for tipo in TIPOS:
        qtd = sum(1 for d in denuncias if d[1] == tipo)
        if qtd > 0:
            print(f" - {tipo}: {qtd}")

    print("\n--- RECOMENDAÇÃO ---")
    if percentual >= 50:
        print(f"Situação crítica: priorizar intervenção imediata em '{local_critico}'.")
    elif percentual >= 25:
        print(f"Situação de atenção: programar melhorias em '{local_critico}'.")
    else:
        print(f"Situação controlada: manter monitoramento, com foco em '{local_critico}'.")


def main():
    print("=" * 60)
    print("CENTRAL DE DENÚNCIAS DE ACESSIBILIDADE URBANA")
    print("Reporte problemas de acessibilidade e ajude a reduzir")
    print("desigualdades na cidade!")
    print("=" * 60)

    opcao = -1
    while opcao != 0:
        print("\n1 - Cadastrar denúncia")
        print("2 - Consultar relatório")
        print("3 - Carregar exemplos")
        print("0 - Encerrar")
        opcao = ler_inteiro("Opção: ", 0, 3)

        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            relatorio()
        elif opcao == 3:
            carregar_exemplos()

    print("Programa encerrado. Obrigado por contribuir!")


main()