from house_info import HouseInfo
from datetime import date

class ParticleData(HouseInfo):
  def _convert_data(self, data):
    recs = []
    for rec in data:
      recs.append(float(rec))
    return recs

  def get_data_by_area(self, rec_area=0):
    recs = super().get_data_by_area("particulate", rec_area)
    return self._convert_data(recs)
  
  def get_data_by_date(self, rec_date=date.today()):
    recs = super().get_data_by_date("particulate", rec_date)
    return self._convert_data(recs)

  def get_data_concentrations(self, data):
    particulate = {"good": 0, "moderate": 0, "bad": 0}
    key = ""
    for rec in data:
      
      if rec <= 50.0:
        key = "good"
      elif rec > 50.0 and rec <= 100.0:
        key = "moderate"
      elif rec > 100.0:
        key = "bad"

      particulate[key] = particulate[key] + 1

    return particulate