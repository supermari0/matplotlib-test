from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def main():
    dates = []
    for i in range(5):
        dates.append(datetime.now() - timedelta(days=i))
    plt.plot(dates, [1,2,3,4,5])
    plt.ylabel('numbers')
    plt.show()

if __name__ == '__main__':
    main()
