def merge_the_tools(string, k):
    seg = []
    parts = int(len(string)/k)
    for i in range(parts):
        seg.append(string[i*k:(i+1)*k])
    for s in seg:
        chars = ""
        for c in s:
            if c not in chars:
                chars += c
        print(chars)