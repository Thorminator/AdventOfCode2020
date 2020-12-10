def parse_input(file_name):
    with open(file_name) as f:
        return [int(line) for line in f.read().split("\n")]


def find_candidates(available_adapters, current_jolt):
    candidates = []
    for adapter in available_adapters:
        if 0 < adapter - current_jolt <= 3:
            candidates.append(adapter)
        elif adapter <= current_jolt:
            break
    return candidates


def find_arrangements(available_adapters):
    final_adapter = available_adapters[0]
    arrangement_counts = {str(final_adapter): 1}
    for adapter in available_adapters[1:]:
        candidates = find_candidates(available_adapters, adapter)
        arrangement_counts[str(adapter)] = sum(arrangement_counts[str(candidate)] for candidate in candidates)
    return sum(arrangement_counts[str(candidate)] for candidate in find_candidates(available_adapters, 0))


adapters = list(reversed(sorted(parse_input("input.txt"))))
print(find_arrangements(adapters))
