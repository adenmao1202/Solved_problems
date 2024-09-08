
def rmDUP(lis):
    if not lis:
        return lis
    
    k = 1  
    # Pointer to place the next unique element
    for i in range(1, len(lis)):
        if lis[i] != lis[i - 1]:
            lis[k] = lis[i]
            k += 1
    
    return k, lis
    
    
def main():
    input_list = list(map(int, input().split()))
    print(rmDUP(input_list))  

if __name__ == "__main__":
    main()







lis = [0,0,1,1,1,2,2,3,3,4]
k = []
for i in lis:
    if i not in k:
        k.append(i)
print(k)
uni_num_len, total_len = len(k), len(lis)
under_len = total_len - uni_num_len

for i in range(under_len):
    k.append('_')
print(k)