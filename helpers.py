def display_tierlist(tierlist:dict):
    ranks = sorted(tierlist.keys(), lambda x : tierlist.get(x, None))
    for rank in ranks:
        print(f"{rank}: {tierlist.get(rank)}")
    return None