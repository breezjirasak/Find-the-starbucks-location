from data import Data
from ui import App

if __name__ == '__main__':
    csv_name = 'starbucks location.csv'
    run = App(Data(csv_name))
    run.run()