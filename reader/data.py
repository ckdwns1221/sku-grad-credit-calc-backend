#검사데이터
GE = {'English': ['Lab(1)', 'Lab(2)', '영어커뮤니케이션(1)', '영어커뮤니케이션(2)'],
        'English_cnt': [0, 2], # count ,max
        '기초글쓰기': [0, 1], # 1
        '사회봉사': [0, 1], # 1
        '현대인과성경': [0, 1], # 1
        '현대인과기독교': [0, 1], # 1
        'other': ['파이데이아포럼(1)', '파이데이아포럼(2)', '파이데이아포럼', '대학생활과진로'],
        'other_cnt': [0, 2], # 2
        'one_point': ['기초글쓰기', '사회봉사', '현대인과성경', '현대인과기독교'],
        'for_loop': {'English_cnt': 0, '기초글쓰기': 0, '사회봉사': 0, '현대인과성경': 0, '현대인과기독교': 0, 'other_cnt': 0}
        }

#최신화데이터
GE_list = {'기초글쓰기': {'subject': '기초글쓰기', 'score': 2, 'category': '교필'},
           '사회봉사': {'subject': '사회봉사', 'score':1, 'category':'교필'},
           '영어커뮤니케이션(1)': {'subject': '영어커뮤니케이션(1)', 'score':2, 'category':'교필'},
           '영어커뮤니케이션(2)': {'subject': '영어커뮤니케이션(2)', 'score':2, 'category':'교필'},
           '현대인과성경': {'subject':'현대인과성경', 'score':3, 'category':'교필'},
           '현대인과기독교': {'subject':'현대인과기독교', 'score':3, 'category':'교필'},
           '대학생활과진로': {'subject':'대학생활과진로', 'score':1, 'category':'교필'},
           '파이데이아포럼': {'subject':'파이데이아포럼', 'score':1, 'category':'교필'},}

#산경데이터
IME_REQ = {
    2017:["공학통계(1)", "경영과학(1)", "제품기획및개발"],
    2018:["공학통계(1)", "캡스톤디자인"],
    2019:["공학통계(1)", "캡스톤디자인"],
    2020:["공학통계(1)", "캡스톤디자인"],
    2021:["공학통계(1)", "캡스톤디자인"],
    2022:["공학통계(1)", "캡스톤디자인"],
    2023:["공학통계(1)", "캡스톤디자인"],
}

IME_change={
    "경영과학(1)" : "경영과학",
    "취업과진로" : "진로와취창업",
	"컴퓨터프로그래밍(2)" : "객체지향 프로그래밍 언어",
	"컴퓨터프로그래밍(1)" : "인공지능 파이썬 프로그래밍",
	"작업설계" : "작업 분석 및 설계",
	"데이터분석실무" : "데이터분석및설계",
    "원가공학" : "원가공학(원격수업)",
	"산업경영공학실무(2)" : "산업경영공학실무",
}

IME_list = {
	"미적분학": {'subject':'미적분학','score':3,'category':'전선'},
	"산업경영공학개론": {'subject':'산업경영공학개론','score':3,'category':'전선'},
	"공학통계(1)": {'subject':'공학통계(1)','score':3,'category':'전필'},
	"경영과학": {'subject':'경영과학','score':3,'category':'전선'},
	"제조및생산시스템개론": {'subject':'제조및생산시스템개론','score':3,'category':'전선'},
	"진로와취창업": {'subject':'진로와취창업','score':2,'category':'전선'},
	"객체지향 프로그래밍 언어": {'subject':'객체지향 프로그래밍 언어','score':3,'category':'전선'},
	"생산운영관리": {'subject':'생산운영관리','score':3,'category':'전선'},
	"경영과학(2)": {'subject':'경영과학(2)','score':3,'category':'전선'},
	"시스템시뮬레이션": {'subject':'시스템시뮬레이션','score':3,'category':'전선'},
	"신뢰성공학": {'subject':'신뢰성공학','score':3,'category':'전선'},
	"캡스톤디자인": {'subject':'캡스톤디자인','score':3,'category':'전필'},
	"품질경영실무": {'subject':'품질경영실무','score':3,'category':'전선'},
	"공학수학": {'subject':'공학수학','score':3,'category':'전선'},
	"인공지능 파이썬 프로그래밍": {'subject':'인공지능 파이썬 프로그래밍','score':3,'category':'전선'},
	"데이터베이스": {'subject':'데이터베이스','score':3,'category':'전선'},
	"공학통계(2)": {'subject':'공학통계(2)','score':3,'category':'전선'},
	"원가공학(원격수업)": {'subject':'원가공학(원격수업)','score':3,'category':'전선'},
	"작업 분석 및 설계": {'subject':'작업 분석 및 설계','score':3,'category':'전선'},
	"제품기획및개발": {'subject':'제품기획및개발','score':3,'category':'전선'},
	"경제성공학": {'subject':'경제성공학','score':3,'category':'전선'},
	"실험계획의원리": {'subject':'실험계획의원리','score':3,'category':'전선'},
	"품질관리": {'subject':'품질관리','score':3,'category':'전선'},
	"물류및시설계획": {'subject':'물류및시설계획','score':3,'category':'전선'},
	"데이터분석및설계": {'subject':'데이터분석및설계','score':3,'category':'전선'},
	"인간공학": {'subject':'인간공학','score':3,'category':'전선'},
	"산업경영공학실무": {'subject':'산업경영공학실무','score':3,'category':'전선'},
	"빅데이터와머신러닝": {'subject':'빅데이터와머신러닝','score':3,'category':'전선'},
}

IME_grad = {
    2017:{"선택조건" : ["졸업작품", "졸업논문", "품질경영기사", "토익 800점 이상"]},
    2018:{"선택조건" : ["졸업작품", "졸업논문", "품질경영기사", "토익 800점 이상"]},
    2019:{"선택조건" : ["졸업작품", "졸업논문", "품질경영기사", "토익 800점 이상"]},
    2020:{"선택조건" : ["졸업작품", "졸업논문", "품질경영기사", "토익 800점 이상"]},
    2021:{"선택조건" : ["졸업작품", "졸업논문", "품질경영기사", "토익 800점 이상"]},
    2022:{"선택조건" : ["졸업작품", "졸업논문", "품질경영기사", "빅데이터 분석 기사"]},
    2023:{"선택조건" : ["졸업작품", "졸업논문", "품질경영기사", "빅데이터 분석 기사"]},
}