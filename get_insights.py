from datetime import datetime
from dateutil.relativedelta import relativedelta

import pandas as pd
class insights:
    def __init__(self):
        print('Getting Insights')
        self.start_date = datetime.strptime('2020-01-01 00:00:00+0530','%Y-%m-%d %H:%M:%S%z')
        self.end_date = datetime.strptime('2020-02-13 00:00:00+0530','%Y-%m-%d %H:%M:%S%z')
        self.steps_per_week = []
        self.data = {}

    def getTotal(self, param):
        try:
            format = '%Y-%m-%d %H:%M:%S%z'
            csv_file = pd.read_csv(f'csv_data/{param}.csv')
            
            ## Changing format of date from str to datetime
            csv_file['@startDate'] = pd.to_datetime(csv_file['@startDate'],format=format)
            csv_file['@endDate'] = pd.to_datetime(csv_file['@endDate'],format=format)
            week_date = datetime.strptime(f'2020-01-07 00:00:00+0530',format)
            
            ## To calculate steps per Week
            idx = 0
            in_a_week_count = 0
            total_week_data = []
            while idx < len(csv_file["@startDate"]) and week_date <= self.end_date:
                if csv_file["@startDate"][idx] <= week_date:
                    in_a_week_count+=csv_file["@value"][idx]                
                else:
                    total_week_data.append(round(in_a_week_count, 2)) 
                    in_a_week_count = 0
                    week_date+=relativedelta(weeks=1)
                idx+=1
            self.data[f"{param}"] = total_week_data   

        except Exception as e:
            print(e)
            return

    def getAverage(self, param):
        try:
            format = '%Y-%m-%d %H:%M:%S%z'
            csv_file = pd.read_csv(f'csv_data/{param}.csv')
            
            ## Changing format of date from str to datetime
            csv_file['@startDate'] = pd.to_datetime(csv_file['@startDate'],format=format)
            csv_file['@endDate'] = pd.to_datetime(csv_file['@endDate'],format=format)
            week_date = datetime.strptime(f'2020-01-07 00:00:00+0530',format)
            
            ## To calculate steps per Week
            idx = 0
            in_a_week_count = 0
            total_week_data = []
            count = 0
            while idx < len(csv_file["@startDate"]) and week_date <= self.end_date:
                if csv_file["@startDate"][idx] <= week_date:
                    in_a_week_count+=csv_file["@value"][idx]                
                else:
                    total_week_data.append(round(in_a_week_count/count, 2)) 
                    in_a_week_count, count = 0, 0
                    week_date+=relativedelta(weeks=1)
                idx+=1
                count+=1

            self.data[f"{param}"] = total_week_data  

        except Exception as e:
            print(e)
            return


a = insights()
## Parameters whose total count would help for insights
get_total_count_params = ['step_counts', 'distanceWalkingRunning', 'activeEnergyBurned', 'basalEnergyBurned', 'appleExerciseTime' ]
## Parameters whose average would help for insights
get_average_params = ['heartRate', 'restingHeartRate', 'walkingHeartRateAverage' ]

for param in get_total_count_params:
    a.getTotal(param)

for param in get_average_params:
    a.getAverage(param)

print(a.data)