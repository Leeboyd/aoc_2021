
with open("input/input.txt") as f:
    lines = "".join([bin(int(x, 16))[2:].zfill(4) for x in f.read().strip()])

def _parse_packet(bin_str: str, idx: int, ver_sum: int):
    ver_sum += int(bin_str[idx:idx + 3], 2)
    tp = int(bin_str[idx + 3:idx + 6], 2)
    idx += 6
    if tp == 4:
        not_last = True
        bin_value = ""
        while not_last:
            bin_value += bin_str[idx + 1:idx + 5]
            if bin_str[idx] == "0":
                not_last = False
            idx += 5
        return idx, ver_sum, int(bin_value, 2)
    else:
        # expr_values = []

        # length type ID
        l_id = bin_str[idx]
        idx += 1

        if l_id == "0":
            length_in_bits = int(bin_str[idx:idx + 15], 2)
            idx += 15

            end_point = idx + length_in_bits
            while idx < end_point:
                idx, ver_sum, expr_value = _parse_packet(bin_str, idx, ver_sum)
                # expr_values.append(expr_value)
        else:
            length_in_subpackets = int(bin_str[idx:idx + 11], 2)
            idx += 11

            for _ in range(length_in_subpackets):
                idx, ver_sum, expr_value = _parse_packet(bin_str, idx, ver_sum)
                # expr_values.append(expr_value)
        return idx, ver_sum, None

answer_1 = _parse_packet(lines, 0, 0)[1]
print(answer_1)