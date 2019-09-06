with open('verbsANSI.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')
result = ''
result = result + "<ul>" + "<system>" + "<ul>"
#print(data)
level1 = data.split("%")
level1= level1[1:]
for i in range(len(level1)):
    #print(level1[i])
    #print("\n")
    level2 = level1[i].split("*")
    print("<id>assembly</id><assembly>")
    print(level2[0])
    print("</assembly>")
    result = result + "<id>assembly</id><assembly>"+level2[0]+"</assembly>"+ "<ul>"
    level2 = level2[1:]
    for j in range(len(level2)):
        #print(level2[j])
        #print("\n")
        if '$' in level2[j]:
            level3 = level2[j].split("$")
            print("<id>component</id><component>")
            print(level3[0])
            print("</component>")
            result = result+ "<id>component</id><component>"+ level3[0]+ "</component>"+ "<ul>"
            level3 = level3[1:]
            for k in range(len(level3)):
                level4 = level3[k].split("-")
                print("<id>attribute</id><attribute>")
                print(level4[0])
                print("</attribute>")
                #print(level4[1])
                verbs = level4[1].split(",")
                print("<id>verbs</id>")
                result = result + "<id>attribute</id><attribute>" + level4[0] + "</attribute>"+ "<ul>"+"<id>verbs</id>"
                for l in range(len(verbs)):
                    print("<verb>")
                    print(verbs[l])
                    print("</verb>")
                    result = result + "<verb>" + verbs[l]+ "</verb>"
                result = result + "</ul>"
            result = result + "</ul>"

        else:
            level4 = level2[j].split("-")
            print("<id>attribute</id><attribute>")
            print(level4[0])
            print("</attribute>")
            #print(level4[1])
            verbs = level4[1].split(",")
            print("<id>verbs</id>")
            result = result + "<id>attribute</id><attribute>" + level4[0] + "</attribute>" + "<ul>"+"<id>verbs</id>"
            for l in range(len(verbs)):
                print("<verb>")
                print(verbs[l])
                print("</verb>")
                result = result + "<verb>" + verbs[l] + "</verb>"
            result = result + "</ul>"
    result = result + "</ul>"
result = result + "</ul>" + "</system>" + "</ul>"
f = open('verbgraph.xml', 'w')
f.write(result)