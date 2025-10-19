n = int(input("Enter Number of Processes: "))
process = []

# Getting AT & BT
for i in range(n):
    AT = int(input(f"Enter Arrival time for P{i+1}: "))
    BT = int(input(f"Enter Burst time for P{i+1}: "))
    process.append({"PID": f"P{i+1}", "AT": AT, "BT": BT, "RT": BT})


def FCFS(process):
    process.sort(key=lambda x: x["AT"])
    time = 0
    completed = []
    timeline = []

    for p in process:
        if time < p["AT"]:
            while time < p["AT"]:
                timeline.append("IDLE")
                print("CPU IDLEING.......")
                time += 1

        for _ in range(p["BT"]):
            timeline.append(p["PID"])
            print("Processing...")
            time += 1

        p["CT"] = time
        p["TAT"] = p["CT"] - p["AT"]
        p["WT"] = p["TAT"] - p["BT"]
        completed.append(p)

    print("\n=== FCFS Scheduling ===")
    print("Timeline:")
    print("Time :", " ".join([str(i).rjust(2) for i in range(len(timeline))]))
    print("CPU  :", " ".join(timeline))

    print("\nResults:")
    print(f"{'PID':<5}{'AT':<5}{'BT':<5}{'CT':<5}{'TAT':<5}{'WT':<5}")
    for p in completed:
        print(f"{p['PID']:<5}{p['AT']:<5}{p['BT']:<5}{p['CT']:<5}{p['TAT']:<5}{p['WT']:<5}")


def SJF(process):
    process.sort(key=lambda x: (x["AT"], x["BT"]))
    time = 0
    completed = []
    ready_queue = []
    timeline = []
    processes = process.copy()

    while len(completed) < len(process):
        for p in processes:
            if p["AT"] <= time and p not in ready_queue and p not in completed:
                ready_queue.append(p)

        if ready_queue:
            ready_queue.sort(key=lambda x: x["BT"])
            current = ready_queue.pop(0)

            if time < current["AT"]:
                while time < current["AT"]:
                    timeline.append("IDLE")
                    print("CPU IDLEING.......")
                    time += 1

            for _ in range(current["BT"]):
                timeline.append(current["PID"])
                print("Processing...")
                time += 1

            current["CT"] = time
            current["TAT"] = current["CT"] - current["AT"]
            current["WT"] = current["TAT"] - current["BT"]
            completed.append(current)
        else:
            timeline.append("IDLE")
            print("CPU IDLEING.......")
            time += 1

    print("\n=== SJF Scheduling (Non-preemptive) ===")
    print("Timeline:")
    print("Time :", " ".join([str(i).rjust(2) for i in range(len(timeline))]))
    print("CPU  :", " ".join(timeline))

    print("\nResults:")
    print(f"{'PID':<5}{'AT':<5}{'BT':<5}{'CT':<5}{'TAT':<5}{'WT':<5}")
    for p in completed:
        print(f"{p['PID']:<5}{p['AT']:<5}{p['BT']:<5}{p['CT']:<5}{p['TAT']:<5}{p['WT']:<5}")


def RR(process):
    from collections import deque
    queue = deque()
    time = 0
    timeline = []
    completed = []
    processes = sorted(process, key=lambda x: x["AT"])
    arrived = []
    idx = 0

    # Calculate average BT for auto quantum
    avg_bt = sum(p["BT"] for p in process) // len(process)
    quantum = max(2, min(10, avg_bt))
    print(f"\nAuto-selected Time Quantum: {quantum}")

    while len(completed) < len(process):
        while idx < len(processes) and processes[idx]["AT"] <= time:
            arrived.append(processes[idx])
            queue.append(processes[idx])
            idx += 1

        if queue:
            current = queue.popleft()

            if current["RT"] > quantum:
                for _ in range(quantum):
                    timeline.append(current["PID"])
                    print("Processing...")
                    time += 1
                    while idx < len(processes) and processes[idx]["AT"] <= time:
                        arrived.append(processes[idx])
                        queue.append(processes[idx])
                        idx += 1
                current["RT"] -= quantum
                queue.append(current)

            else:
                for _ in range(current["RT"]):
                    timeline.append(current["PID"])
                    print("Processing...")
                    time += 1
                    while idx < len(processes) and processes[idx]["AT"] <= time:
                        arrived.append(processes[idx])
                        queue.append(processes[idx])
                        idx += 1
                current["CT"] = time
                current["TAT"] = current["CT"] - current["AT"]
                current["WT"] = current["TAT"] - current["BT"]
                completed.append(current)
        else:
            timeline.append("IDLE")
            print("CPU IDLEING.......")
            time += 1

    print("\n=== Round Robin Scheduling ===")
    print("Timeline:")
    print("Time :", " ".join([str(i).rjust(2) for i in range(len(timeline))]))
    print("CPU  :", " ".join(timeline))

    print("\nResults:")
    print(f"{'PID':<5}{'AT':<5}{'BT':<5}{'CT':<5}{'TAT':<5}{'WT':<5}")
    for p in completed:
        print(f"{p['PID']:<5}{p['AT']:<5}{p['BT']:<5}{p['CT']:<5}{p['TAT']:<5}{p['WT']:<5}")


# Choosing scheduler type based on number of processes
if n <= 3:
    FCFS(process)
elif 4 <= n <= 7:
    SJF(process)
else:
    RR(process)

