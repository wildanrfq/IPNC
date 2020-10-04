import requests

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
