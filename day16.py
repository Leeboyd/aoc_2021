
with open("input/day16.txt") as f:
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

def _parse_packet_2(bin_str: str, idx: int, ver_sum: int):
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
        expr_values = []

        # length type ID
        l_id = bin_str[idx]
        idx += 1

        if l_id == "0":
            length_in_bits = int(bin_str[idx:idx + 15], 2)
            idx += 15

            end_point = idx + length_in_bits
            while idx < end_point:
                idx, ver_sum, expr_value = _parse_packet_2(bin_str, idx, ver_sum)
                expr_values.append(expr_value)
        else:
            length_in_subpackets = int(bin_str[idx:idx + 11], 2)
            idx += 11

            for _ in range(length_in_subpackets):
                idx, ver_sum, expr_value = _parse_packet_2(bin_str, idx, ver_sum)
                expr_values.append(expr_value)

        if tp == 0:
            return idx, ver_sum, sum(expr_values)
        elif tp == 1:
            res = 1
            for x in expr_values:
                res *= x
            return idx, ver_sum, res
        elif tp == 2:
            return idx, ver_sum, min(expr_values)
        elif tp == 3:
            return idx, ver_sum, max(expr_values)
        elif tp == 5:
            return idx, ver_sum, int(expr_values[0] > expr_values[1])
        elif tp == 6:
            return idx, ver_sum, int(expr_values[0] < expr_values[1])
        elif tp == 7:
            return idx, ver_sum, int(expr_values[0] == expr_values[1])

answer_1 = _parse_packet(lines, 0, 0)[1]
print(answer_1)
answer_2 = _parse_packet_2(lines, 0, 0)[2]
print(answer_2)