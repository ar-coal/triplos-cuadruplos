import sys

# x = sys.argv[1]
# x = input()
x = "(X*y+y/z)*(z+y)"
or_str = x
data = {}
global_flag = 0
print(or_str)

if "=" in or_str:
    global_flag = or_str[0]
    or_str = or_str[1:]
    or_str = or_str.replace(":=","")
    or_str = or_str.replace("=","")
or_str = or_str.strip()
for index in range(len(or_str)):
    data[index] = or_str[index]

agrupation = ['(', ')', '[', ']', '{', '}']
tokens = {
    "exponencial": {'^':'POW'},
    "mul": {'*': 'MUL', '/': 'DIV'},
    "add": {'+': 'ADD', '-': 'SUB','–':'SUB'}
}


def solve_t(sub_limit,top_limit):
    for key in tokens:
        current = tokens[key]
        for i,v in data.items():
            if sub_limit<i<top_limit:
                if v in current:
                    print(current[v]+" "+data[i-1]+" "+data[i+1])
                    valor = data[i+1]
                    data[i] = data[i-1]
                    for index,val in data.items():
                        if val == valor:
                            data[index] = data[i-1]
    #print(data)


def solve_c(sub_limit,top_limit, count):
    for key in tokens:
        current = tokens[key]
        for i,v in data.items():
            if sub_limit<i<top_limit:
                if v in current:
                    t_value = "t" + str(count)
                    print(current[v]+" "+t_value+" "+data[i-1]+" "+data[i+1])
                    count = count+1
                    valor = data[i+1]
                    valor2 = data[i-1]
                    data[i] = t_value
                    for index,val in data.items():
                        if val == valor:
                            data[index] = t_value
                        elif val == valor2:
                            data[index] = t_value
    #print(data)
    return count


def triplos():
    print("----------Triplos----------")
    count = 0
    for i,v in data.items():
        flag = 0
        if v in agrupation:
            flag = 1
        for key in tokens:
            current = tokens[key]
            if v in current:
                flag = 1
        if flag == 0:
            print("LOAD t"+str(count)+" "+v)
            data[i] = "t"+str(count)
            count += 1
    bandera = 0
    while bandera == 0:
        find = 0
        prev_v = ""
        prev_i = -1
        for i,v in data.items():
            if v in agrupation:
                current_i = agrupation.index(v)
                if prev_v == agrupation[current_i-1]:
                    solve_t(prev_i,i)
                    data[prev_i] = data[prev_i+1]
                    data[i] = data[prev_i+1]
                prev_v = v
                prev_i = i
                find = find+1
        if find == 0:
            bandera = 1
    solve_t(0,len(data))
    if global_flag != 0:
        print("STORE "+data[0]+" "+global_flag)


def cuadruplos():
    print("----------cuadruplos----------")
    count = 0
    for i,v in data.items():
        flag = 0
        if v in agrupation:
            flag = 1
        for key in tokens:
            current = tokens[key]
            if v in current:
                flag = 1
        if flag == 0:
            print("LOAD t"+str(count)+" "+v)
            data[i] = "t"+str(count)
            count += 1
    bandera = 0
    #print(data)
    while bandera == 0:
        find = 0
        prev_v = ""
        prev_i = -1
        for i,v in data.items():
            if v in agrupation:
                current_i = agrupation.index(v)
                if prev_v == agrupation[current_i-1]:
                    count = solve_c(prev_i,i,count)
                    data[prev_i] = data[prev_i+1]
                    data[i] = data[prev_i+1]
                prev_v = v
                prev_i = i
                find = find+1
        if find == 0:
            bandera = 1
    solve_c(0,len(data),count)
    if global_flag != 0:
        print("STORE "+data[0]+" "+global_flag)


def main():
    triplos()
    for index in range(len(or_str)):
        data[index] = or_str[index]
    cuadruplos()

if __name__ == "__main__":
    main()