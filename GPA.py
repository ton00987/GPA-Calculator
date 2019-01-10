import csv

command = input('Insert: 1 Edit: 2\n')

def insert_grade():
  new_semester = input('Enter Semester: ')
  new_subject = input('Enter subject: ')
  new_credit = input('Enter credit: ')
  new_grade = input('Enter grade: ')
  new_row = [new_semester, new_subject, new_credit, new_grade]

  with open('Calculate GPA.csv', 'r') as f:
    reader = csv.reader(f)
    reader = list(reader)
    reader.pop(0)
    reader.append(new_row)
    reader.sort()
  f.close()

  header = ['Semester', 'Subject', 'Credits', 'Grade']
  with open('Calculate GPA.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(reader)
  f.close()

def edit_grade():
  change_subject = input('Enter subject code: ')
  edit_semester = input('Enter semester: ')
  edit_subject = input('Enter subject: ')
  edit_credit = input('Enter credit: ')
  edit_grade = input('Enter grade: ')
  edit_row = [edit_semester, edit_subject, edit_credit, edit_grade]

  with open('Calculate GPA.csv', 'r') as f:
    reader = csv.reader(f)
    reader = list(reader)
    reader.pop(0)
    for i in range(len(reader)):
      if reader[i][1][:9] == change_subject:
        reader[i] = edit_row

    reader.sort()
  f.close()

  header = ['Semester', 'Subject', 'Credits', 'Grade']
  with open('Calculate GPA.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(reader)
  f.close()

if command == '1':
  insert_grade()
elif command == '2':
  edit_grade()