import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

# security visualiser
lefttitle, righttitle, goodorbad = st.columns((2,1,1.6))
with lefttitle:
    st.title('Stock Return Visualiser')
    st.write('Displays a line graph of the returns of your chosen securities against time')

left, middle, right = st.columns((0.5, 0.1, 2))
with left:
    assets = st.text_input("Provide asset tickers", value = "NFLX")
    dollars = st.number_input("How much would you like to invest? ($)", step = 50)
    today = pd.to_datetime('today')
    start = st.date_input('Start', value=pd.to_datetime('2023-01-01'), max_value = today - pd.Timedelta(days=1))
    end = st.date_input('End', value=today)
if len(assets) > 0:
    def relativeret(df):
        rel = df.pct_change()
        cumret = (1 + rel).cumprod() - 1
        cumret = cumret.fillna(0)
        return cumret

    with right:
            df = relativeret(yf.download(assets, start, end)['Adj Close'])
            st.header('Returns of {}'.format(assets))
            st.line_chart(df)
    with righttitle:
        with righttitle:
            st.title('\n\n')
            days = (end - start).days
            data = yf.download(assets, start=start, end=end)

            # Extract the specific start and end date share prices
            start_price = data['Adj Close'].iloc[0]
            end_price = data['Adj Close'].iloc[-1]

            # Calculate the return
            change = (((end_price - start_price)/start_price))*100
            dollarret = dollars * change / 100
            tickers_list = assets.split(',')
            number_tickers = len(tickers_list)
            multiplereturnpercentage = change.mean()
            multiplereturndollar = (multiplereturnpercentage * dollars)/100
            if number_tickers > 1:
                st.metric(label=f'Your return on \${dollars:.2f} is ${multiplereturndollar:.2f}', value=assets, delta='{:.2%}'.format(multiplereturnpercentage / 100))
            if number_tickers == 1:
                st.metric(label=f'Your return on \${dollars:.2f} is ${dollarret:.2f}', value=assets, delta='{:.2%}'.format(change / 100))

    with middle:
        st.write(' ')

    with goodorbad:
        if number_tickers == 1:
            st.title('\n')
            if change > 0.01:
                st.subheader(f"{assets} was a :green[good] investment, returning " + f":green[$] :green[{dollarret:.2f}]")
            if change < 0.01:
                st.subheader(f"{assets} was a :red[bad] investment, returning " + f":red[$] :red[{dollarret:.2f}]")
        if number_tickers > 1:
            st.title('\n')
            if multiplereturnpercentage > 0.01:
                st.subheader(f"{assets} was a :green[good] investment, returning " + f":green[$] :green[{multiplereturndollar:.2f}]")
            if multiplereturnpercentage < 0.01:
                st.subheader(f"{assets} was a :red[bad] investment, returning " + f":red[$] :red[{multiplereturndollar:.2f}]")

# port visualiser
st.write('---')
st.title('Risk Visualiser')
st.write('Displays a line graph of your portfolios returns against the S&P500, and calculates the total risk')
left2, middle, right2, right3 = st.columns((2, 1, 4, 4))
with left2:
    assets2 = st.text_input(("Provide asset tickers (comma-separated)"), value='AMZN, NFLX, TSLA', key="1")
    if len(assets2) > 0:
        start = st.date_input('Start date', value=pd.to_datetime('2023-01-01'))

with middle:
    ('')
if len(assets2) > 0:
    data = yf.download(assets2, start=start, end=end)['Adj Close']
    if data.empty:
        st.write(f"No data available for the provided asset tickers: {assets2}")
    else:
        ret_df = data.pct_change()
        cumul_ret = (ret_df + 1).cumprod() - 1
        pf_cumul_ret = cumul_ret.mean(axis=1)
        benchmark = yf.download('^GSPC', start=start, end=end)['Adj Close']
        bench_ret = benchmark.pct_change()
        bench_dev = (bench_ret + 1).cumprod() - 1
        W = (np.ones(len(ret_df.cov())) / len(ret_df.cov()))
        pf_std = (W.dot(ret_df.cov()).dot(W)) ** (1 / 2)
        ret_df.cov()

        st.subheader('Portfolio vs Index Development')
        st.line_chart(data=pd.concat([bench_dev, pf_cumul_ret], axis=1))

    with right2:
        st.subheader("Portfolio Risk:")
        pf_std
        st.subheader("Benchmark Risk:")
        bench_risk = bench_ret.std()
        bench_risk
    with right3:
        ('\n')
        ('\n')
        ('\n')
        ('\n')

        risk = pf_std / bench_risk

        if risk < 2:
            st.subheader("Your portfolio is :green[risk averse]")
        elif 2 <= risk < 3:
            st.subheader("Your portfolio is :orange[somewhat risky]")
        else:
            st.subheader("Your portfolio is :red[very risky]")
