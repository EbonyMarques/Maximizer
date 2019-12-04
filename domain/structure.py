from domain.main import *

#results guide
#[0] - Constants([cp.Parameter(), cp.Parameter(), cp.Parameter()])
#[1] - Variables([cp.Variable(), cp.Variable(), cp.Variable()])
#[2] - Strigs(["x1","x2","x3"])

names = ["investimento", "espaço", "quantidade(s) mínima(s) de produto(s)", "quantidade(s) máxima(s) de produto(s)"]
messages = ["<!> Comecemos setando a função objetivo.",
            ">>> Para cada produto considerado, entre com seu custo e, por fim, com o montante disponível para investimento: ",
            "<!> Ótimo. Agora, tratemos das restrições!",
            ">>> Para cada produto considerado, entre com sua área e, por fim, com a área total disponível: ",
            "<!> Caso deseje adicionar restrição(ões) de quantidade(s) mínima(s), entre com aquele(s) produto(s) que terá(ão). Por exemplo: p1,p3,...\n<!> Caso não deseje, apenas tecle enter para continuar: ", 
            "<!> Caso deseje adicionar restrição(ões) de quantidade(s) máxima(s), entre com aquele(s) produto(s) que terá(ão). Por exemplo: p1,p3,...\n<!> Caso não deseje, apenas tecle enter para continuar: ",
            ">>> Entre com a quantidade mínima do produto ",
            ">>> Entre com a quantidade máxima do produto ",
            ">>> Para cada produto considerado, entre com seu lucro: ",
            "<?> Entre com 'e' para editar o problema definido ou pressione enter para voltar ao menu...",
            ">>> "]
errors = ["<!> Este produto não existe: "]

def menu():
    print("*-*"*15 + "\n")
    print("<!> Bem-vindo ao Maximizer!\n<?> O que você deseja fazer?\n\n<1> Definir novo problema...\n<2> Sair.")
    while True:
        result = decisor()
        if result == 0:
            print("<!> Opção inválida!")
            continue
        elif result == 1:
            print("\n" + "*-*"*15 + "\n")
            action = new_problem()
            #print(action)
            if action == 0:
                menu()
                break
        elif result == 2:
            print("\n<!> Obrigado por usar!")
            print("*-*"*15)
            break
        else:
            print("<!> Tente novamente!")
            continue

def decisor():
    action = input("\n"+messages[-1])
    if action == "1":
        return 1
    elif action == "2":
        return 2
    else:
        return 0
    
def new_problem():
    results = []
    constraints = []
    string_answers = []

    print("<!> Definamos um novo problema!")
    # Definição da função objetivo
    string_answers.append(
        objective(messages, results)
    )

    print(messages[2])

    # Definição da restrição de investimento
    string_answers.append(
        basic_constraint(messages[1], names[0], results, constraints, "<=")
    )

    #Definição da restrição de espaço
    string_answers.append(
        basic_constraint(messages[3], names[1], results, constraints, "<=")
    )

    #Definição da restrição de valores positivos ">=0"
    for i in range(len(results[0])):
        constraints.append(results[1][i] >= 0)
        string_answers.append(results[2][i].replace("p", "x") +" >= 0")

    #Definição da restrição de quantidades mínimas
    constraint = value_constraint([messages[4], messages[6], messages[-1]], errors, names[2], results, constraints, ">=")
    if (constraint):
        string_answers.append(constraint)

    #Definição da restrição de quantidades máximas
    constraint = value_constraint([messages[5], messages[7], messages[-1]], errors, names[3], results, constraints, "<=")
    if (constraint):
        string_answers.append(constraint)

    #Construção da função objetivo c1*x1+c2*x2+...+cn*xn
    objetivo = write_objective(results)

    #Construção e resolução do problema de maximização, utilizando a biblioteca solver
    calc_result(objetivo, constraints, string_answers, results)

    return edit_problem(objetivo, string_answers, results, constraints)

def edit_problem(objetivo, string_answers, results, constraints):
    print(messages[9])
    action = input(messages[-1])
    print()

    if action.lower() == "e":
        print("<?> O que você deseja fazer?:\n\n<1> Editar função objetivo...\n<2> Editar restrição de investimento...\n<3> Editar restrição de espaço...\n<4> Editar restrição(ões) de quantidade(s) mínima(s)...\n<5> Editar restrição(ões) de quantidade(s) máxima(s)...\n<6> Voltar ao menu...\n")
        while True:
            valor = input(messages[-1])

            #print(string_answers, results)
            if valor == "1":
                del string_answers[0]
                string_answers[0:0] = [objective(messages, results)]
                objetivo = write_objective(results)
                calc_result(objetivo, constraints, string_answers, results)
                print("<!> Função objetivo editada!")
                return edit_problem(objetivo, string_answers, results, constraints)
                break
            elif valor == "2":
                del string_answers[1]
                string_answers[1:1] = [basic_constraint(messages[1], names[0], results, constraints, "<=")]
                objetivo = write_objective(results)
                calc_result(objetivo, constraints, string_answers, results)
                print("<!> Restrição de investimento editada!")
                return edit_problem(objetivo, string_answers, results, constraints)
                break
            elif valor == "3":
                del string_answers[2]
                string_answers[2:2] = [basic_constraint(messages[3], names[1], results, constraints, "<=")]
                objetivo = write_objective(results)
                calc_result(objetivo, constraints, string_answers, results)
                print("<!> Restrição de espaço editada!")
                return edit_problem(objetivo, string_answers, results, constraints)
                break
            elif valor == "4":
                constraint = value_constraint([messages[4], messages[6], messages[-1]], errors, names[2], results, constraints, ">=", string_answers)
                if len(string_answers) > 6 and string_answers[6][0].find(">=")>=0:
                    del string_answers[6]
                    print("<!> Restrição(ões) de quantidade(s) mínima(s) antiga(s) removida(s)!")
                if (constraint):
                    string_answers[-1:-1] = [constraint]
                objetivo = write_objective(results)
                calc_result(objetivo, constraints, string_answers, results)
                return edit_problem(objetivo, string_answers, results, constraints)
                break
            elif valor == "5":
                constraint = value_constraint([messages[5], messages[7], messages[-1]], errors, names[3], results, constraints, "<=", string_answers)
                if len(string_answers) > 6 and (string_answers[6][0].find("<=")>=0 or (len(string_answers) > 7 and string_answers[7][0].find("<=")>=0)):
                    if string_answers[6][0].find("<=")>=0:
                        del string_answers[6]
                        print("<!> Restrição(ões) de quantidade(s) máxima(s) antiga(s) removida(s)!")
                    else:
                        del string_answers[7]
                        print("<!> Restrição(ões) de quantidade(s) máxima(s) antiga(s) removida(s)!")
                if (constraint):
                    string_answers.append(constraint)
                objetivo = write_objective(results)
                calc_result(objetivo, constraints, string_answers, results)
                return edit_problem(objetivo, string_answers, results, constraints)
                break
            elif valor == "6":
                return 0
                break
            else:
                print("<!> Opção inválida!")
    else:
        return 0