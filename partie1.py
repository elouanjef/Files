import ciw
import matplotlib.pyplot as plt
from networking import NetworkValues
from values import Values

"""
--------------------------Tache1--------------------------------
On a réalisé 2 graphes différents:
- l'un où on visualise que 50 itérations de l'algorithme permettant de trouver le temps moyen de séjour, suffisent largement.
En effet, on découvre, qu'on fasse 50 ou 500 itérations, le temps moyen restera toujours du même ordre de grandeur.
Donc pour une question d'optimisation, le graphe sert à confirmer qu'on peut faire seulement 50 itérations.
- l'autre graphe montre que le temps moyen de séjour est proportionnel au temps de la simulation.
"""

"""
DEBUT PARTIE 1
"""

v = Values()
n = NetworkValues()
n.set_A(30)
n.reset_network()
tache = "tache1"

"""
Code /
"""

def simu(time, nb):
    for i in range(nb):
        ciw.seed(i)
        Q = ciw.Simulation(n.N)
        Q.simulate_until_max_time(time)
        recs = Q.get_all_records()
        waits = [r.waiting_time for r in recs]
        mean_waits = sum(waits)/len(waits)
        print(f"Simulation n°{i+1}: {round(mean_waits, 6)} sec")
        v.average_waits_dict[f"{time}"] = mean_waits
        v.average_waits.append(mean_waits)

"""
\ Code
"""

"""
TACHE1 Code pour calculer les valeurs
"""

if tache == "tache1":

    """
    C'est l'un ou l'autre, c'était histoire de tracer les 2 graphes, faire les 2 ça sert à rien
    """

    # while v.nbexecs <= 600:
    #      simu(v.simtime, v.nbexecs)
    #      v.nbexecs+=10

    v.simtime = 2
    while v.simtime <= 10:
         simu(v.simtime, v.nbexecs)
         v.simtime+=1

    graph = v.average_waits_dict.items()
    x, y = zip(*graph)

    plt.plot(x, y)
    plt.show()

"""
Indiquer les manipulations que vous utilisez pour récupérer les résultats du temps moyenne de
séjour.
--------->
"""

    # simu(v.simtime, 1000)
    # mean_waiting_time = sum(v.average_waits)/len(v.average_waits)
    # print(f"Temps moyen de séjour: {round(mean_waiting_time, 6)} sec")

"""
FIN PARTIE 1
"""

"""
DEBUT PARTIE 2
"""

if tache == "tache2":

    simu(v.simtime, 1000)

    mean_waiting_time = sum(v.average_waits)/len(v.average_waits)
    print(f"Temps moyen de séjour: {round(mean_waiting_time, 6)} sec")

    """
    TACHE2
    Nous avons choisi la méthode de réplication. Indiquer le nombre de réplications
    (répétitions) et la précision que vous décidez d’utiliser.
    --------->
    """

    confiance = mean_waiting_time*(v.prct/100)
    gauche = round(mean_waiting_time - confiance, 6)
    droite = round(mean_waiting_time + confiance, 6)
    I = [gauche, droite]

    v.average_waits = []
    v.nbexecs = 5

    while True:
        simu(v.simtime, v.nbexecs)
        mean_waiting_time = sum(v.average_waits)/len(v.average_waits)
        print(f"Moyenne: {mean_waiting_time}")
        if I[0] < mean_waiting_time < I[1]: break
        v.nbexecs+=5

    print(f"A partir d'un nombre de {v.nbexecs} exécutions, ce n'est techniquement plus utile d'augmenter le nombre de répétitions, pour un intervalle de confiance de {v.prct}, car la une moyenne de séjour de {round(mean_waiting_time, 6)} sec et I = [{gauche} ; {droite}] coincident")
