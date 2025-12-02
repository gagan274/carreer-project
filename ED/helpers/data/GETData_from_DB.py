# Library Imports
from dotenv import load_dotenv
import os
from pymongo import MongoClient,DESCENDING

# Loading the data from .env file
load_dotenv()
MONGO_URI = os.getenv('MONGO_HOST_CONNECTION')
MONGO_DB = os.getenv('MONGO_DB')
client = MongoClient(MONGO_URI)
db = client[MONGO_DB]

# Declaring the db connection and List of all the collection.
collection_Login = db['login']
collection_Register = db['register']
collection_Otp = db['otp']
collection_UserMetaData = db['UserMetaData']
collection_realtimeData = db['Realtime_Data']
collection_Alerts = db['Realtime_Alerts']

# Projections declaration.
projection_4_Dashboard_LiveData={
    '_id': 0,
    'gateway_id': 1,
    'rack_0.BatteryPackVoltage': 1,
    'rack_0.BatteryChargeCurrent': 1,
    'rack_0.BatteryChargeDiscurrent': 1,
    'rack_0.SOC': 1,
    'rack_0.SOH': 1,
    'rack_0.timestamp':1,
    'rack_0.ChargeContactor':1,
    'rack_0.DischargeContactor':1,
    'rack_1.BatteryPackVoltage': 1,
    'rack_1.BatteryChargeCurrent': 1,
    'rack_1.BatteryChargeDiscurrent': 1,
    'rack_1.SOC': 1,
    'rack_1.SOH': 1,
    'rack_1.timestamp':1,
    'rack_1.ChargeContactor':1,
    'rack_1.DischargeContactor':1,
    'rack_2.BatteryPackVoltage': 1,
    'rack_2.BatteryChargeCurrent': 1,
    'rack_2.BatteryChargeDiscurrent': 1,
    'rack_2.SOC': 1,
    'rack_2.SOH': 1,
    'rack_2.timestamp':1,
    'rack_2.ChargeContactor':1,
    'rack_2.DischargeContactor':1,
    'rack_3.BatteryPackVoltage': 1,
    'rack_3.BatteryChargeCurrent': 1,
    'rack_3.BatteryChargeDiscurrent': 1,
    'rack_3.SOC': 1,
    'rack_3.SOH': 1,
    'rack_3.timestamp':1,
    'rack_3.ChargeContactor':1,
    'rack_3.DischargeContactor':1,
    'rack_4.BatteryPackVoltage': 1,
    'rack_4.BatteryChargeCurrent': 1,
    'rack_4.BatteryChargeDiscurrent': 1,
    'rack_4.SOC': 1,
    'rack_4.SOH': 1,
    'rack_4.timestamp':1,
    'rack_4.ChargeContactor':1,
    'rack_4.DischargeContactor':1,
    'rack_5.BatteryPackVoltage': 1,
    'rack_5.BatteryChargeCurrent': 1,
    'rack_5.BatteryChargeDiscurrent': 1,
    'rack_5.SOC': 1,
    'rack_5.SOH': 1,
    'rack_5.timestamp':1,
    'rack_5.ChargeContactor':1,
    'rack_5.DischargeContactor':1,
    'rack_6.BatteryPackVoltage': 1,
    'rack_6.BatteryChargeCurrent': 1,
    'rack_6.BatteryChargeDiscurrent': 1,
    'rack_6.SOC': 1,
    'rack_6.SOH': 1,
    'rack_6.timestamp':1,
    'rack_6.ChargeContactor':1,
    'rack_6.DischargeContactor':1,
    'rack_7.BatteryPackVoltage': 1,
    'rack_7.BatteryChargeCurrent': 1,
    'rack_7.BatteryChargeDiscurrent': 1,
    'rack_7.SOC': 1,
    'rack_7.SOH': 1,
    'rack_7.timestamp':1,
    'rack_7.ChargeContactor':1,
    'rack_7.DischargeContactor':1,
    'rack_8.BatteryPackVoltage': 1,
    'rack_8.BatteryChargeCurrent': 1,
    'rack_8.BatteryChargeDiscurrent': 1,
    'rack_8.SOC': 1,
    'rack_8.SOH': 1,
    'rack_8.timestamp':1,
    'rack_8.ChargeContactor':1,
    'rack_8.DischargeContactor':1,
    'rack_9.BatteryPackVoltage': 1,
    'rack_9.BatteryChargeCurrent': 1,
    'rack_9.BatteryChargeDiscurrent': 1,
    'rack_9.SOC': 1,
    'rack_9.SOH': 1,
    'rack_9.timestamp':1,
    'rack_9.ChargeContactor':1,
    'rack_9.DischargeContactor':1,
    'rack_10.BatteryPackVoltage': 1,
    'rack_10.BatteryChargeCurrent': 1,
    'rack_10.BatteryChargeDiscurrent': 1,
    'rack_10.SOC': 1,
    'rack_10.SOH': 1,
    'rack_10.timestamp':1,
    'rack_10.ChargeContactor':1,
    'rack_10.DischargeContactor':1,
    'rack_11.BatteryPackVoltage': 1,
    'rack_11.BatteryChargeCurrent': 1,
    'rack_11.BatteryChargeDiscurrent': 1,
    'rack_11.SOC': 1,
    'rack_11.SOH': 1,
    'rack_11.timestamp':1,
    'rack_11.ChargeContactor':1,
    'rack_11.DischargeContactor':1
}

projection_4_SOC_SOH_KPI = {
    'rack_0.SOC': 1,
    'rack_0.SOH': 1,
    'rack_1.SOC': 1,
    'rack_1.SOH': 1,
    'rack_2.SOC': 1,
    'rack_2.SOH': 1,
    'rack_3.SOC': 1,
    'rack_3.SOH': 1,
    'rack_4.SOC': 1,
    'rack_4.SOH': 1,
    'rack_5.SOC': 1,
    'rack_5.SOH': 1,
    'rack_6.SOC': 1,
    'rack_6.SOH': 1,
    'rack_7.SOC': 1,
    'rack_7.SOH': 1,
    'rack_8.SOC': 1,
    'rack_8.SOH': 1,
    'rack_9.SOC': 1,
    'rack_9.SOH': 1,
    'rack_10.SOC': 1,
    'rack_10.SOH': 1,
    'rack_11.SOC': 1,
    'rack_11.SOH': 1,
}


def getDataWithProjection(collection, query, projection):
    return collection.find_one(query, projection)

def getDataWithoutProjection(collection, query):
   return collection.find_one(query)

def getDataWithDescending(collection, query):
    return collection.find(query).sort('_id', -1).limit(1)