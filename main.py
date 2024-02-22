def demander_reponse_num_utilisateur(min, max):
    reponse_str = input("votre réponse (entre " + str(min)+" et "+str(max)+"): ")
    try:
         reponse_int = int(reponse_str)
         if min <= reponse_int <= max:
             return reponse_int
         print("ERREUR: Veuillez rentrer un nombre entre ",min," et ",max)
    except:
        print("ERREUR: Veuillez rentrer uniquement des chiffres")
    return demander_reponse_num_utilisateur(min, max)


def poser_question(question):
    bonne_reponse = question[3]
    print("QUESTION :")
    print(" ",question[0])
    for i in range(1,len(question)):
        print(" ",i,"-",question[i])

    print()

    resultat_reponse_correcte = False
    reponse_int = demander_reponse_num_utilisateur(1, len(question)-1)

    if question[reponse_int].lower() == bonne_reponse.lower() :
        print("bonne reponse")
        resultat_reponse_correcte = True
    else:
        print("mauvaise reponse")

    print()
    return resultat_reponse_correcte

def lancer_questionnaire(questionnaire):
    score = 0
    for question in questionnaire:
        if poser_question(question):
            score += 1
    print("Score final :",score)

questionnaire = (
    ["Quelle est la capitale de la France ?","Marseile","Nice","Paris","Nantes"], 
    ["Quelle est la capitale de l'italie ?","Pise","Venise","Rome","Florence"], 
    ("Quelle est la capitale de la Belgique ?","Anvers","Bruges","Bruxelle","Liege"))

lancer_questionnaire(questionnaire)

