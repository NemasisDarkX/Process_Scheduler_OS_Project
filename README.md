# Dynamic CPU Scheduling Simulator

##  Overview
This project is a simple **CPU Process Scheduling Simulator** written in Python.  
It allows you to simulate how an operating system schedules processes using various algorithms — starting with **FCFS (First Come First Serve)**, with plans to extend to **SJF (Shortest Job First)** and **RR (Round Robin)**.  

The simulator dynamically selects which scheduling algorithm to use based on the number of processes entered by the user.

---

##  Features
- Accepts user input for:
  - **Number of processes (n)**
  - **Arrival Time (AT)** and **Burst Time (BT)** for each process
- Automatically initializes:
  - **Remaining Time (RT)** = **BT**
- Dynamically chooses scheduling strategy:
  - **FCFS** for ≤ 3 processes  
  - **SJF** for 4–7 processes  
  - **RR** for > 7 processes  
- Displays:
  - CPU **timeline** (execution order)
  - Process details table (AT, BT, CT, TAT, WT)
- Handles **CPU idle time** when no process is ready
- Automatically calculates quantum time by taking avarage BT
	`$avg_bt = sum(p["BT"] for p in process) // len(process)
    	 $quantum = max(2, min(10, avg_bt))` 


