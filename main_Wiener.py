from Wiener import gen_process, plot_processes, plot_mean_var, plot_first_exit

def main_Wiener():
    delta = 0.1
    eps = 0.05
    M = 10000
    dt = 0.005

    processes = [gen_process(M, dt) for _ in range(4)]
    plot_processes(processes, dt)

    many_processes = [gen_process(M, dt) for _ in range(150)]
    plot_mean_var(many_processes)

    alpha = 0.4
    plot_first_exit(many_processes, alpha, dt)

if __name__ == "__main__":
    main_Wiener()