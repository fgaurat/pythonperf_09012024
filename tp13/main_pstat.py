import pstats

def main():
    stats = pstats.Stats("nth_prim.pstat")
    # print(stats.print_stats())
    stats.sort_stats(pstats.SortKey.TIME).print_stats(3)
    
if __name__ == '__main__':
    main()