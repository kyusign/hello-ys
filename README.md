# SNS Dashboard

SNS Dashboard는 **YouTube · TikTok · Instagram** 채널의 일일 조회수를 수집해  
입력한 CPM(조회수 1 천 회당 수익)으로 예상 수익을 계산하는 파이썬 애플리케이션입니다.  
초기 설정 창에서는 **채널 URL 3개와 CPM 3개, 총 6개**만 입력합니다.

---

## 사용법

### 1. 의존성 설치

```bash
pip install -r requirements.txt
# 방법 1
python -m sns_dashboard setup

# 방법 2
python sns_dashboard/main.py setup

# 방법 3 (패키징 exe 배포본)
sns-dashboard.exe setup
python -m sns_dashboard run
python -m sns_dashboard plot

필요한 파일을 모두 정리했으니, 이제 충돌 없이 머지될 거예요. 다른 부분도 막히면 알려 주세요!
