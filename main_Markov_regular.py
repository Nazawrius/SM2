from Markov_regular import path, plot_paths, experimental_matrix, experimental_consecutive_time, plot_stationary

def main_Markov():
    matrix = [
        [0.0, 0.5, 0.2, 0.1, 0.2],
        [0.4, 0.1, 0.2, 0.0, 0.3],
        [0.2, 0.2, 0.2, 0.2, 0.2],
        [0.0, 0.1, 0.2, 0.6, 0.1],
        [0.0, 0.2, 0.2, 0.4, 0.2]
    ]
    vector = [0.1, 0.5, 0.0, 0.2, 0.2]
    length = 150

    paths = [path(matrix, vector, length) for _ in range(300)]
    #plot_paths(paths[:4])
    exp_m = experimental_matrix(paths)
    for row in exp_m:
        print(' '.join(map(str, row)))
    
    print(experimental_consecutive_time(paths))

    paths = [path(matrix, vector, length) for _ in range(1000)]
    plot_stationary(paths)

if __name__ == "__main__":
    main_Markov()