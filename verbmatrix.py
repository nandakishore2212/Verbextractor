import xlsxwriter
with open('verbsANSI2.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')
verbmat = [[0] * 200 for _ in range(5000)]
m=1
n=1
#print(data)
level1 = data.split("%")
level1= level1[1:]
for i in range(len(level1)):
    if '*' in level1[i]:
        level2 = level1[i].split("*")

        #print(level2[0])

        level2 = level2[1:]
        for j in range(len(level2)):

            if '$' in level2[j]:
                level3 = level2[j].split("$")

                #print(level3[0])

                level3 = level3[1:]
                for k in range(len(level3)):
                    level4 = level3[k].split("-")

                    parent = level4[0]
                    verbmat[0][n] = parent
                    n = n + 1

                    verbs = level4[1].split(",")


                    for l in range(len(verbs)):
                        v = verbs[l]
                        flag=0
                        for p in range(m):
                            if (v == verbmat[p][0]):
                                verbmat[p][n-1]=1
                                flag=1
                        if(flag==0):
                            verbmat[m][0]=v
                            verbmat[m][n-1]=1
                            m = m+1


                    #result = result + "</ul>"
                #result = result + "</ul>"

            else:
                level4 = level2[j].split("-")

                parent = level4[0]
                verbmat[0][n] = parent
                n = n + 1
                verbs = level4[1].split(",")

                for l in range(len(verbs)):
                    v = verbs[l]
                    flag = 0
                    for p in range(m):
                        if (v == verbmat[p][0]):
                            verbmat[p][n-1] = 1
                            flag = 1
                    if (flag == 0):
                        verbmat[m][0] = v
                        verbmat[m][n-1] = 1
                        m = m + 1
                    #result = result + "<verb>" + verbs[l] + "</verb>"
                #result = result + "</ul>"
        #result = result + "</ul>"
    else:
        level4 = level1[i].split("-")

        parent= level4[0]
        verbmat[0][n] =parent
        n=n+1
        verbs = level4[1].split(",")

        for l in range(len(verbs)):
            v = verbs[l]
            flag = 0
            for p in range(m):
                if (v == verbmat[p][0]):
                    verbmat[p][n-1] = 1
                    flag = 1
            if (flag == 0):
                verbmat[m][0] = v
                verbmat[m][n-1] = 1
                m = m + 1

#print(verbmat)
#print("\n\n")

workbook = xlsxwriter.Workbook('verbarray.xlsx')
worksheet = workbook.add_worksheet()

row = 0

for col, data in enumerate(verbmat):
    worksheet.write_column(row, col, data)

workbook.close()
#result = result + "</ul>" + "</system>" + "</ul>"
