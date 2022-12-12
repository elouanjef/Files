import ciw
import matplotlib.pyplot as plt
from networking import NetworkValues
from values import Values

"""
--------------------------Tache2--------------------------------
Pour cette tâche, il faut établir un intervalle de confiance, si on prend par exemple 5%, on doit vérifier à partir de quel nombre de répitions de simulations, le temps moyen de séjour se situe dans cet intervalle.
Pour ceci, on fait une 1000 simulations, d'un temps quelconque, ces 1000 simulations corresponderont à la valeur réelle.
A partir de ces 1000 simulations, on établit un intervalle de confiance:
I = [tps_moyen_sjr_reel - 5%; tps_moyen_sjr_reel + 5%]

On vérifie ensuite à partir de quel nombre de simulations, on a tps_moyen_sjr_theoX appartient à I (à partir de quel indice)
"""

"""
DEBUT PARTIE 2
"""

v = Values()
n = NetworkValues()
n.set_A(15)
n.reset_network()
tache = "tache1"

"""
Code /
"""

recs = []

def simu(time, nb, tache):
    v.sojourn_time = 0
    for i in range(nb):
        ciw.seed(i)
        Q = ciw.Simulation(n.N)
        Q.simulate_until_max_time(time)

        recs = Q.get_all_records()
        for r in recs:
            v.sojourn_time += abs(r.exit_date - r.arrival_date)

        print(f"Simulation n°{i+1}")

    if tache == "tache1":
        print(f"\nValeur absolue du temps de séjour, avec A = {n.A}: {round(v.sojourn_time, 3)}")
        print("\nCe temps est mesuré en unités discrètes, c'est-à-dire que chaque unité de temps représente une seule action dans le système.\n")

    elif tache == "tache2":
        v.tabS.append(v.sojourn_time)

"""
\ Code
"""

"""
TACHE1 Estimation du temps de séjour avec A = 15
"""

if tache == "tache1":
    n.set_A(15) # On set la valeur du A au cas où
    n.reset_network() # On recrée un réseau avec cette valeur
    simu(v.simtime, v.nbexecs, tache) # On fait nbexecs simulations avec A = 15

"""
TACHE2
"""

"""
Donner l’estimation ponctuelle et l’intervalles de con ance pour la mesure de
performance.
---------> Ca marche pas zebi, a finir, faut peut-être le faire manuellement, pas en python quoi
"""

    # values = type(recs)
    # print(recs)
    # mean_performance = mean(values)
    # stdev_performance = stdev(values)
    # print(f"\nEstimation ponctuelle: {mean_performance}")
    # confidence_interval = (mean_performance - (2-(prct/100))*stdev_performance/sqrt(len(values)), mean_performance + (2-(prct/100))*stdev_performance/sqrt(len(values)))
    # print(f"\nIntervalle de confiance pour la mesure de performance: {confidence_interval}")
"""
Représenter graphiquement l’évolution du temps de séjour en fonction de la valeur du taux
d’arrivée A.
---------> réponse en dessous
"""
if tache == "tache2":
    for a in range(15, 51):
        print(f"A={a}")
        simu(v.simtime, v.nbexecs, tache)
        n.set_A(a)
        n.reset_network()
        v.tabA.append(a)
    plt.plot(v.tabA, v.tabS) # Graphe avec x = tabA et y = tabSojourn
    plt.show()


"""
Ici pour chaque mesure on trace trois courbes : l’estimation ponctuelle et l’intervalles de
con ance (bornes supérieure et inférieure).
---------> Du coup la première question n'est pas terminée, on peut pas encore faire
"""
