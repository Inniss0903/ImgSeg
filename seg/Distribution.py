from experiment import show_distribution

twoD_se_path = "/Users/gem/IdeaProjects/deDoc/2D"
d = {}


def show_2d_distribution():
    try:
        two_dim_result = open(twoD_se_path)
    except Exception as e:
        print(e)

    for line in two_dim_result.readlines():
        comm = line.rstrip().split('\t')
        key = len(comm)
        d[key] = d.get(key, 0) + 1

    x = []
    y = []
    for e in sorted(d):
        x.append(e)
        y.append(d[e])
    show_distribution(x, y)
