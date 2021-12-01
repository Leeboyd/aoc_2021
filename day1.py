# Dec 1 - 1 - my answer
# read input
with open('./input/input1.txt', 'r') as fr:
    Lines = fr.readlines()
    # Strips the newline character
    input = list(map(lambda x: int(x.rstrip().replace("\n", "")), Lines))
    print(f"TOTAL {len(input)} Lines")

def find_surge(input):
    last = None
    result = 0

    if len(input):
        while len(input):
            if last is None:
                last = input.pop(0)
                continue
            
            current = input.pop(0)

            if current > last:
                result += 1
            
            last = current
    return result

answer1 = find_surge(input)

result_temp = []
for i in range(1, len(input) - 1):
    result_temp.append( sum([input[i-1],input[i],input[i+1]]) )

answer2 = find_surge(result_temp)