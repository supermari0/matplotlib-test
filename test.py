from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def main():
    dates = []
    for i in range(1000):
        dates.append(datetime.now() - timedelta(days=i))
    plt.ylabel('numbers')
    plt.xlabel('dates')
    fig, ax = plt.subplots()
    ax.plot_date(dates, range(1000), marker='', linestyle='-')
    fig.autofmt_xdate()
    plt.savefig('./test.png')

if __name__ == '__main__':
    main()
