from Wiener import gen_process, plot_processes

def main_Wiener():
    delta = 0.1
    eps = 0.05
    M = 10000
    dt = 0.01

    processes = [gen_process(M, dt) for _ in range(4)]
    plot_processes(processes, dt)

    many_processes = [gen_process(M, dt) for _ in range(250)]

if __name__ == "__main__":
    main_Wiener()