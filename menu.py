from banco import *

def menu_principal():
    while True:
        print("\n=== SISTEMA DE CLÍNICA ===")
        print("1. Pacientes")
        print("2. Médicos")
        print("3. Consultas")
        print("4. Lembretes")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_paciente()
        elif opcao == "2":
            menu_medico()
        elif opcao == "3":
            menu_consulta()
        elif opcao == "4":
            menu_lembrete()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

def exibir_pacientes(pacientes):
    if not pacientes:
        print("Nenhum paciente encontrado.")
        return
    print("\n--- LISTA DE PACIENTES ---")
    for paciente in pacientes:
        print(f"ID: {paciente[0]}, Nome: {paciente[1]}, Email: {paciente[2]}")

def menu_paciente():
    while True:
        try:
            print("\n--- PACIENTES ---")
            print("1. Inserir paciente")
            print("2. Alterar paciente")
            print("3. Excluir paciente")
            print("4. Consultar paciente por ID")
            print("5. Consultar todos os pacientes")
            print("0. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":  
                try:
                    nome = input("Digite o nome do paciente: ")
                    email = input("Digite o email do paciente: ")
                    paciente = {
                        "nm_paciente": nome,
                        "nm_email": email
                    }
                    insere_paciente(paciente)
                    print(f"Paciente inserido com sucesso! ID: {paciente['id']}")
                except Exception as e:
                    print(f"Erro ao inserir paciente: {e}")
            elif opcao == "2":  
                try:
                    id_paciente = input("Digite o ID do paciente a ser atualizado: ")
                    nome = input("Digite o novo nome do paciente: ")
                    email = input("Digite o novo email do paciente: ")
                    paciente = {
                        "id": int(id_paciente),
                        "nm_paciente": nome,
                        "nm_email": email
                    }
                    atualizar_paciente(paciente)
                    print("Paciente atualizado com sucesso!")
                except Exception as e:
                    print(f"Erro ao atualizar paciente: {e}")
            elif opcao == "3":  
                try:
                    id_paciente = input("Digite o ID do paciente a ser excluído: ")
                    deletar_paciente(int(id_paciente))
                    print("Paciente deletado com sucesso!")
                except Exception as e:
                    print(f"Erro ao deletar paciente: {e}")
            elif opcao == "4":  
                try:
                    id_paciente = input("Digite o ID do paciente: ")
                    paciente = consultar_paciente_id(id_paciente)
                    exibir_pacientes([paciente] if paciente else [])
                except Exception as e:
                    print(f"Erro ao consultar paciente por ID: {e}")
            elif opcao == "5":  
                try:
                    pacientes = consultar_paciente()
                    exibir_pacientes(pacientes)
                except Exception as e:
                    print(f"Erro ao consultar todos os pacientes: {e}")
            elif opcao == "0":  
                break
            else:
                print("Opção inválida! Tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

def exibir_medicos(medicos):
    if not medicos:
        print("Nenhum médico encontrado.")
        return
    print("\n--- LISTA DE MÉDICOS ---")
    for medico in medicos:
        print(f"ID: {medico[0]}, Nome: {medico[1]}, Especialidade: {medico[2]}")

def menu_medico():
    while True:
        try:
            print("\n--- MÉDICOS ---")
            print("1. Inserir médico")
            print("2. Alterar médico")
            print("3. Excluir médico")
            print("4. Consultar médico por ID")
            print("5. Consultar todos os médicos")
            print("0. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1": 
                try:
                    nome = input("Digite o nome do médico: ")
                    especialidade = input("Digite a especialidade do médico: ")
                    medico = {
                        "nm_medico": nome,
                        "nm_especialidade": especialidade
                    }
                    insere_medico(medico)
                    print(f"Médico inserido com sucesso! ID: {medico['id']}")
                except Exception as e:
                    print(f"Erro ao inserir médico: {e}")
            elif opcao == "2": 
                try:
                    id_medico = input("Digite o ID do médico a ser atualizado: ")
                    nome = input("Digite o novo nome do médico: ")
                    especialidade = input("Digite a nova especialidade do médico: ")
                    medico = {
                        "id": int(id_medico),
                        "nm_medico": nome,
                        "nm_especialidade": especialidade
                    }
                    atualizar_medico(medico)
                    print("Médico atualizado com sucesso!")
                except Exception as e:
                    print(f"Erro ao atualizar médico: {e}")
            elif opcao == "3":  
                try:
                    id_medico = input("Digite o ID do médico a ser excluído: ")
                    deletar_medico(int(id_medico))
                    print("Médico deletado com sucesso!")
                except Exception as e:
                    print(f"Erro ao deletar médico: {e}")
            elif opcao == "4":  
                try:
                    id_medico = input("Digite o ID do médico: ")
                    medico = consultar_medico_id(id_medico)
                    exibir_medicos([medico] if medico else [])
                except Exception as e:
                    print(f"Erro ao consultar médico por ID: {e}")
            elif opcao == "5": 
                try:
                    medicos = consultar_medico()
                    exibir_medicos(medicos)
                except Exception as e:
                    print(f"Erro ao consultar todos os médicos: {e}")
            elif opcao == "0":  
                break
            else:
                print("Opção inválida! Tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

def exibir_consultas(consultas):
    if not consultas:
        print("Nenhuma consulta encontrada.")
        return
    print("\n--- LISTA DE CONSULTAS ---")
    for consulta in consultas:
        print(f"ID: {consulta[0]}, Paciente ID: {consulta[1]}, Médico ID: {consulta[2]}, "
              f"Data/Hora: {consulta[3]}, Tipo: {consulta[4]}, Status: {consulta[5]}")

def menu_consulta():
    while True:
        try:
            print("\n--- CONSULTAS ---")
            print("1. Inserir consulta")
            print("2. Alterar consulta")
            print("3. Excluir consulta")
            print("4. Consultar consulta por ID")
            print("5. Consultar todas as consultas")
            print("0. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":  
                try:
                    id_paciente = int(input("Digite o ID do paciente: "))
                    id_medico = int(input("Digite o ID do médico: "))
                    dt_hora = input("Digite a data e hora da consulta (AAAA-MM-DD HH:MM): ")
                    tp_consulta = input("Digite o tipo da consulta: ")
                    st_confirmacao = input("Digite o status da confirmação (P/C/D): ")

                    consulta = {
                        "id_paciente": id_paciente,
                        "id_medico": id_medico,
                        "dt_hora": dt_hora,
                        "tp_consulta": tp_consulta,
                        "st_confirmacao": st_confirmacao
                    }
                    insere_consulta(consulta)
                    print(f"Consulta inserida com sucesso! ID: {consulta['id']}")
                except Exception as e:
                    print(f"Erro ao inserir consulta: {e}")
            elif opcao == "2":  
                try:
                    id_consulta = int(input("Digite o ID da consulta a ser atualizada: "))
                    id_paciente = int(input("Digite o novo ID do paciente: "))
                    id_medico = int(input("Digite o novo ID do médico: "))
                    dt_hora = input("Digite a nova data e hora da consulta (AAAA-MM-DD HH:MM): ")
                    tp_consulta = input("Digite o novo tipo da consulta: ")
                    st_confirmacao = input("Digite o novo status da confirmação (P/C/D): ")

                    consulta = {
                        "id": id_consulta,
                        "id_paciente": id_paciente,
                        "id_medico": id_medico,
                        "dt_hora": dt_hora,
                        "tp_consulta": tp_consulta,
                        "st_confirmacao": st_confirmacao
                    }
                    atualizar_consulta(consulta)
                    print("Consulta atualizada com sucesso!")
                except Exception as e:
                    print(f"Erro ao atualizar consulta: {e}")
            elif opcao == "3": 
                try:
                    id_consulta = int(input("Digite o ID da consulta a ser excluída: "))
                    deletar_consulta(id_consulta)
                    print("Consulta deletada com sucesso!")
                except Exception as e:
                    print(f"Erro ao deletar consulta: {e}")
            elif opcao == "4":  
                try:
                    id_consulta = int(input("Digite o ID da consulta: "))
                    consulta = consultar_consulta_id(id_consulta)
                    exibir_consultas([consulta] if consulta else [])
                except Exception as e:
                    print(f"Erro ao consultar consulta por ID: {e}")
            elif opcao == "5": 
                try:
                    consultas = consultar_consulta()
                    exibir_consultas(consultas)
                except Exception as e:
                    print(f"Erro ao consultar todas as consultas: {e}")
            elif opcao == "0":  
                break
            else:
                print("Opção inválida! Tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

def exibir_lembretes(lembretes):
    if not lembretes:
        print("Nenhum lembrete encontrado.")
        return
    print("\n--- LISTA DE LEMBRETES ---")
    for lembrete in lembretes:
        print(f"ID: {lembrete[0]}, ID da Consulta: {lembrete[1]}, Data de Criação: {lembrete[2]}")

def menu_lembrete():
    while True:
        try:
            print("\n--- LEMBRETES ---")
            print("1. Inserir lembrete")
            print("2. Alterar lembrete")
            print("3. Excluir lembrete")
            print("4. Consultar lembrete por ID")
            print("5. Consultar todos os lembretes")
            print("0. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                try:
                    id_consulta = int(input("Digite o ID da consulta relacionada ao lembrete: "))
                    lembrete = {"id_consulta": id_consulta}
                    insere_lembrete(lembrete)
                    print(f"Lembrete inserido com sucesso! ID: {lembrete['id']}")
                except Exception as e:
                    print(f"Erro ao inserir lembrete: {e}")
            elif opcao == "2":
                try:
                    id_lembrete = int(input("Digite o ID do lembrete a ser atualizado: "))
                    id_consulta = int(input("Digite o novo ID da consulta: "))
                    lembrete = {"id": id_lembrete, "id_consulta": id_consulta}
                    atualizar_lembrete(lembrete)
                    print("Lembrete atualizado com sucesso!")
                except Exception as e:
                    print(f"Erro ao atualizar lembrete: {e}")
            elif opcao == "3":
                try:
                    id_lembrete = int(input("Digite o ID do lembrete a ser excluído: "))
                    deletar_lembrete(id_lembrete)
                    print("Lembrete deletado com sucesso!")
                except Exception as e:
                    print(f"Erro ao deletar lembrete: {e}")
            elif opcao == "4":
                try:
                    id_lembrete = int(input("Digite o ID do lembrete: "))
                    lembrete = consultar_lembrete_id(id_lembrete)
                    exibir_lembretes([lembrete] if lembrete else [])
                except Exception as e:
                    print(f"Erro ao consultar lembrete por ID: {e}")
            elif opcao == "5":
                try:
                    lembretes = consultar_lembrete()
                    exibir_lembretes(lembretes)
                except Exception as e:
                    print(f"Erro ao consultar todos os lembretes: {e}")
            elif opcao == "0":
                break
            else:
                print("Opção inválida! Tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    menu_principal()
