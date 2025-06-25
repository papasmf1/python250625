import re  # 정규 표현식을 사용할 수 있게 해주는 모듈을 불러옵니다.

# 이메일 주소를 체크하는 함수
def validate_email(email):
    # 아래는 정규 표현식이에요.
    # 이 정규식은 이메일이 아래와 같은 규칙을 따르는지 확인합니다.
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # re.match()는 이메일이 정규식 패턴에 맞는지 확인하고, 맞으면 True, 아니면 False를 반환합니다.
    return bool(re.match(pattern, email))

# 샘플 이메일 주소 10개
emails = [
    "valid.email@example.com",  # 올바른 이메일
    "invalid-email.com",  # 잘못된 이메일
    "another_valid123@domain.co",  # 올바른 이메일
    "yetanother@example@domain.com",  # 잘못된 이메일
    "valid_email123@sub.domain.com",  # 올바른 이메일
    "wrong@domain,com",  # 잘못된 이메일
    "someone@domain..com",  # 올바른 이메일
    "correct.email123@domain.org",  # 올바른 이메일
    "invalid@domain..com",  # 올바른 이메일
    "final.valid.email@domain.com"  # 올바른 이메일
]

# 각 이메일이 유효한지 검사
results = {email: validate_email(email) for email in emails}

# 결과 출력
for email, is_valid in results.items():
    print(f"{email}: {'Valid' if is_valid else 'Invalid'}")
