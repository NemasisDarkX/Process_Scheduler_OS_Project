n = int(input("Enter Number of Process:"))
process=[]

#getting AT && BT
for i in range(n):
    AT=int(input(f"Enter Arrival time for P{i+1}:"))
    BT=int(input(f"Enter Burst time for P{i+1}:"))
    process.append({"PID": f"P{i+1}","AT": AT, "BT": BT, "RT":BT})


def FCFS(process):
    process.sort(key= lambda x: x["AT"])
    time=0
    comepleted=[]
    timeline=[]

    for p in process:
        if time < p["AT"]:
            while time < p["AT"]:
                timeline.append("IDLE")
                print("CPU IDLEING.......")
                time+=1

        for _ in range(p["BT"]):
            timeline.append(p["PID"])
            print("Processing...")
            time+=1

        p["CT"] = time
        p["TAT"] = p["CT"] - p["AT"]
        p["WT"] = p["TAT"] - p["BT"]
        comepleted.append(p)

     # Print results
    print("\n=== FCFS Scheduling ===")
    print("Timeline:")
    print("Time :", " ".join([str(i).rjust(2) for i in range(len(timeline))]))
    print("CPU  :", " ".join(timeline))

    print("\nResults:")
    print(f"{'PID':<5}{'AT':<5}{'BT':<5}{'CT':<5}{'TAT':<5}{'WT':<5}")
    for p in comepleted:
        print(f"{p['PID']:<5}{p['AT']:<5}{p['BT']:<5}{p['CT']:<5}{p['TAT']:<5}{p['WT']:<5}")    


#choosing scheduler type based on number of process
if n<=3:
    FCFS(process)
elif 4 <= n <= 7:
    print("Running SJF")
else:
    print("Running RR")

