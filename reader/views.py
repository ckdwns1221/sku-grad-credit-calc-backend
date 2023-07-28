from django.shortcuts import render
from collections import defaultdict
import openpyxl

def upload_file(request):
	if request.method == 'GET':
		return render(request, 'reader/upload.html')

	file = request.FILES['file']
	wb = openpyxl.load_workbook(file)
	sheet = wb.active
#----------------------------------------------------------------------------------------------
	# already set
	area = {'교필영역', '교선영역', '전필영역', 
			'전선영역', '복필영역', '복전영역', '부전공영역', 
			'일선영역', '교직영역'} #, '졸업사정결과'}
	short_area = {'교필', '교선', '전필', 
			'전선', '복필', '복전', '부전공', 
			'일선', '교직', '채플'}
	score_need_list = {'전필요구학점', '전선요구학점', '복수전공필수요구학점', 
                    '복수전공요구학점', '부전공요구학점'}
	score_for_grade = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0':3.0, 
					'C+': 2.5, 'C0': 2.0, 'D+':1.5, 'D0': 1.0}
	info_category = ['major', 'minor', 'student_num', 'grade', 
                  'name', 'score_need', 'socre_did']
	info_idx = ['A2', 'F2', 'J2', 'M2', 'O2', 'Y2', 'AB2']
	year = {'2015', '2016', '2017', '2018', '2019', '2020', '2021', 
         '2022', '2023', '2024', '2025', '2026'}
	semester = {'1학기', '2학기'}
 
	# set during runtime
	score_need = defaultdict(int)	# 영역별 요구 학점
	score_did = defaultdict(float)	# 영역별 이수 학점
	subject_did = defaultdict(list)	# 수강한 과목 모두 (이건 하지 말까 고민중 semester_subject를 모아둔 느낌) => 필요하다!! # [영역, 학점, 등급]
	subject_didnot = defaultdict(dict) # 수강하지 않은 필수 과목 => set(필수 과목) 해서 discard 하는방식

	semester_grade = defaultdict(dict) # 학년별, 학기별 평점(grade), 이수 학점(score)
	for i in range(1, 6):	# 학년별
		for j in range(1, 3):	# 학기별
			semester_grade[(i, j)] = defaultdict(float)

	semester_subject = defaultdict(dict) # 학년별, 학기별 수강 과목
	for i in range(1, 6):	# 학년별
		for j in range(1, 3):	# 학기별
			semester_subject[(i, j)] = list()

	# a f j m o y ab	
	
	student = dict()
	for i in range(7):
		student[info_category[i]] = sheet[info_idx[i]].value
	
	ex = set()
	j = 1
	while j < 150: # 수강 학기 매칭 ex) 1학년 1학기 => 19년도 1학기
		if sheet[str('X'+str(j))].value in year and sheet[str('Z'+str(j))].value in semester:
			ex.add((str(sheet[str('X'+str(j))].value), str(sheet[str('Z'+str(j))].value)[0]))	# ex) (2019,1)
		j += 1
	student_semester = []
	for i in ex:
		student_semester.append(i)
	student_semester.sort()

	semester_dict = dict()
	j = 0
	for i in range(len(student_semester)):
		j += 1
		semester_dict[student_semester[i]] = ((i//2)+1, j)
		j %= 2

	j = 1
	while j < 150: # just for the example

		if sheet[str('A'+str(j))].value and sheet[str('A'+str(j))].value[:3] == '교필:':
			total_data = list(sheet[str('A'+str(j))].value.split(' '))
			for data in total_data:
				sub, score = map(str, data.split(':'))
				score_did[sub] += float(score)
     
		if sheet[str('A'+str(j))].value in area: # ex) 교필영역이 area집합에 있으면
			j += 2
	# 영역  개설학부(과)  이수구분	강좌명	학점  등급	년도  학기  비고	
	# A		B			G		I    S	  U    X	Z	AB

			while sheet[str('G'+str(j))].value in short_area:	# ex) 해당 영역(교필영역)에 수강한 과목이 있으면

				ex_semester = (semester_dict[(sheet[str('X'+str(j))].value, sheet[str('Z'+str(j))].value[0])])
    
				if sheet[str('U'+str(j))].value != 'P' and sheet[str('U'+str(j))].value != 'F': # F맞으면 학점이 하이폰(-)으로 나오나요?
					semester_grade[ex_semester]['S'] += int(sheet[str('S'+str(j))].value) # 해당 과목 이수 학점
					semester_grade[ex_semester]['G'] += int(sheet[str('S'+str(j))].value)*score_for_grade[sheet[str('U'+str(j))].value]
        
				if sheet[str('U'+str(j))].value == 'P':
					semester_grade[ex_semester]['P'] += int(sheet[str('S'+str(j))].value)
     
				# [영역, 학점, 등급]
				subject_did[sheet[str('I'+str(j))].value] = [sheet[str('G'+str(j))].value, sheet[str('S'+str(j))].value, sheet[str('U'+str(j))].value]	
				semester_subject[ex_semester].append(sheet[str('I'+str(j))].value)

				j += 1	# excel 다음 행으로
				if sheet[str('A'+str(j+2))].value and sheet[str('A'+str(j+2))].value[:-3] in score_need_list: 
					score_need[str(sheet[str('A'+str(j+2))].value[:-3])] = int(str(sheet[str('N'+str(j+2))].value))
					score_need[str(sheet[str('P'+str(j+2))].value[:-3])] = int(str(sheet[str('W'+str(j+2))].value))
					break	# 요구학점 나오면 해당 영역 종료

		else:
			j += 1

	print(f'score_need \n{score_need}')
	print(f'score_did \n{score_did}')	
	print(f'subject_did \n{subject_did}')
	print(f'student \n{student}')
	print(f'semester_grade \n{semester_grade}')
	print(f'semester_subject \n{semester_subject}')

	for i in range(1, 6):
		for j in range(1, 3):
			if semester_grade[(i, j)]['S']:
				semester_grade[(i, j)]['G'] /= semester_grade[(i, j)]['S']
				semester_grade[(i, j)]['S'] += semester_grade[(i, j)]['P']  # 계산할때는 패논패 계산 없이 함

	return render(request, 'reader/upload.html', {'message': 'File uploaded successfully.'})

