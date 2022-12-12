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

    if tache == "tache1":
        v.tabS.append(v.sojourn_time)

"""
\ Code
"""

"""
TACHE1
"""

if tache == "tache1":

    figure, axis = plt.subplots(2,2)
    minA = 15
    maxA = 51

    n.set_R(n.R*2)
    n.reset_network()
    for a in range(minA, maxA):
        print(f"A={a}")
        simu(v.simtime, v.nbexecs, tache)
        n.set_A(a)
        n.reset_network()
        v.tabA.append(a)

    # First simulation
    axis[0, 0].plot(v.tabA, v.tabS)
    axis[0, 0].set_title("Double R")

    n.reset_R()
    n.set_A(15)
    n.set_S(n.S*2)
    n.reset_network()
    for a in range(minA, maxA):
        print(f"A={a}")
        simu(v.simtime, v.nbexecs, tache)
        n.set_A(a)
        n.reset_network()
        v.tabA.append(a)

    # Second simulation
    axis[0, 1].plot(v.tabA, v.tabS)
    axis[0, 1].set_title("Double S")

    n.reset_S()
    n.set_A(15)
    n.set_SR(n.SR*2)
    n.reset_network()
    for a in range(minA, maxA):
        print(f"A={a}")
        simu(v.simtime, v.nbexecs, tache)
        n.set_A(a)
        n.reset_network()
        v.tabA.append(a)

    # Third simulation
    axis[1, 0].plot(v.tabA, v.tabS)
    axis[1, 0].set_title("Double SR")
    plt.show()
