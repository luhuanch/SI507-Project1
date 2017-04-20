import csv

with open('gradebook.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    dic = {}
    dic_2 = {}
    weight_lst = []
    point_lst = []
    for row in reader:
        if  row["Student"] != "weight" and row["Student"] != "max_points":
            dic_1 = {}
            dic_1["Assn 1"] = row['Assn 1']
            dic_1["Assn 2"] = row['Assn 2']
            dic_1["Assn 3"] = row['Assn 3']
            dic_1["Final Exam"] = row['Final Exam']
            dic[row['Student']] = dic_1



        if row["Student"] == "weight":
            weight_lst.append(row['Assn 1'])
            weight_lst.append(row['Assn 2'])
            weight_lst.append(row['Assn 3'])
            weight_lst.append(row['Final Exam'])
        if row["Student"] == "max_points":
            point_lst.append(row['Assn 1'])
            point_lst.append(row['Assn 2'])
            point_lst.append(row['Assn 3'])
            point_lst.append(row['Final Exam'])
    print(dic)
    print ("----------------------------------------")
    dic_1 = {}
    dic_1['Weight'] = weight_lst[0]
    dic_1['max_points'] = point_lst[0]
    dic_2["Assn 1"] =  dic_1
    dic_1 = {}
    dic_1['Weight'] = weight_lst[1]
    dic_1['max_points'] = point_lst[1]
    dic_2["Assn 2"] =  dic_1
    dic_1 = {}
    dic_1['Weight'] = weight_lst[2]
    dic_1['max_points'] = point_lst[2]
    dic_2["Assn 3"] =  dic_1
    dic_1 = {}
    dic_1['Weight'] = weight_lst[3]
    dic_1['max_points'] = point_lst[3]
    dic_2["Final Exam"] =  dic_1
    print (dic_2)
print ("----------------------------------------")
def student_average(student_name):
    grade_1  = float(dic[student_name]["Assn 1"])*float(dic_2['Assn 1']['Weight'])/float(dic_2['Assn 1']['max_points'])
    grade_2  = float(dic[student_name]["Assn 2"])*float(dic_2['Assn 2']['Weight'])/float(dic_2['Assn 2']['max_points'])
    grade_3  = float(dic[student_name]["Assn 3"])*float(dic_2['Assn 3']['Weight'])/float(dic_2['Assn 3']['max_points'])
    grade_4  = float(dic[student_name]["Final Exam"])*float(dic_2['Final Exam']['Weight'])/float(dic_2['Final Exam']['max_points'])
    print (student_name + " : " + str(((grade_1 + grade_2 + grade_3 + grade_4))*100))

def assn_average(assn_name):
    with open('gradebook.csv') as csvfile:
        reader= csv.reader(csvfile)
        n = 0
        for row in reader:
            try:
                type(int(row[1])) == type(100)
                if row[0] != "weight" and row[0] != "max_points":
                    if assn_name == "Assn 1":
                        n += int(row[1])
                    elif assn_name == "Assn 2":
                        n += int(row[2])
                    elif assn_name == "Assn 3":
                        n += int(row[3])
                    elif assn_name == "Final Exam":
                        n += int(row[4])
                else:
                    break
            except:
                continue
        print (assn_name + ":" + str(100*n/float(dic_2[assn_name]['max_points'])/6))

student_average('Julie')
student_average('Humphrey')
student_average('James')
student_average('Clark')
student_average("Audrey")
student_average('Marilyn')
print ("----------------------------------------")
assn_average("Assn 1")
assn_average('Assn 2')
assn_average('Assn 3')
assn_average('Final Exam')
print ("----------------------------------------")
