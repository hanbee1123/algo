def sort(lst):
    if not lst:
        return []
    return (sort([x for x in lst[1:] if x <  lst[0]])
            + [lst[0]] +
            sort([x for x in lst[1:] if x >= lst[0]]))


if __name__ == "__main__":
    sort("cba")