class VietnamPackage:
    def detail(self):
        print("[베트남 패키지 3박 5일] 다낭 효도여행 60만원")

if __name__ == "__main__":
    print("이 문장은 모듈에서 직접 실행할 때만 나타납니다.")
    print("해당 py에서 직접 실행한 것")
    trip_to = VietnamPackage()
    trip_to.detail()
else:
    print("이 문장은 외부에서 모듈을 불러올 때 나타납니다.")