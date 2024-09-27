#!/Users/Quan/Desktop/crawl-venv/bin/python3

"""
Viết script tìm 50 quán bia / quán nhậu / quán bar / nhà hàng quanh toạ độ của lớp học (lên google map để lấy) với bán kính 2KM.
Ghi kết quả theo định dạng JSON vào file pymi_beer.geojson

Sử dụng Google Map API
https://developers.google.com/places/web-service/

Chú ý: phải tạo "token" để có thể truy cập API - phải tạo tài khoản google cloud, 
cần có thẻ thanh toán online quốc tế (VISA/Mastercard). Học viên không có thẻ thì đi làm thẻ.

Chú ý: giữa mỗi trang kết quả phải đợi để lấy tiếp.

Chú ý: tránh đặt ngược lat/long

- Kết quả trả về lưu theo format JSON, với mỗi điểm là một GeoJSON point (https://leafletjs.com/examples/geojson/), 
up file này lên GitHub để xem bản đồ kết quả.

- Xem mẫu GEOJSON https://github.com/tung491/make_boba_map

Store code
Store name
Address
Region
Province
District
Latlong
"""
import geojson
import csv

#each store wrapped by multi information, so create class for store
class MyPoint():
	def __init__(self, latlong, storecode, storename, address, region, province, district):
		self.latlong = latlong
		self.storecode = storecode
		self.storename = storename
		self.address = address
		self.region = region
		self.province = province
		self.district = district
	@property
	def __geo_interface__(self):
		return {'type': 'Feature',
				'geometry': {'type': 'Point', 'coordinate': (self.latlong[0], self.latlong[1])},
				'properties': {'Storecode': self.storecode, 'Storename': self.storename, 'Address': self.address,
							   'Region': self.region, 'Province': self.province, 'District': self.district}
							   }

#convert latlong to geojson format will be repeated on each item, so write a function for it
def convert_latlong(input_data):
	return tuple(map(lambda x:float(x), input_data[::-1])) #reverse to map the format of geojson

features = []
with open('Lat Long Geocoding.csv', 'r') as f:
	loc = csv.DictReader(f)
	for i in loc:
		latlong = convert_latlong(i['Latlong'].split(','))
		storecode = i['Store Code']
		storename = i['Store Name']
		address = i['Address']
		region = i['Region']
		province = i['Province']
		district = i['District']
		F = MyPoint(latlong, storecode, storename, address, region, province, district)
		features.append(F)


p_collection = geojson.FeatureCollection(features) #create Feature collection from list of Feature

with open('ConcungStore.geojson', 'w') as f:
	geojson.dump(p_collection, f)
















