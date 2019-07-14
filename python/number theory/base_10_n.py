def Base_10_to_n(X, n):
    """
    Xをn進数に変換し、文字列で返す
    """
    X_dumy = X
    out = ''
    while X_dumy > 0:
        out = str(X_dumy % n)+out
        X_dumy = int(X_dumy/n)
    return out
