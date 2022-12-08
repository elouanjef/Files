import ciw
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

average_waits = []
simtime = 180

for s in range(1000):
    ciw.seed(s)
    Q = ciw.Simulation(N)
    Q.simulate_until_max_time(simtime)
    recs = Q.get_all_records()
    waits = [r.waiting_time for r in recs]
    average_waits.append(sum(waits)/len(waits))

mean_waiting_time = sum(average_waits)/len(average_waits)
print("Temps moyen d'attente: ", mean_waiting_time)
