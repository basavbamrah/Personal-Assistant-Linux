def extract(path='./Contacts (1).vcf'):
    d = {}
    n = ""
    pn = ""
        
    with open(path, 'r') as contact:
        whitelist = ['FN', 'TEL', 'CELL']
        for line in contact:
            blacklist = ['BEGIN', 'VERSION', 'END', 'CHARSET']
            if [ele for ele in blacklist if ele in line]:
                continue
            elif 'FN' in line:

                n = line
                n = n.replace('FN:', "")
                # n = list(n)
                n = [i if (i.isalpha() or i.isspace()) else "" for i in n]
                # print(n)

                n = "".join(n).strip()
                # print(n)

                if n.replace(" ", "").isalpha():
                    # print('yes')
                    if n not in d:
                        d[n] = []

            elif 'CELL' in line or 'TEL' in line or 'PREF' in line:
                pn = line

                pn = pn.split(':')[1]
                pn = pn.split(';')
                if len(pn)>1:pn=pn[1]
                pn=''.join(pn).strip()

                if pn[0] != '+' and len(pn) == 10:
                    pn = "+91"+pn
                if n:
                    if len(d[n])<2:
                         d[n].append(pn)
                    # with open('./temp.txt', 'a')as temp:
                    #     temp.write(f'{n} : {pn}\n')
            else:
                continue
        for i in list(d.keys()):
            d[i]=list(set(d[i]))
        # print(d)
        return d
extract()