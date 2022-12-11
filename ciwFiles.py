import ciw
import matplotlib.pyplot as plt

I=0.001
Y=0.0001
R=10000
S=1500
A=30 #entre 10 et 40
A_P2 = 15 # J'utilise une autre variable
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

# Je crée un réseau juste pour la partie 2
N_P2=ciw.create_network(

    arrival_distributions=[
        ciw.dists.Exponential(rate=A_P2),#SI
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
simtime = 25 ## pour que ça soit pas trop long non plus
nbexecs = 70 ## valeur optimale trouvée avec la partie 1
prct = 2.5 ## Pourcentage de confiance

"""
DEBUT PARTIE 1
"""

"""
TACHE1 Code pour calculer les valeurs
"""
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


"""
TACHE2 Application, en trouvant la valeur optimale de répétitons
"""
# I = []
#
# simu(simtime, 1000)
#
# mean_waiting_time = sum(average_waits)/len(average_waits)
# print(f"Temps moyen d'attente: {round(mean_waiting_time, 6)} sec")
#
# confiance = mean_waiting_time*(prct/100)
# gauche = round(mean_waiting_time - confiance, 6)
# droite = round(mean_waiting_time + confiance, 6)
# I = [gauche, droite]
#
# print(I)
#
# # average_waits_dict = {}
# average_waits = []
# # simtime = 10
# nbexecs = 5
# cpt = 0
#
# while True:
#     simu(simtime, nbexecs)
#     mean_waiting_time = sum(average_waits)/len(average_waits)
#     print(f"Moyenne: {mean_waiting_time}")
#     if I[0] < mean_waiting_time < I[1]: break
#     nbexecs+=5
#
# print(f"A partir d'un temps de {nbexecs}, car il a une moyenne de séjour de {round(mean_waiting_time, 6)} sec et I = [{gauche} ; {droite}]")

"""
FIN PARTIE 1
"""

"""
DEBUT PARTIE 2
"""

"""
TACHE1 Estimation du temps de séjour avec A=15
"""
recs = []
def simu_P2(time, nb):
    sojourn_time = 0
    for i in range(nb):
        ciw.seed(i)
        Q = ciw.Simulation(N_P2)
        Q.simulate_until_max_time(time)

        recs = Q.get_all_records()
        for r in recs:
            sojourn_time += abs(r.exit_date - r.arrival_date)

        print(f"Simulation n°{i}")


    print(f"\nValeur absolue du temps de séjour, avec A=15: {round(sojourn_time, 3)}")
    print("\nCe temps est mesuré en unités discrètes, c'est-à-dire que chaque unité de temps représente une seule action dans le système.\n")
    # values = type(recs)
    # print(recs)
    # mean_performance = mean(values)
    # stdev_performance = stdev(values)
    # print(f"\nEstimation ponctuelle: {mean_performance}")
    # confidence_interval = (mean_performance - (2-(prct/100))*stdev_performance/sqrt(len(values)), mean_performance + (2-(prct/100))*stdev_performance/sqrt(len(values)))
    # print(f"\nIntervalle de confiance pour la mesure de performance: {confidence_interval}")

simu_P2(simtime, nbexecs)



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
