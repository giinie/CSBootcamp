# 주어진 주식 가격을 보고 얻을 수 있는 최대 수익을 구하는 알고리즘
# 입력: 주식 가격의 변화 값(리스트: prices)
# 출력: 한 주를 한 번 사고팔아 얻을 수 있는 최대 수익 값

def max_profit(prices):
    n = len(prices)
    max_profit = 0         # 최대 수익은 항상 0 이상의 값
    min_price = prices[0]  # 첫째 날의 주가를 주가의 최솟값으로 기억

    for i in range(1, n):  # 1부터 n-1까지 반복
        profit = prices[i] - min_price  # 지금까지의 최솟값에 주식을 사서 i날에 팔 때의 수익
        if profit > max_profit:   # 이 수익이 지금까지 최대 수익보다 크면 값을 고침
            max_profit = profit
        if prices[i] < min_price: # i날 주가가 최솟값보다 작으면 값을 고침
            min_price = prices[i]

    return max_profit

stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock))
