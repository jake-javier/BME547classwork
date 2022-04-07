import requests

r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/jkj22")
print(r.text)

r2 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/M3")
print(r2.text)
r3 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/M5")
print(r3.text)

if r2.text != r3.text:
    print("Not a match")
else:
    print("It's a match!")

post = {"Name": "jkj22", "Match": "No"}

r4 = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check", json = post)
print(r4.text)