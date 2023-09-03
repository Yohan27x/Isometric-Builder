# import random
# from random import randrange

# class Rect:
#     def __init__(self,width,height, num):
#         self.width = width
#         self.height = height
#         self.num = num


# rect_list = []

# for x in range(15):
#     for y in range(15):
#         #duration =  random.randrange(1300,2700)
#         rect = Rect(random.randrange(0,5), random.randrange(0,5), random.randrange(0,5))
#         rect_list.append(rect)

# for rect in rect_list:
#     print("rect : ", rect.width , "/", rect.height)

# print("----------------------------------------")

# rect_list.sort(key=lambda rect: (rect.num, rect.width, rect.height), reverse=False)


# for rect in rect_list:
#     print("rect : ", rect.num, "/", rect.width , "/", rect.height)



# def eratostene(n):
#     boolean_table = [False, False]
#     for i in range(2,n+1):
#         boolean_table.append(True)
            
#     for i in range(2,n+1):
#         # print(boolean_table[i-2])
#         if boolean_table[i] == True:
#             for j in range(len(boolean_table)):
#                 if(j != i):
#                     if(j%(i) == 0):
#                         boolean_table[j] = False
                        
#     print("boolean_table : ", boolean_table)
#     primes = []
#     for i in range(n+1):
#         if (boolean_table[i] == True):
#             primes.append(i)

#     return primes
                

# def test_eratostene():
#     primes = eratostene(30)
#     print(primes)

# test_eratostene()


# magical_square1 = [[1,8,11,14],[15,10,5,4],[6,3,16,9],[12,13,2,7]]
# carre_pas_mag = [[10,8,11,14],[15,1,5,4],[6,3,16,9],[12,13,2,7]]

# def display_as_square(square):
#     for row in square:
#         for num in row:
#             print(num, end='  ')
#         print(" ")


# display_as_square(magical_square1)
# print(" ")
# display_as_square(carre_pas_mag)
        
# def has_all_row_same(square):

#     square_copy = square.copy()

#     if(len(square_copy) != 0):
#         has_same = True

#         sum_first_row = 0
#         for num in square_copy[0]:
#             sum_first_row += num
#         square_copy.pop(0)
      
#         for row in square_copy:
#             sum_row = 0
#             for num in row:
#                 sum_row += num
#             if(sum_row != sum_first_row):
#                 has_same = False
    
#         if(has_same == False):
#             return False
#         else:
#             return sum_row
        
#     else:
#         return False


# print(has_all_row_same(magical_square1))

# def has_all_columns_same_sum(square):

#     if(len(square[0]) != 0):
        
#         has_same = True
#         sum_first_col = 0
#         for row in square:
#             sum_first_col += row[0]
     
#         for i in range(len(square)):
#             if(i >= 1):
#                 sum_col = 0
#                 for j,row in enumerate(square):
#                     # print("square[j][0] : ", square[j][i])
#                     sum_col += square[j][i]
#                 # print("sum_col / sum_first_col : ", sum_col , "/", sum_first_col)
#                 if(sum_col != sum_first_col):
#                     has_same = False

    
#         if(has_same == False):
#             return False
#         else:
#             return sum_col
            
#     else:
#         return False


# # print(has_all_columns_same_sum(magical_square1))


# def has_same_diagonals(square):

#     if(len(square)!=0):
       
#         first_diago = 0
#         for i in range(len(square)):
#             print(square[i][i])
#             first_diago += square[i][i]

#         scd_diago = 0
#         i = 0
#         j = len(square)-1
#         for z in range(len(square)):
#             print(square[i][j])
#             scd_diago += square[i][j]
#             i += 1
#             j -= 1
          

#     if(scd_diago == first_diago):
#         return scd_diago
#     else:
#         return False


      
# # print(has_same_diagonals(magical_square1))


# # def is_square_magical(square):

# #     const1 = has_all_row_same(square)
# #     const2 = has_all_columns_same_sum(square)
# #     const3 = has_same_diagonals(magical_square1)

# #     if(const1 == const2 and const1 == const3):
# #         return True
# #     else:
# #         return False
    
# # print(is_square_magical(carre_pas_mag))


# 1. Créez une liste « customers» contenant les tuples «(1, Paul), (2, Ali), (3, Julia), (4, Noah), (5, Janet) ».

# 2. Créer une seconde liste « accounts»  contenant le solde de chaque compte.  
# Le solde du compte courant est un réel aléatoire entre 0 et 10 000 arrondie à 2 chiffres après la virgule. 

# 3. Créez une fonction « max_balance(customers, balance) » qui retourne le client avec le plus grand solde.

import random


