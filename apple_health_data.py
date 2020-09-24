import pandas as pd
import xmltodict

class apple_health_data:
    def __init__(self):
        self.input_path = './export.xml'
    
    def extractData(self):
        with open(self.input_path, 'r') as xml_file:
            self.input_data = xmltodict.parse(xml_file.read())
        records_list = self.input_data['HealthData']['Record']
        df = pd.DataFrame(records_list)
        # print(df['@type'].unique())

        ## Filtering data for a 6 weeks
        start_date, end_date = '2019-03-01 00:00:00 +0530', '2019-04-13 00:00:00 +0530'
        mask = (df['@startDate'] > start_date) & (df['@startDate'] <= end_date)
        df = df.loc[mask]
        
        ## Formatting date
        format = '%Y-%m-%d %H:%M:%S %z'
        df['@creationDate'] = pd.to_datetime(df['@creationDate'], format=format)
        df['@startDate'] = pd.to_datetime(df['@startDate'], format=format)
        df['@endDate'] = pd.to_datetime(df['@endDate'], format=format)

        #### Activity ####    
        # StepCount
        step_counts = df[df['@type'] == 'HKQuantityTypeIdentifierStepCount']
        step_counts.to_csv('step_counts.csv', index=False)

        # Excercise
        distanceWalkingRunning = df[df['@type'] == 'HKQuantityTypeIdentifierDistanceWalkingRunning']
        distanceWalkingRunning.to_csv('distanceWalkingRunning.csv', index=False)

        basalEnergyBurned = df[df['@type'] == 'HKQuantityTypeIdentifierBasalEnergyBurned']
        basalEnergyBurned.to_csv('basalEnergyBurned.csv', index=False)

        appleExerciseTime = df[df['@type'] == 'HKQuantityTypeIdentifierAppleExerciseTime']
        appleExerciseTime.to_csv('appleExerciseTime.csv', index=False)

        activeEnergyBurned = df[df['@type'] == 'HKQuantityTypeIdentifierActiveEnergyBurned']
        activeEnergyBurned.to_csv('activeEnergyBurned.csv', index=False)

        
        #### Vitals  ####
        # heart Rate
        heartRate = df[df['@type'] == 'HKQuantityTypeIdentifierHeartRate']
        heartRate.to_csv('heartRate.csv', index=False)

        restingHeartRate = df[df['@type'] == 'HKQuantityTypeIdentifierRestingHeartRate']
        restingHeartRate.to_csv('restingHeartRate.csv', index=False)

        walkingHeartRateAverage = df[df['@type'] == 'HKQuantityTypeIdentifierWalkingHeartRateAverage']
        walkingHeartRateAverage.to_csv('walkingHeartRateAverage.csv', index=False)

        # Respiratory Rate
        respiratoryRate = df[df['@type'] == 'HKQuantityTypeIdentifierRespiratoryRate']
        respiratoryRate.to_csv('respiratoryRate.csv', index=False)

        #BMI and body Mass
        bm = df[df['@type'] == 'HKQuantityTypeIdentifierBodyMass']
        bm.to_csv('bm.csv', index=False)  

        bmi = df[df['@type'] == 'HKQuantityTypeIdentifierBodyMassIndex']
        bmi.to_csv('bmi.csv', index=False)  

        # VO2
        vo2 = df[df['@type'] == 'HKQuantityTypeIdentifierVO2Max']
        vo2.to_csv('vo2.csv', index=False)  



        
a = apple_health_data()
a.extractData()
