from flask import Flask, render_template, request
import os
from apiclient import discovery
from google.oauth2 import service_account

app = Flask(__name__)

try:
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    secret_file = os.path.join(os.getcwd(), "g_credentials.json")

    credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=scopes)
    service = discovery.build("sheets", "v4", credentials=credentials)
    sheet = service.spreadsheets().values()
    sheet_id = '1DEY9MCfFDpO-QT3thHriFdCI8I8gbuZe_1yHC35C-JI'

except OSError as e:
    print(e)


@app.route("/")
def main():
    signed = 0
    response = sheet.get(spreadsheetId=sheet_id, range="Main!A:A").execute()
    signed = len(response['values']) - 1

    return render_template("index.html", signed=signed)


@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.form:
        name = request.form.get("user_name")
        email = request.form.get("user_email")
        range = "Main!A:B"
        body = {
            "range": range,
            "majorDimension": "ROWS",
            "values": [[name, email]]
        }

        sheet.append(spreadsheetId=sheet_id, range=range, body=body, valueInputOption='USER_ENTERED').execute()


    return render_template("congrats.html")


if __name__ == "__main__":
    app.run(debug=True)


###### example to update cells
# range_name="Main!A1:D2"
# values = [
#     [1, 2, 3, 4],
#     [2, 3, 4, 5]
# ]
#
# data = {
#     'values': values
# }
#
# sheet.update(spreadsheetId=sheet_id, body=data, range=range_name, valueInputOption='USER_ENTERED').execute()

## example get request
# response = sheet.get(spreadsheetId=sheet_id, range="Main!A:A").execute()


### example append request
# body = {
#         "range": "Main!A:A",
#         "majorDimension": "COLUMNS", #ROWS
#         "values": [
#             ["m", "a", "y", "a"]
#     ]
# }
# values = [["m"],["a"],["y"],["a"]]
# response = sheet.append(spreadsheetId=sheet_id, range="Main!A:A", body=body, valueInputOption='USER_ENTERED').execute()
#