# customers = [(1, "Paul"), (2, "Ali"), (3, "Julia"), (4, "Noah"), (5, "Janet")]
# accounts = []
# for customer in customers:
#     accounts.append(round(random.uniform(0,4000),2))

# print(customers)
# print(accounts)

# def max_balance(customers, balance):

#     max_balance = balance[0]
#     customer = customers[0]

#     for i,account in enumerate(balance):
#         if account > max_balance:
#             max_balance = account
#             customer = customers[i]

#     return customer


# max_balance(customers, accounts)



#  Les variables customers et account de l'exercice précédent ont été recréées (mais ne sont pas visible par vous).

# # 1. Créez une fonction « Stockage_Dict(clients,compte_courant) » qui retourne un dictionnaire contenant
#  trois items {« clients » : clients, « courant » : compte_courant, « épargne » : compte_épargne }. Le compte épargne
# correspond à une liste de réels aléatoires entre 0 et 40 000.

# 2. Créez une fonction « Max_Dic (dico) » qui prend en paramètres le dictionnaire contenant les clients et leurs comptes.
#  Cette fonction retourne le client ayant le solde maximal, c’est-à-dire la somme de ces deux comptes est maximale. 

# 3. Le client « Paul » a reçu un virement de 500 euros dans son compte, les autres clients ont tous reçu un prélèvement de 3000 euros.
#  Créer une fonction « M_A_J (dico) » qui met à jour les comptes des clients et qui retourne le nouveau dictionnaire.

# 4. Écrire une fonction “Ajout_Decouvert” qui ajoute un item dans le dictionnaire. L’item corresponds à « découvert : liste »,
#   la valeur de l’item est une liste stockant les clients à découvert (i.e. compte_courant < 0 ).


# customers = [(1, "Paul"), (2, "Ali"), (3, "Julia"), (4, "Noah"), (5, "Janet")]
# accounts = []
# for customer in customers:
#     accounts.append(round(random.uniform(0,4000),2))


# def Stockage_dict(clients, compte_courant):

#     dict_info = {}

#     dict_info["clients"] = []
#     for client in clients:
#         dict_info["clients"].append(client)

#     dict_info["courant"] = []
#     for courant in compte_courant:
#         dict_info["courant"].append(courant)

#     dict_info["epargne"] = []
#     for i in range(len(clients)):
#        dict_info["epargne"].append(random.uniform(0,40000))


#     return dict_info

# dico = Stockage_dict(customers, accounts)
# print(dico)

# def Max_Dic(dico):

#     max_sum = dico["courant"][0] + dico["epargne"][0]
#     max_client = dico["clients"][0]

#     for i in range(len(dico["courant"])):
#         new_max_sum = dico["courant"][i] + dico["epargne"][i]
#         if(new_max_sum > max_sum):
#             max_sum = new_max_sum
#             max_client = dico["clients"][i]


#     return max_client


# print(Max_Dic(dico))


# # 3. Le client « Paul » a reçu un virement de 500 euros dans son compte, les autres clients ont tous reçu un prélèvement de 3000 euros.
# #  Créer une fonction « M_A_J (dico) » qui met à jour les comptes des clients et qui retourne le nouveau dictionnaire.

# def M_A_J(dico):

#     for i,client in enumerate(dico["clients"]):
#         if(client[1] == "Paul"):
#             dico["courant"][i] += 500
#         else:
#             dico["courant"][i] += 3000


# M_A_J(dico)
# print(dico)


# # 4. Écrire une fonction “Ajout_Decouvert” qui ajoute un item dans le dictionnaire. L’item corresponds à « découvert : liste »,
# #   la valeur de l’item est une liste stockant les clients à découvert (i.e. compte_courant < 0 ).

# def Ajout_Decouvert(dico):
#     dico["découvert"] = []
#     for i,courant in enumerate(dico["courant"]):
#         if courant < 0:
#             dico["découvert"].append(dico["clients"][i])


# Ajout_Decouvert(dico)
# print(dico)




# On dispose d'un fichier grades.txt contenant des notes de différents étudiants. Le format du fichier est le suivant : 

# Paul: 10, 11, 15
# Jennifer: 11, 13, 14
# etc.etc.

# 1. Faire une fonction parse_grades(path) qui renvoie une liste de dictionnaire. Chaque dictionnaire devra avoir la structure suivante : 

# {

#      student_name: lenom,

#     grades: liste de notes

# }

# Penser à fermer votre fichier que ce soit manuellement ou automatiquement grace à with


# 2. Utiliser la fonction et stocker le résultat dans une variable student_grades

l = ['element1\t0238.94', 'element2\t2.3904', 'element3\t0139847']
print([i.split('\t')[0] for i in l])


