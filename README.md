# 데이터 사이언스 학습 프로젝트

데이터 분석 및 웹 스크래핑 학습을 위한 Python 프로젝트입니다.

## 환경 설정

### 1. 가상환경 생성 및 활성화

```bash
# 가상환경 생성
python3 -m venv .venv

# 가상환경 활성화 (macOS/Linux)
source .venv/bin/activate

# 가상환경 활성화 (Windows)
# .venv\Scripts\activate
```

### 2. 패키지 설치

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Jupyter 실행

```bash
# JupyterLab 실행 (권장)
jupyter lab

# 또는 Jupyter Notebook 실행
jupyter notebook
```

## 설치된 주요 라이브러리

- **Jupyter**: 대화형 노트북 환경
- **Pandas**: 데이터 분석 및 조작
- **NumPy**: 수치 계산
- **Matplotlib/Seaborn/Plotly**: 데이터 시각화
- **Requests/BeautifulSoup**: 웹 스크래핑
- **Selenium**: 동적 웹 페이지 스크래핑
- **Scikit-learn**: 머신러닝

## 사용 예시

### Python 스크립트 실행
```bash
python f.py
```

### 웹 스크래핑 예시
```python
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
```

## 프로젝트 구조

```
study/
├── .venv/              # 가상환경 (설치 후 생성됨)
├── .cursorignore       # Cursor IDE 제외 파일
├── .gitignore          # Git 제외 파일
├── requirements.txt    # Python 패키지 목록
├── f.py               # 기존 스크립트
└── README.md          # 프로젝트 문서
```

## 참고사항

- 가상환경을 활성화한 상태에서 작업하세요
- 새로운 패키지 설치 시 `requirements.txt`에 추가하세요
- Jupyter 노트북 파일은 `.ipynb` 확장자를 갖습니다






