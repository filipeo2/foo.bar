def solution(l):
    print('\n', l)

    # convert the entire l content in numeric values to sort later
    numeric_list = []
    for elevator_version in l:
        version_parts = elevator_version.split('.')
        numeric_version_parts = [int(x) for x in version_parts]
        numeric_list.append(numeric_version_parts)
    print(numeric_list)

    # sort the entire numeric list
    sorted_list = sorted(numeric_list)
    print(sorted_list)

    # concatenate every major.minor.version (dots) and create the final list
    final_list = ['.'.join([str(i) for i in item]) for item in sorted_list]
    print(final_list)
    return final_list

# solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])
assert solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]) == ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]
assert solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]) == ['0.1','1.1.1','1.2','1.2.1','1.11','2','2.0','2.0.0']