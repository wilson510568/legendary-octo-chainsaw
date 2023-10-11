import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import pandas as pd


# 定義一個標楷體字體屬性
kaiu_font = FontProperties(fname=r'C:\Windows\Fonts\kaiu.ttf')


def plot_stock_trend(stock_data, stock_symbol):
    plt.figure(figsize=(12, 6))
    plt.title(f"{stock_symbol} 股價走勢圖", fontproperties=kaiu_font)  # 使用標楷體字體
    plt.plot(stock_data.index, stock_data['Close'], label='收盤價', color='blue')
    plt.xlabel('日期', fontproperties=kaiu_font)  # 使用標楷體字體
    plt.ylabel('價格', fontproperties=kaiu_font)  # 使用標楷體字體
    plt.legend(prop=kaiu_font)  # 使用標楷體字體
    plt.grid(True)
    plt.show()





while True:
    # 讓用戶輸入股票代碼
    stock_symbol = input("請輸入股票代碼 (例如：2330.TW) 或輸入 'exit' 退出：")

    if stock_symbol.lower() == 'exit':
        break

    # 創建一個股票物件
    stock = yf.Ticker(stock_symbol)

    # 獲取股息資訊
    dividends = stock.dividends
    if not dividends.empty:
        print("股息發放時間：")
        print(dividends)
    else:
        print("目前無股息資訊")

    # 獲取殖利率
    dividend_yield = stock.info["dividendYield"]
    if dividend_yield:
        print(f"殖利率：{dividend_yield * 100:.2f}%")
    else:
        print("目前無殖利率資訊")

    # 獲取最晚買入時間
    ex_dividend_date = stock.info.get("exDividendDate")
    if ex_dividend_date:
        print(f"最晚買入時間：{ex_dividend_date}")
    else:
        print("目前無最晚買入時間資訊")

    # 獲取股票價格資訊
    stock_price = stock.history(period="1d")
    if not stock_price.empty:
        print("即時股價資訊：")
        print(stock_price)
    else:
        print("無法獲取即時股價資訊")

    # 獲取基本資料
    stock_info = stock.info
    if stock_info:
        print("基本資料：")
        print(f"公司名稱: {stock_info['longName']}")
        print(f"行業: {stock_info['industry']}")
        print(f"市值: {stock_info['marketCap']}")
    else:
        print("無法獲取基本資料")

    # 下載並繪製股票走勢圖
    stock_data = stock.history(period="1y")
    if not stock_data.empty:
        plot_stock_trend(stock_data, stock_symbol)


