def get_list(path):
    fp = open(path)
    lst = fp.readlines()
    fp.close()
    return lst


if __name__ == "__main__":
    detect_label = r"H:\ABM\result\test.txt"
    origin_label = r"H:\ABM\data\val\labels\label.txt"

    detect_list = get_list(detect_label)
    origin_list = get_list(origin_label)

    # tot = len(detect_list)
    acc = tot = 0
    labeldct = {}
    for i in detect_list:
        lst = i.strip().split()
        labeldct[lst[0]] = lst[1:]

    for i in origin_list:
        lst = i.strip().split()
        ori = labeldct[lst[0] + ".jpg"]
        lst = lst[1:]
        for j in range(0, min(len(ori), len(lst))):
            tot += 1
            if ori[j] == lst[j]:
                acc += 1
        # labeldct[lst[0]] = [labeldct[lst[0]], lst[1:]]

    print(acc / tot)

