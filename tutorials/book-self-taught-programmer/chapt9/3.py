import csv

l1 =[1, 2, 3, 4]
l2 =[10, 20, 30, 40]
l3 = [["a", "b", "c", "d", "e"], ["f", "g", "h"], ["i"]]
with open("table.csv", "w") as file_obj:
    cvs_obj = csv.writer(file_obj, delimiter = ",")
    cvs_obj.writerow(l1)
    cvs_obj.writerow(l2)
    for list in l3:
        cvs_obj.writerow(list)