import os
import csv
import glob

def load_sensor_data():
  sensor_data = []
  sensor_files = glob.glob(os.path.join(os.getcwd(), 'datasets', '*.csv'))

  for sensor_file in sensor_files:
    with open(sensor_file) as data_file:
      data_reader = csv.DictReader(data_file, delimiter=',')
      for row in data_file:
        sensor_data.append(row)

  return sensor_data