import calendar

#calendar 라이브러리 사용해서 해결한 방법
def solve_1(start_year,end_year):
    fisrt_sunday=0
    """calendar.weekday(year,month,day) 입력시 해당 요일을 0-6 내의 숫자로 반환
        매월 1일이 일요일인 경우를 구해야 하므로 년도/월만 바꾸고 요일은 고정.
    """
    for year in range(start_year,end_year+1):
        if calendar.weekday(year,1,1)==6:
            fisrt_sunday+=1
        if calendar.weekday(year, 2, 1) == 6:
            fisrt_sunday += 1
        if calendar.weekday(year, 3, 1) == 6:
            fisrt_sunday += 1
        if calendar.weekday(year, 4, 1) == 6:
            fisrt_sunday += 1
        if calendar.weekday(year, 5, 1) == 6:
            fisrt_sunday += 1
        if calendar.weekday(year, 6, 1) == 6:
            fisrt_sunday += 1
        if calendar.weekday(year, 7, 1) == 6:
            fisrt_sunday += 1
        if calendar.weekday(year, 8, 1) == 6:
            fisrt_sunday += 1
        if calendar.weekday(year, 9, 1) == 6:
            fisrt_sunday += 1
        if calendar.weekday(year, 10, 1) == 6:
            fisrt_sunday += 1
        if calendar.weekday(year, 11, 1) == 6:
            fisrt_sunday += 1
        if calendar.weekday(year, 12, 1) == 6:
            fisrt_sunday += 1
    return fisrt_sunday


def solve_2(start_year,end_year):
    ans=0

    leap_year=[31,29,31,30,31,30,31,31,30,31,30,31]#윤년일 경우
    not_leap_year=[31,28,31,30,31,30,31,31,30,31,30,31]#윤년이 아닐 경우

    def month(li,start):#다음 년도 1월 1일의 요일과 해당 년도 내의 sunday 개수 반환
        ans=0
        for month in li:
            if start == 6:
                ans += 1
            start = (start + month - 28) % 7
        return [ans,(start + 3) % 7]

    start=month(not_leap_year,0)[1]#1901년의 1월 1일 시작 요일 계산

    while(start_year<end_year+1):
        if start_year%100!=0:# 100으로 나눠지지 않는 경우
            if start_year%4==0:
                li = month(leap_year, start)
            else:
                li=month(not_leap_year, start)
        else:
            if start_year%400==0:# 100으로 나눠지고, 400으로도 나눠지는 경우
                li = month(leap_year, start)
            else:
                li = month(not_leap_year, start)
        ans += li[0]# 해당 년도의 sunday 개수 추가
        start=li[1]#다음 년도의 1월1일 요일로 변경
        start_year+=1#년도 변경

    return ans


print('solve1:',solve_1(1901,2000))
print('solve2:',solve_2(1901,2000))