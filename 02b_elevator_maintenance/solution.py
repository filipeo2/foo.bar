def solution(l):
    from collections import deque
    print('\n', l)

    numeric_list = []
    for elevator_version in l:
        version_parts = elevator_version.split('.')
        numeric_version_parts = [int(x) for x in version_parts]

        # print(splited_text)
        match numeric_version_parts:
            case [major, minor, rev]:
                print(numeric_version_parts, 'major, minor, rev')
                numeric_list.append([major, minor, rev])
            case [major, minor]:
                print(numeric_version_parts, 'major, minor')
                numeric_list.append([major, minor])
            case [major]:
                print(numeric_version_parts, 'major only')
                numeric_list.append([major])
            case _:
                print(numeric_version_parts, 'error')
    print(numeric_list)
    sorted_list = sorted(numeric_list)
    print(sorted_list)

    # # once sorted by major, do sort in minor field of each version inside each major
    # rotational_list = deque(sorted_list)
    # for current_major_version in range(len(rotational_list)):
    #     print('\ncurrent_major_version', current_major_version)

    #     temp_minor_list = [] # initilize a new list to treat current major version
    #     while rotational_list[0][0] == current_major_version:
    #         print(rotational_list[0][1])

    #         temp_minor_list.append(rotational_list.popleft())
    #     temp_minor_list.sort() 

    # ordered_result = sorted(l)
    # print(sorted(l))

    # concatenate every major.minor.version (dots) and every all elevator version (comma)
    result = ','.join(['.'.join([str(i) for i in item]) for item in sorted_list])
    print(result)
    return result

 #     print(version_tuple)
    #     for major, minor, rev in version:
    #         print(major, minor, rev)

# print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
assert solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]) == '0.1,1.1.1,1.2,1.2.1,1.11,2,2.0,2.0.0'
assert solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]) == '1.0,1.0.2,1.0.12,1.1.2,1.3.3'