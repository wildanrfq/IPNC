from .colors import colors as c
import requests, os

class Model:

    def get_info(self, no):
        """
        This method used for get number phone information
        and return it as a list, this method take 1 parameter
        the parameter is no and data type for no is string
        """

        final_result = {} # variable for store the data

        try:
            if type(no) == str:
                if no[3] == "8" or no[3] == "2":
                    data = requests.get("https://api.antideo.com/phone/id/"+no).json()
                    if "error" not in data and data["valid"] == True:
                        if data["type"] == "FIXED_LINE": ca = "-"
                        else:
                            try:ca = data["carrier"]
                            except:ca = "-"
                        f = data["formats"]
                        final_result['number_phone'] = no
                        final_result['international'] = f['international']
                        final_result['national'] = f['national']
                        final_result['provider'] = ca
                        final_result['type'] = data['type'].replace('_', ' ').title()
                        final_result['location'] = data['location']
                        final_result['timezone'] = data['timezones']
                    elif data['valid'] == False:
                        final_result['message'] = "Nomor yang anda masukan tidak valid"
                    else:
                        final_result['message'] = "Nomor yang anda masukan salah, contoh +6281291718019"
            else:
                final_result['message'] = "Error, the parameter must be string"
        except:
            final_result['message'] = "Error, the parameter must be string"


        # returning the data
        yield final_result
    
    def get_info_cli(self, no):
        """
        this method used for get number information from cli
        """
        #
        os.system("toilet -f smblock --filter border:metal -w 50 'Indo Phone Number Checker - (  IPNC )'")
        print()
        os.system("toilet -f smblock '          by : @danrfq' --filter gay")
        print()

        for data in self.get_info(no):
            if "message" in data:
                print(c.fg.red+"[ ERROR ]\nFormat Nomor Yang Anda Masukkan Salah!"+c.end+"\n"+c.fg.lightgreen+"Contoh Nomor : +6281291718019"+c.end)
            else:
                print(c.fg.yellow+"""╔ [ {} Information ]
╠
╠ International : {}
╠ National : {}
╠ Provider : {}
╠ Type : {}
╠ Location : {}
╠ Timezones : {}
╠
╚ [ Finish ]""".
                format(no,
                        data["international"],
                        data["national"],
                        data['provider'],
                        data["type"].replace("_"," ").title(),
                        data["location"],
                        ", ".join(data["timezone"]))+c.end
                )
