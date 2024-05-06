def get_list(tr , tc , map):
    if map == 'heat' and tc > tr:
        return tc
    elif map == 'freeze' and tc < tr :
        return tc
    elif map == 'auto':
        return tc
    return tr

tr , tc = map(int, input().split())

map = input()

print(get_list(tr, tc , map))