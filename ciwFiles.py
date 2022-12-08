import ciw
import matplotlib.pyplot as plt

I=0.001
Y=0.0001
R=10000
S=1500
A=30 #entre 10 et 40
C=707
B=16
F=42.2
N=ciw.create_network(

    arrival_distributions=[
        ciw.dists.Exponential(rate=A),#SI
        ciw.dists.NoArrivals(),#SR
        ciw.dists.NoArrivals(),#SS
        ciw.dists.NoArrivals()],#SC

    service_distributions=[
        ciw.dists.Deterministic(value=I),#SI
        ciw.dists.Exponential(rate=1/(Y+B/R)),#SR
        ciw.dists.Deterministic(value=B/S),#SS
        ciw.dists.Deterministic(value=B/C)],#SC

    routing=[
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [0, B/F, 0, 0]],

    number_of_servers=[1, 1, 1, 1]

)



average_waits_dict = {}
average_waits = []
simtime = 5
nbexecs = 1



def simu(time, nb):
    for i in range(nb):
        ciw.seed(i)
        Q = ciw.Simulation(N)
        Q.simulate_until_max_time(time)
        recs = Q.get_all_records()
        waits = [r.waiting_time for r in recs]
        mean_waits = sum(waits)/len(waits)
        print(f"Simulation n°{i}: {round(mean_waits, 6)} sec")
        average_waits_dict[f"{time}"] = mean_waits
        average_waits.append(mean_waits)

# while nbexecs <= 600:
#      simu(simtime, nbexecs)
#      nbexecs+=10

# while simtime <= 100:
#      simu(simtime, nbexecs)
#      simtime+=10



# print(average_waits)
#
# graph = average_waits.items()
# x, y = zip(*graph)
#
# plt.plot(x, y)
# # plt.show()

I = []

simu(simtime, 1000)

mean_waiting_time = sum(average_waits)/len(average_waits)
print(f"Temps moyen d'attente: {round(mean_waiting_time, 6)} sec")

prct = 2.5
confiance = mean_waiting_time*(prct/100)
gauche = round(mean_waiting_time - confiance, 6)
droite = round(mean_waiting_time + confiance, 6)
I = [gauche, droite]

print(I)

# average_waits_dict = {}
average_waits = []
# simtime = 10
nbexecs = 5

cpt = 0
while True:
    simu(simtime, nbexecs)
    mean_waiting_time = sum(average_waits)/len(average_waits)
    print(f"Moyenne: {mean_waiting_time}")
    if I[0] < mean_waiting_time < I[1]: break
    nbexecs+=5
print(f"A partir d'un temps de {nbexecs}, car il a une moyenne de séjour de {round(mean_waiting_time, 6)} sec et I = [{gauche} ; {droite}]")

##------------------------##
##---------Tache1---------##
# On a réalisé 2 graphes différents:
# - l'un où on visualise que 50 itérations de l'algorithme permettant de trouver le temps moyen de séjour, suffisent largement.
# En effet, on découvre, qu'on fasse 50 ou 500 itérations, le temps moyen restera toujours du même ordre de grandeur.
# Donc pour une question d'optimisation, le graphe sert à confirmer qu'on peut faire seulement 50 itérations.
# - l'autre graphe montre que le temps moyen de séjour est proportionnel au temps de la simulation.

##------------------------##
##---------Tache2---------##
# Pour cette tâche, il faut établir un intervalle de confiance, si on prend par exemple 5%, on doit vérifier à partir de quel nombre de répitions de simulations, le temps moyen de séjour se situe dans cet intervalle.
# Pour ceci, on fait une 1000 simulations, d'un temps quelconque, ces 1000 simulations corresponderont à la valeur réelle.
# A partir de ces 1000 simulations, on établit un intervalle de confiance:
# I = [tps_moyen_sjr_reel - 5%; tps_moyen_sjr_reel + 5%]
#
# On vérifie ensuite à partir de quel nombre de simulations, on a tps_moyen_sjr_theoX appartient à I (à partir de quel indice)
