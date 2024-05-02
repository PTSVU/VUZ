def main(input_list):

    Ω = set(input_list)

    X = {ω for ω in Ω if -80 < ω < 96}

    K = {ω // 8 for ω in Ω if ω > 25}

    A = {k * x for k in K for x in X if k < x}

    return len(X) * len(A) - sum(x * a for x in X for a in A)
