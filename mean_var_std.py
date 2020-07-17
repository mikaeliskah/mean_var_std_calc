# solution uploaded to
# https://repl.it/@MikaMusic/NoxiousAdmiredBlogs#mean_var_std.py

import numpy as np

# list = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def calculate(list):
    '''this function will convert a list to a 3-by-3 matrix (fixed-size) and return
    statistics mean, var and std vor each column, line and the flattened matrix. '''

    # throw error when len(list) < 9
    l = len(list)
    if l < 9:
        raise ValueError("List must contain nine numbers.")

    M = create_matrix_from_list(list)

    # peralloc statistics lists
    mean_m = []
    mean_n = []
    mean = []
    var_m = []
    var_n = []
    std_m = []
    std_n = []
    max_m = []
    max_n = []
    min_m = []
    min_n = []
    sum_m = []
    sum_n = []

    # calculate statistics
    m = 3  # matrix size m-by-m
    for mm in range(m):
        mean_m.append(np.mean(M[:, mm]))
        var_m.append(np.var(M[:, mm]))
        std_m.append(np.std(M[:, mm]))
        max_m.append(np.max(M[:, mm]))
        min_m.append(np.min(M[:, mm]))
        sum_m.append(np.sum(M[:, mm]))

        mean_n.append(np.mean(M[mm]))
        var_n.append(np.var(M[mm]))
        std_n.append(np.std(M[mm]))
        max_n.append(np.max(M[mm]))
        min_n.append(np.min(M[mm]))
        sum_n.append(np.sum(M[mm]))

    mean_flat = np.mean(M)
    var_flat = np.var(M)
    std_flat = np.std(M)
    max_flat = np.max(M)
    min_flat = np.min(M)
    sum_flat = np.sum(M)

    means = [mean_m, mean_n, mean_flat]
    varis = [var_m, var_n, var_flat]
    stds = [std_m, std_n, std_flat]
    maxs = [max_m, max_n, max_flat]
    mins = [min_m, min_n, min_flat]
    sums = [sum_m, sum_n, sum_flat]

    # create dictionary
    calculations = {
        'mean': means,
        'variance': varis,
        'standard deviation': stds,
        'max': maxs,
        'min': mins,
        'sum': sums
    }
    return calculations


def create_matrix_from_list(list):
    M = np.zeros((3, 3))
    ii = 0
    for mm in range(3):
        for nn in range(3):
            M[mm][nn] = list[ii]
            ii += 1
    return M


# result = calculate(list)
#
# for i in result.items():
#     print(i)
