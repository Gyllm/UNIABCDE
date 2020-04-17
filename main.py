from estudante import Student
from professor import Teacher
import os

def cls():
  os.system('cls' if os.name=='nt' else 'clear')


menu = ('''Selecione uma opção digitando o número equivalente:
[1] - Cadastrar Aluno
[2] - Cadastrar Professor
[3] - Mostrar Informações
        1- Mostrar Informações dos Alunos
        2- Mostrar Informações dos Professores
[4] - Mostrar mensalidades
[5] - Mostrar dias de trabalho
[6] - Adicional de periculosidade
[0] - Sair do programa ''')
opção = 1
professor1 = Teacher('Marcio','99630-2010','marcio@gmail','5500.00','10-08-2019','Engenharia')
professor2 = Teacher('Carla','99630-2030','carla@gmail','5000.00','02-03-2020','Direito')
aluno1 = Student('Maria','1665','ma@gmail','001','Direito')
aluno2 = Student('Pedro','2000','pd@gmail','002','Engenharia')
while opção != 0:
    print(menu)
    opção = int(input())
    if opção==0:
        print('Sair do programa')
        cls()
        break
    elif opção==1:
        # Cadastrar Aluno (name,phone,email,ar,course)
        contador = 0
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
                    print('Opção de curso inválida')
            if contador==0:
                estudante1=Student(a[0],a[1],a[2],a[3],a[4])
                contador=contador + 1
            else:
                estudante2=Student(a[0],a[1],a[2],a[3],a[4])
                contador=contador + 1
            cls()
            print('Aluno cadastrado com sucesso!!')
            print (a)
    elif opção==2:
        # Cadastrar Professor (name,phone,email,salary,start_date,course)
        contador = 0
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
                    print('Opção de curso inválida')
            if contador==0:
                professor1=Teacher(b[0],b[1],b[2],b[3],b[4],b[5])
                contador=contador + 1
            else:
                professor2=Teacher(b[0],b[1],b[2],b[3],b[4],b[5])
                contador=contador + 1
            cls()
            print('Professor cadastrado com sucesso!!')
            print (b)
    elif opção==3:
        # Mostrar informações
        cls()
        info=int(input('''Mostrar informações
                            1- Dos alunos cadastrados
                            2- Dos professores cadastrados '''))
        if info==1:
            cls()
            print(aluno1.show_info())
            print('+' * 20)
            print(aluno2.show_info())
            print('+' * 20)
        elif info==2:
            cls()
            print(professor1.show_info())
            print('+' * 20)
            print(professor2.show_info())
            print('+' * 20)
        else:
            print('Opção inválida')
    elif opção==4:
        # Mostrar mensalidades
        cls()
        print('Segue abaixo a mensalidades dos alunos \n')
        print(aluno1.monthtly_payment())
        print('+' * 20)
        print(aluno2.monthtly_payment())
        print('+' * 20)
        print('\n')
    elif opção==5:
        # Mostrar dias de trabalho
        cls()
        print('Segue abaixo os dias de trabalho de cada professor \n')
        print(professor1.work_days())
        print('+' * 20)
        print(professor2.work_days())
        print('+' * 20)
        print('\n')
    elif opção==6:
        # Mostrar adicional de periculosidade
        cls()
        print('Segue abaixo os valores de adicional de periculosiade de cada professor \n')
        print(professor1.additional_health_hazard())
        print('+' * 20)
        print(professor2.additional_health_hazard())
        print('+' * 20)
        print('\n')
    else:
        cls()
        print('Opção inválida! Escolha uma opção válida do menu')