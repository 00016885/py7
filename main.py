#
# student = {}
#
# print(student)
#
# student = {'name': 'Lola',
#            'age': 19,
#            'course': 'BIS'
#            }
#
# print(student)
#
# student1 = dict()
# student1['name'] = 'Ahmad'
# student1['age'] = 25
# student1['course'] = 'BIS'
# student1['married'] = False
#
# print(len(student))
#
# print('Lola' in student['name'])
# values = student1.values()
# print(25 in values)
#

# myFinalMarks = {'CSF': 75, 'FunPro': 80, 'WT': 85}
#
# def calculate(finalMarks):
#     total = 0
#     for i in finalMarks:
#         print(i)
#         print(finalMarks[i])
#         total += finalMarks[i]
# calculate(myFinalMarks)

# def histogram(s):
#     d = dict()
#     for c in s:
#         if c not in d:
#             d[c] = 1
#         else:
#             d[c] += 1
#     return d
#
# h= histogram("brontosaurus")
#
# print(h)
#
# h1=histogram('a')
#
# print(h1)
# print(h1.get('a',0))
# print(h1.get('B',1))


# csf = {
#     'cw1-weight': 0.4,
#     'cw1-mark': 79,
#     'exam-weight': 0.6,
#     'exam-mark': 65
# }
# print(csf.get('cw1-weight')*csf.get('cw1-mark')+csf.get('exam-weight')*csf.get('exam-mark'))


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def print_hist(h):
    d = dict()
    for c in h:
        print(c, h[c])

h=histogram('university')
print_hist(h)
