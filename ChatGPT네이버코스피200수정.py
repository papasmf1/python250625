import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

def clean_number(text):
    """숫자 문자열에서 쉼표를 제거하고 정수로 변환"""
    if isinstance(text, str):
        return re.sub(r'[^\d.-]', '', text)
    return text

def get_kospi200_top_stocks(max_pages=10):
    """
    네이버 금융에서 코스피200 편입종목 상위 데이터를 크롤링
    
    Args:
        max_pages: 크롤링할 최대 페이지 수 (기본값: 10)
    
    Returns:
        DataFrame: 코스피200 편입종목 데이터
    """
    base_url = "https://finance.naver.com/sise/entryJongmok.naver"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    
    all_data = []
    total_items = 0
    
    for page in range(1, max_pages + 1):
        try:
            print(f"페이지 {page}/{max_pages} 크롤링 중...")
            params = {
                "type": "KPI200",
                "page": page
            }
            
            response = requests.get(base_url, params=params, headers=headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, "html.parser")
            
            # 편입종목 상위 테이블 찾기
            table = soup.find("table", class_="type_1")
            if not table:
                print(f"페이지 {page}에서 테이블을 찾을 수 없습니다.")
                continue
                
            rows = table.find_all("tr")
            page_items = 0
            
            for row in rows:
                cols = row.find_all("td")
                if len(cols) == 7:  # 유효한 데이터 행인지 확인
                    stock_name = cols[0].get_text(strip=True)
                    current_price = cols[1].get_text(strip=True)
                    
                    # 전일비 추출 (상승/하락/보합 구분)
                    change_elem = cols[2].find("span", class_="tah")
                    change = change_elem.get_text(strip=True) if change_elem else "0"
                    
                    # 상승/하락/보합 상태 확인
                    status = None
                    if cols[2].find("em", class_="bu_pup"):
                        status = "상승"
                    elif cols[2].find("em", class_="bu_pdn"):
                        status = "하락"
                    elif cols[2].find("em", class_="bu_pn"):
                        status = "보합"
                    
                    change_rate = cols[3].get_text(strip=True)
                    volume = cols[4].get_text(strip=True)
                    amount = cols[5].get_text(strip=True)
                    market_cap = cols[6].get_text(strip=True)
                    
                    # 종목 코드 추출 (종목 링크에서)
                    stock_link = cols[0].find("a")
                    stock_code = None
                    if stock_link and 'href' in stock_link.attrs:
                        code_match = re.search(r'code=(\d+)', stock_link['href'])
                        if code_match:
                            stock_code = code_match.group(1)
                    
                    all_data.append({
                        "종목코드": stock_code,
                        "종목명": stock_name,
                        "현재가": current_price,
                        "전일비": change,
                        "상태": status,
                        "등락률": change_rate,
                        "거래량": volume,
                        "거래대금(백만)": amount,
                        "시가총액(억)": market_cap
                    })
                    page_items += 1
            
            total_items += page_items
            print(f"페이지 {page} 완료: {page_items}개 종목 추가 (현재 총 {total_items}개)")
            
            # 너무 빠른 요청은 차단될 수 있으므로 잠시 대기
            time.sleep(1.0)  # 안정성을 위해 대기 시간 증가
            
        except Exception as e:
            print(f"페이지 {page} 크롤링 중 오류 발생: {e}")
    
    if not all_data:
        print("크롤링된 데이터가 없습니다.")
        return pd.DataFrame()
    
    # DataFrame 생성 및 데이터 전처리
    df = pd.DataFrame(all_data)
    
    # 숫자 데이터 전처리
    numeric_columns = ['현재가', '전일비', '거래량', '거래대금(백만)', '시가총액(억)']
    for col in numeric_columns:
        df[col] = df[col].apply(clean_number)
    
    # 등락률에서 퍼센트 기호 제거
    df['등락률'] = df['등락률'].str.replace('%', '').astype(float)
    
    # 날짜 및 시간 정보 추가
    df['수집일시'] = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
    
    print(f"총 {len(df)}개 종목 데이터 크롤링 완료")
    return df

def save_to_excel(df, filename="코스피200_종목_전체.xlsx"):
    """데이터프레임을 엑셀 파일로 저장"""
    try:
        df.to_excel(filename, index=False)
        print(f"{filename} 파일로 저장되었습니다.")
        return True
    except Exception as e:
        print(f"파일 저장 중 오류 발생: {e}")
        return False

# Example usage
if __name__ == "__main__":
    # 10개 페이지 크롤링 (약 100개 종목)
    kospi200_stocks = get_kospi200_top_stocks(max_pages=10)  
    
    if not kospi200_stocks.empty:
        # 처음 10개 종목만 출력
        print("\n크롤링된 데이터 샘플 (상위 10개):")
        print(kospi200_stocks.head(10))  
        
        # 결과 요약 출력
        print(f"\n크롤링 결과 요약:")
        print(f"- 총 종목 수: {len(kospi200_stocks)}개")
        print(f"- 상승 종목: {len(kospi200_stocks[kospi200_stocks['상태'] == '상승'])}개")
        print(f"- 하락 종목: {len(kospi200_stocks[kospi200_stocks['상태'] == '하락'])}개")
        print(f"- 보합 종목: {len(kospi200_stocks[kospi200_stocks['상태'] == '보합'])}개")
        
        # 엑셀 파일로 저장
        save_to_excel(kospi200_stocks)