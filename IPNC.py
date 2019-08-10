# Indo Phone Number Checker ( IPNC )
# Please Don't Recode! Respect The Creator ;)
# this tools is created by danrfq (@danrfq)

import requests, os
from colors import colors as c

os.system("toilet -f smblock --filter border:metal -w 50 'Indo Phone Number Checker - (  IPNC )'")
print()
os.system("toilet -f smblock '          by : @danrfq' --filter gay")
print()

no = "+62"+input(c.fg.yellow+"Masukkan Nomor HP Anda : +62")

if no[3] == "8" or no[3] == "2":
	data = requests.get("https://api.antideo.com/phone/id/"+no).json()
	print(c.fg.lightgreen+"Processing...."+c.end)
	if "error" not in data and data["valid"] == True:
		if data["type"] == "FIXED_LINE": ca = "-"
		else:
			try:ca = data["carrier"]
			except:ca = "-"
		f = data["formats"]
		print(c.fg.yellow+"""╔ [ {} Information ]
╠
╠ International : {}
╠ National : {}
╠ Provider : {}
╠ Type : {}
╠ Location : {}
╠ Timezones : {}
╠
╚ [ Finish ]""".format(no,f["international"],f["national"],ca,data["type"].replace("_"," ").title(),data["location"],", ".join(data["timezones"]))+c.end)
	elif data["valid"] == False: print(c.fg.red+"[ ERROR ]\nNomor Yang Anda Masukkan Tidak Valid!"+c.end)

else: print(c.fg.red+"[ ERROR ]\nFormat Nomor Yang Anda Masukkan Salah!"+c.end+"\n"+c.fg.lightgreen+"Contoh Nomor : +6281291718019"+c.end)