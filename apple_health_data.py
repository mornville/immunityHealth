import pandas as pd
class Apple_health_data:
    def __init__(self):
        self.stepCount =  []
        self.heartRate = []
        self.bmi = []
        self.bodyFat = []
        self.bodyMass = []
        self.respiratory = []
        self.height = []
        self.VO2 = []

    def getStepCount(self):
        data = pd.read_csv('apple_health_data/stepCount.csv')
        data.fillna(0,inplace=True)
        self.stepCount = data
    
    def getBMI(self):
        data = pd.read_csv('apple_health_data/bmi.csv')
        data.fillna(0,inplace=True)
        self.bmi = data
    
    def getHeartRate(self):
        data = pd.read_csv('apple_health_data/heartRate.csv')
        data.fillna(0,inplace=True)
        self.heartRate = data
    
    def getVO2(self):
        data = pd.read_csv('apple_health_data/VO2.csv')
        data.fillna(0,inplace=True)
        self.VO2 = data

    def getHeight(self):
        data = pd.read_csv('apple_health_data/height.csv')
        data.fillna(0,inplace=True)
        self.height = data

    def getRespiratory(self):
        data = pd.read_csv('apple_health_data/respiratory.csv')
        data.fillna(0,inplace=True)
        self.respiratory = data
    
    def getBodyMass(self):
        data = pd.read_csv('apple_health_data/bodyMass.csv')
        data.fillna(0,inplace=True)
        self.bodyMass = data
    
    def getBodyFat(self):
        data = pd.read_csv('apple_health_data/bodyFat.csv')
        data.fillna(0,inplace=True)
        self.bodyFat = data

a = Apple_health_data()
a.getStepCount()
