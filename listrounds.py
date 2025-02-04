def find_rounds(numbers):
    newlist = []
    ll = numbers
    nn = 1
    while len(ll) > 0:
        subll = []
        for i in range(len(ll)):
            if ll[i] == nn:
                subll.append(nn)
                nn += 1
        ll = [x for x in ll if x not in subll]
        newlist.append(subll)
    return newlist


if __name__ == "__main__":
    print(find_rounds([1, 2, 3, 4]))
    # [[1, 2, 3, 4]]

    print(find_rounds([1, 3, 2, 4]))
    # [[1, 2], [3, 4]]    

    print(find_rounds([4, 3, 2, 1]))
    # [[1], [2], [3], [4]]
    
    print(find_rounds([1]))
    # [[1]]

    print(find_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
    # [[1], [2, 3], [4, 5, 6], [7, 8]]