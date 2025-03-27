def union(x, y):
    st = set()
    for a in x:
        st.add(a)
    for b in y:
        st.add(b)
    return st


print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True