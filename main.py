from Poisson import gen_process, plot_processes, plot_num_vs_time

def main():
    intensity = 0.4
    time = 300

    processes = [gen_process(intensity, time) for _ in range(4)]
    plot_processes(processes)
    for process in processes:
        plot_num_vs_time(process)

if __name__ == "__main__":
    main()