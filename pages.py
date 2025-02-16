def create_string(pages):
    uniq_pages = sorted(set(pages))

    if not uniq_pages:
        return ""

    rval = []
    alku = uniq_pages[0]
    vika = alku

    for i in range(1, len(uniq_pages)):
        taa = uniq_pages[i]

        if taa == vika + 1:
            vika = taa
        else:
            if alku == vika:
                rval.append(str(alku))
            else:
                rval.append(f"{alku}-{vika}")

            alku = taa
            vika = taa

    if alku == vika:
        rval.append(str(alku))
    else:
        rval.append(f"{alku}-{vika}")

    return ",".join(rval)


if __name__ == "__main__":
    print(create_string([1])) # 1
    print(create_string([1, 2, 3])) # 1-3
    print(create_string([1, 1, 1])) # 1
    print(create_string([1, 2, 1, 2])) # 1-2
    print(create_string([1, 6, 2, 5])) # 1-2,5-6
    print(create_string([1, 3, 5, 7])) # 1,3,5,7
    print(create_string([1, 8, 2, 7, 3, 6, 4, 5])) # 1-8
    print(create_string([3, 2, 9, 4, 3, 6, 9, 8])) # 2-4,6,8-9

    pages = [3, 2, 1, 3, 2, 1]
    print(create_string(pages)) # 1-3
    print(pages) # [3, 2, 1, 3, 2, 1]