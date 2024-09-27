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
"""
import geojson
import csv

coor = []
with open('Lat Long Geocoding.csv', 'r') as f:
	loc = csv.DictReader(f)
	for i in loc:
		latlon = i['Latlong'].split(',')
		coor.append(tuple(map(lambda x: float(x), latlon[::-1]))) #reverse lat and long

p = [geojson.Point(i) for i in coor]

p_collection = geojson.FeatureCollection(p)

with open('testmap.geojson', 'w') as f:
	geojson.dump(p_collection, f)
















