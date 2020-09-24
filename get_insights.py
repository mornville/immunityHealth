from datetime import datetime
from dateutil.relativedelta import relativedelta

import pandas as pd
class insights:
    def __init__(self):
        print('Getting Insights')
        self.start_date = datetime.strptime('2020-01-01 00:00:00+0530','%Y-%m-%d %H:%M:%S%z')
        self.end_date = datetime.strptime('2020-02-13 00:00:00+0530','%Y-%m-%d %H:%M:%S%z')
        self.steps_per_week = []

    def getStepsInsight(self):
        format = '%Y-%m-%d %H:%M:%S%z'
        step_csv = pd.read_csv('csv_data/step_counts.csv')
        
        ## Changing format of date from str to datetime
        step_csv['@startDate'] = pd.to_datetime(step_csv['@startDate'],format=format)
        step_csv['@endDate'] = pd.to_datetime(step_csv['@endDate'],format=format)
        week_date = datetime.strptime(f'2020-01-07 00:00:00+0530',format)
        
        ## To calculate steps per Week
        idx = 0
        steps_in_a_week = 0
        while idx < len(step_csv["@startDate"]) and week_date <= self.end_date:
            if step_csv["@startDate"][idx] <= week_date:
                steps_in_a_week+=step_csv["@value"][idx]                
            else:
                self.steps_per_week.append(steps_in_a_week) 
                steps_in_a_week = 0
                week_date+=relativedelta(weeks=1)
            idx+=1

    

a = insights()
a.getStepsInsight()
