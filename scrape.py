import json
import requests

url = "https://tripizy.herokuapp.com/getData/?url=https://www.booking.com/hotel/ae/burj-al-arab.en-gb.html?aid=304142%26label=gen173nr-1DCAEoggI46AdIM1gEaMMBiAEBmAEJuAEXyAEM2AED6AEBiAIBqAIDuALh4-yVBsACAdICJGQ5MTc0YjU5LTIzZTAtNDczNS05Y2EyLTNlM2QzN2U4N2EwNNgCBOACAQ%26sid=70b38506eaf526ba9a9dae4a78871f14%26all_sr_blocks=7305201_355298480_2_33_0;checkin=2022-06-30;checkout=2022-07-01;dest_id=-782831;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=4;highlighted_blocks=7305201_355298480_2_33_0;hpos=4;matching_block_id=7305201_355298480_2_33_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=7305201_355298480_2_33_0__408000;srepoch=1656435205;srpvid=a6c176c2394f000c;type=total;ucfs=1%26%23hotelTmpl"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.text.encode("utf-8")
parse_json = json.loads(data)

print(parse_json["data"])