import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

def plot_equity_curve(portfolio_value, Open, Open_time, split_time):
    portfolio_value = pd.Series(portfolio_value)
    Open_time = pd.to_datetime(Open_time)
    
    market_retn = Open/Open.iloc[0] - 1
    portfolio_retn = portfolio_value/portfolio_value.iloc[0]-1
    
    filter_time_in = Open_time < split_time
    filter_time_out = ~filter_time_in
    
    cummax_in = portfolio_value[filter_time_in].cummax()
    cummax_out = portfolio_value[filter_time_out].cummax()

    high_points_in = portfolio_value[filter_time_in] >= cummax_in
    high_points_out = portfolio_value[filter_time_out] >= cummax_out

    drawdown_in = (portfolio_value[filter_time_in] - cummax_in) / cummax_in
    drawdown_out = (portfolio_value[filter_time_out] - cummax_out) / cummax_out
    
    #
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 12), gridspec_kw={'height_ratios': [5, 1]})
    
    ax1.plot(Open_time, market_retn, label='Buy&Hold', color='#17becf', alpha=0.5)
    ax1.plot(Open_time, portfolio_retn, linewidth=1.5, label='Equity')

    ax1.scatter(Open_time[high_points_in], portfolio_retn[high_points_in], 
                color='#39FF14', marker='o', s=40)
    ax1.scatter(Open_time[high_points_out], portfolio_retn[high_points_out], 
                color='#FF6347', marker='o', s=40)
    ax1.axvline(x=split_time, color='blue', linestyle='--')
    ax1.axhline(y=0, color='black', linestyle='--', linewidth=1)
    ax1.tick_params(axis='both', which='major', labelsize=15)
    ax1.set_title('Equity vs. Buy&Hold', fontsize=20)
    ax1.set_ylabel('Profit (%)', fontsize=20)
    ax1.legend(loc='upper left')
    ax1.grid()
    
    ax2.fill_between(Open_time[filter_time_in], drawdown_in, 0, color='red', alpha=0.3)
    ax2.fill_between(Open_time[filter_time_out], drawdown_out, 0, color='red', alpha=0.3)
    ax2.axvline(x=split_time, color='blue', linestyle='--')
    ax1.tick_params(axis='y', which='major', labelsize=15)
    ax2.set_title('MDD')
    ax2.set_xlabel('Time')
    ax2.grid(True)
    
    plt.tight_layout()
    plt.show()