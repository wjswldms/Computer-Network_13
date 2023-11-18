# 주최자 클래스 정의
class Organizer:
    def __init__(self, name):
        self.name = name # 합승자 이름
        self.attendees = [] # 출석한 사람들의 리스트

    def __str__(self):
        return f"{self.name} (출석인원: {len(self.attendees)})"

    def check_attendance(self, person):
        # 출석한 사람을 리스트에 추가하
        self.attendees.append(person)
        print(f"{person}님이 {self.name} 주최자의 택시합승에 출석하셨습니다.")

# 주최자 객체 생성
organizer = Organizer("김유중 교수님")


# 테스트를 위한 임의의 출석자 리스트 생성
attendees = ["정승원", "김한수", "전지은"]

for person in attendees:
    organizer.check_attendance(person)
