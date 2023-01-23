import ciw
import matplotlib.pyplot as plt
from networking import NetworkValues
from values import Values

"""
DEBUT PARTIE 1
"""

v = Values()
n = NetworkValues()
n.set_A(15)
n.reset_network()
tache = "tache1"

"""
Code /
"""

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

    v.tabS.append(v.sojourn_time)
    print(v.tabS)

"""
\ Code
"""

"""
TACHE1
"""

minA = 15
maxA = 31

if tache == "tache1":

    figure, axis = plt.subplots(2,2)

    # Simulation système initial
    n.set_A(15)
    n.reset_network()
    for a in range(minA, maxA):
        print(f"A={a}")
        simu(v.arrivee, v.nbexecs, tache)
        n.set_A(a)
        n.reset_network()
        v.tabA.append(a)

    """
    En sortie ->
    """
    tabSim1 = v.tabS
    axis[0, 0].plot(v.tabA, v.tabS)
    axis[0, 0].set_title("Normal")

    # First simulation
    v.tabA = []
    v.tabS = []
    n.set_A(15)
    n.reset_SR()
    n.reset_S()
    n.set_R(n.R*2)
    n.reset_network()
    for a in range(minA, maxA):
        print(f"A={a}")
        simu(v.arrivee, v.nbexecs, tache)
        n.set_A(a)
        n.reset_network()
        v.tabA.append(a)

    """
    En sortie ->
    """
    tabSim2 = v.tabS
    axis[0, 1].plot(v.tabA, v.tabS)
    axis[0, 1].set_title("Double R")

    # Second simulation
    v.tabA = []
    v.tabS = []
    n.reset_R()
    n.reset_SR()
    n.set_A(15)
    n.set_S(n.S*2)
    n.reset_network()
    for a in range(minA, maxA):
        print(f"A={a}")
        simu(v.arrivee, v.nbexecs, tache)
        n.set_A(a)
        n.reset_network()
        v.tabA.append(a)

    """
    En sortie ->
    """
    tabSim3 = v.tabS
    axis[1, 0].plot(v.tabA, v.tabS)
    axis[1, 0].set_title("Double S")

    # Third simulation
    v.tabA = []
    v.tabS = []
    n.reset_S()
    n.reset_R()
    n.set_A(15)
    n.set_SR(n.SR*2)
    n.reset_network()
    for a in range(minA, maxA):
        print(f"A={a}")
        simu(v.arrivee, v.nbexecs, tache)
        n.set_A(a)
        n.reset_network()
        v.tabA.append(a)

    """
    En sortie ->
    """
    tabSim4 = v.tabS
    axis[1, 1].plot(v.tabA, v.tabS)
    axis[1, 1].set_title("Double SR")

    print(f"\n{tabSim1}\n{tabSim2}\n{tabSim3}\n{tabSim4}")
    plt.show()

if tache == "tache2":

    # Simulation système initial
    n.set_A(15)
    n.reset_network()
    for a in range(minA, maxA):
        print(f"A={a}")
        simu(v.arrivee, v.nbexecs, tache)
        n.set_A(a)
        n.reset_network()
        v.tabA.append(a)

    """
    En sortie ->
    """
    tabSim1 = v.tabS

    # First simulation
    v.tabA = []
    v.tabS = []
    n.set_A(15)
    n.set_R(n.R*2)
    n.reset_network()
    for a in range(minA, maxA):
        print(f"A={a}")
        simu(v.arrivee, v.nbexecs, tache)
        n.set_A(a)
        n.reset_network()
        v.tabA.append(a)

    tabSim2 = v.tabS

    tabSim = []
    for i in range(len(v.tabA)):
        calc = abs(tabSim2[i] - tabSim1[i])
        tabSim.append(calc)

    plt.plot(v.tabA, tabSim)
    plt.show()

if tache == "tache3":

    v.tabA = []
    v.tabS = []
    n.set_A(15)
    n.reset_SR()
    n.reset_S()
    n.set_R(n.R*2)
    n.reset_network()
    for a in range(minA, maxA):
        print(f"A={a}")
        simu(v.arrivee, v.nbexecs, tache)
        n.set_A(a)
        n.reset_network()
        v.tabA.append(a)

    tabSim2 = v.tabS

    v.tabA = []
    v.tabS = []
    n.set_A(15)
    n.reset_R()
    n.reset_SR()
    n.set_S(n.S*2)
    n.reset_network()
    for a in range(minA, maxA):
        print(f"A={a}")
        simu(v.arrivee, v.nbexecs, tache)
        n.set_A(a)
        n.reset_network()
        v.tabA.append(a)

    tabSim3 = v.tabS

    v.tabA = []
    v.tabS = []
    n.set_A(15)
    n.reset_R()
    n.reset_S()
    n.set_SR(n.SR*2)
    n.reset_network()
    for a in range(minA, maxA):
        print(f"A={a}")
        simu(v.arrivee, v.nbexecs, tache)
        n.set_A(a)
        n.reset_network()
        v.tabA.append(a)

    tabSim4 = v.tabS

    figure, axis = plt.subplots(2,2)

    tabSimRes1 = []
    for i in range(len(v.tabA)):
        calc = abs(tabSim2[i] - tabSim3[i])
        tabSimRes1.append(calc)

    axis[0, 0].plot(v.tabA, tabSimRes1)
    axis[0, 0].set_title("Double R et Double S")

    tabSimRes2 = []
    for i in range(len(v.tabA)):
        calc = abs(tabSim2[i] - tabSim4[i])
        tabSimRes2.append(calc)

    axis[0, 1].plot(v.tabA, tabSimRes2)
    axis[0, 1].set_title("Double R et Double SR")

    tabSimRes3 = []
    for i in range(len(v.tabA)):
        calc = abs(tabSim3[i] - tabSim4[i])
        tabSimRes3.append(calc)

    axis[1, 0].plot(v.tabA, tabSimRes3)
    axis[1, 0].set_title("Double S et Double SR")

    plt.show()
