#!usr/local/bin


def main():
    map_1 = {'a': 1, 'f': 2, 'b': 3, 'g': 90, 'c': [12, 34], 'z': 45}
    map_2 = {'f': 12, 'c': 3, 'a': [2, 4], 'b': 11, 'y': [8, 23]}

    counter = 0
    map_1_keys = map_1.keys()
    map_2_keys = map_2.keys()

    result = {}
    if len(map_1_keys) > len(map_2_keys):
        for key in map_1_keys:
            if key in map_2:
                print(key)
                result[key] = [map_1.get(key), map_2.get(key)]
                if isinstance(map_2.get(key), list):
                    print("This key has a list value")

    print(result)
    # while counter < len(map_1):
    #     counter += 1


if __name__ == "__main__":
    main()
