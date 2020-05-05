from estudante import Student
from professor import Teacher
import os

def cls():
  os.system('cls' if os.name=='nt' else 'clear')


cls()
menu = ('''Selecione uma opção digitando o número equivalente:
[1] - Cadastrar Aluno
[2] - Cadastrar Professor
[3] - Mostrar Informações
        1- Mostrar Informações dos Alunos
        2- Mostrar Informações dos Professores
[4] - Mostrar mensalidades
[5] - Mostrar dias de trabalho
[6] - Adicional de periculosidade
[7] - Cadastrar usuário
[8] - Efetuar Login
[0] - Sair do programa ''')
us=''
sn=''
opção = 1
aluno1 = ''
aluno2 = ''
professor1 = ''
professor2 = ''
#professor1 = Teacher('Marcio','99630-2010','marcio@gmail','5500.00','10-08-2019','Engenharia')
#professor2 = Teacher('Carla','99630-2030','carla@gmail','5000.00','02-03-2020','Direito')
while opção != 0:
    print(menu)
    opção = int(input())
    if opção==0:
        print('Sair do programa')
        cls()
        break
    elif opção==1:
        # Cadastrar Aluno (name,phone,email,ar,course)
        if len(us) + len(sn) == 0:
            cls()
            print('Efetue Login para continuar \n')
        else:
            cls()
            contador = 0
            if len(Student)>=10:
                print('Já existem 2 alunos cadastrados!! \n')
            else:
                if len(Student)>=4:
                    contador = 1
                a=[]
                while contador < 2:
                    if contador == 0:
                        print('Cadastrar o primeiro Aluno')
                    else:
                        print('Cadastrar o segundo Aluno')
                    a.append((input('Digite o nome do aluno ')))
                    a.append((input('Digite o telefone do aluno ')))
                    a.append((input('Digite o email do aluno ')))
                    a.append((input('Digite o RA do aluno ')))
                    curso = 1
                    while curso != 0:
                        curso = int(input('Escolha o curso do aluno \n 1-Engenharia \n 2-Direito \n 3-Pedagogia '))
                        if curso == 1:
                            a.append('Engenharia')
                            curso=0
                        elif curso == 2:
                            a.append('Direito')
                            curso=0
                        elif curso == 3:
                            a.append('Pedagogia')
                            curso=0
                        else:
                            print('Opção de curso inválida \n')
                    if contador==0:
                        aluno1=Student(a[0],a[1],a[2],a[3],a[4])
                        contador=contador + 1
                    else:
                        aluno2=Student(a[0],a[1],a[2],a[3],a[4])
                        contador=contador + 1
                    cls()
                    print('Aluno cadastrado com sucesso!! \n')
                    print (a)
    elif opção==2:
        # Cadastrar Professor (name,phone,email,salary,start_date,course)
        if len(us) + len(sn) == 0:
            cls()
            print('Efetue Login para continuar \n')
        else:
            cls()
            contador = 0
            if len(Teacher)>=14:
                print('Já existem 2 professores cadastrados!! \n')
            else:
                if len(Teacher)>=6:
                    contador = 1
                b=[]
                while contador < 2:
                    if contador == 0:
                        print('Cadastrar o primeiro Professor')
                    else:
                        print('Cadastrar o segundo Professor')
                    b.append((input('Digite o nome do professor ')))
                    b.append((input('Digite o telefone do professor ')))
                    b.append((input('Digite o email do professor ')))
                    b.append((input('Digite o salário do professor ')))
                    b.append(input('Digite a data de inicio na função do professor '))
                    curso = 1
                    while curso != 0:
                        curso = int(input('Escolha o curso do aluno \n 1-Engenharia \n 2-Direito \n 3-Pedagogia '))
                        if curso == 1:
                            b.append('Engenharia')
                            curso=0
                        elif curso == 2:
                            b.append('Direito')
                            curso=0
                        elif curso == 3:
                            b.append('Pedagogia')
                            curso=0
                        else:
                            print('Opção de curso inválida \n')
                    if contador==0:
                        professor1=Teacher(b[0],b[1],b[2],b[3],b[4],b[5])
                        contador=contador + 1
                    else:
                        professor2=Teacher(b[0],b[1],b[2],b[3],b[4],b[5])
                        contador=contador + 1
                    cls()
                    print('Professor cadastrado com sucesso!! \n')
                    print (b)
    elif opção==3:
        # Mostrar informações
        if len(us) + len(sn) == 0:
            cls()
            print('Efetue Login para continuar \n')
        else:
            cls()
            info=int(input('''Mostrar informações
                                1- Dos alunos cadastrados
                                2- Dos professores cadastrados '''))
            if info==1:
                #Informação dos alunos cadastrados
                cls()
                if len(aluno2)>1:
                    print(aluno1.show_info())
                    print('+' * 20)
                    print(aluno2.show_info())
                    print('+' * 20)
                elif len(aluno1)>1:
                    print(aluno1.show_info())
                    print('+' * 20)
                else:
                    print('Ainda não foi cadastrado nenhum aluno \n')
            elif info==2:
                #Informação dos professores cadastrados
                cls()
                if len(professor2)>1:
                    print(professor1.show_info())
                    print('+' * 20)
                    print(professor2.show_info())
                    print('+' * 20)
                elif len(professor1)>1:
                    print(professor1.show_info())
                    print('+' * 20)
                else:
                    print('Ainda não foi cadastrado nenhum professor \n')
            else:
                print('Opção inválida \n')
    elif opção==4:
        # Mostrar mensalidades
        if len(us) + len(sn) == 0:
            cls()
            print('Efetue Login para continuar \n')
        else:
            if len(aluno2)>1:
                cls()
                print('Segue abaixo a mensalidades dos alunos \n')
                print(aluno1.monthtly_payment())
                print('+' * 20)
                print(aluno2.monthtly_payment())
                print('+' * 20)
                print('\n')
            elif len(aluno1)>1:
                cls()
                print('Segue abaixo a mensalidades dos alunos \n')
                print(aluno1.monthtly_payment())
                print('+' * 20)
            else:
                print('Ainda não foi cadastrado nenhum aluno \n')
    elif opção==5:
        # Mostrar dias de trabalho
        if len(us) + len(sn) == 0:
            cls()
            print('Efetue Login para continuar \n')
        else:
            if len(professor2)>1:
                cls()
                print('Segue abaixo os dias de trabalho de cada professor \n')
                print(professor1.work_days())
                print('+' * 20)
                print(professor2.work_days())
                print('+' * 20)
                print('\n')
            elif len(professor1)>1:
                cls()
                print('Segue abaixo os dias de trabalho de cada professor \n')
                print(professor1.work_days())
                print('+' * 20)
            else:
                print('Ainda não foi cadastrado nenhum professor \n')
    elif opção==6:
        # Mostrar adicional de periculosidade
        if len(us) + len(sn) == 0:
            cls()
            print('Efetue Login para continuar \n')
        else:
            if len(professor2)>1:
                cls()
                print('Segue abaixo os valores de adicional de periculosiade de cada professor \n')
                print(professor1.additional_health_hazard())
                print('+' * 20)
                print(professor2.additional_health_hazard())
                print('+' * 20)
                print('\n')
            elif len(professor1)>1:
                cls()
                print('Segue abaixo os valores de adicional de periculosiade de cada professor \n')
                print(professor1.additional_health_hazard())
                print('+' * 20)
            else:
                print('Ainda não foi cadastrado nenhum professor \n')
    elif opção==7:
        # Cadastrar novo usuário
        cls()
        u = input('Digite um nome de usuário ')
        sp = input('Digite uma senha ')
        ss = input('Repita a senha ')
        if sp != ss:
            print('As senhas escolhidas não são iguais')
            sp = input('Digite uma senha ')
            ss = input('Repita a senha ')
        else:
            f = open('cadastro.txt','w')
            f.write(u)
            f.write('\n')
            f.write(sp)
            f.close
            print('Usuário cadastrado com sucesso \n')
    elif opção==8:
        # Efetuar login
        cls()
        print('EFETUAR LOGIN')
        us = input('Digite o usuario ')
        sn = input('Digite a senha ')
        f = open('cadastro.txt','r')
        nm = f.read(len(us))
        esp = f.read(1)
        pw = f.read(len(sn))
        f.close
        if nm == us:
            if pw != sn:
                cls()
                print('Senha não confere')
                us=''
                sn=''
            else:
                cls()
                print('Login efetuado com sucesso!! \n')
        else:
            cls()
            print('Usuario não cadastrado \n')
    else:
        cls()
        print('Opção inválida! Escolha uma opção válida do menu \n')