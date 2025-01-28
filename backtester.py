import vectorbt as vbt

def backtest_strategy(price_data):
    fast_ma = vbt.MA.run(price_data, 10)
    slow_ma = vbt.MA.run(price_data, 20)
    
    entries = fast_ma.ma_crossed_above(slow_ma)
    exits = fast_ma.ma_crossed_below(slow_ma)
    
    pf = vbt.Portfolio.from_signals(price_data, entries, exits)
    return pf.stats()
