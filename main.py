import json


file_to_convert = open("to_convert.txt", "r")

prop_list = []

print("Converting...")
for line in file_to_convert:
    test = line.split(",")
    prop = {
        "name": test[0][20:-6],
        "pos_x": float(test[1][1:]),
        "pos_y": float(test[3][:-1]),
        "pos_z": float(test[2]),
        "angle_x": float(test[5]),
        "angle_y": float(test[6][:-1]),
        "angle_z": float(test[4][1:]),
    }

    prop_normalized = {
        "TransformData": {
            "position": {
                "x": prop.get("pos_x"),
                "y": prop.get("pos_y"),
                "z": prop.get("pos_z")
            },
            "eulerAngles": {
                "x": prop.get("angle_x"),
                "y": prop.get("angle_y"),
                "z": prop.get("angle_z")
            },
            "localScale": {
                "x": 1.0,
                "y": 1.0,
                "z": 1.0
            }
        },
        "PathString": "",
        "Path": [],
        "Name": prop.get("name").replace("/", "#"),
        "AllowMantle": True,
        "FadeDistance": 50000.0,
        "RealmID": -1,
        "ClientSide": False,
        "Option": 0
    }

    prop_list.append(prop_normalized)

info = {"Version": "1.0.7", "Props": prop_list, "Ziplines": [], "LinkedZiplines": [], "VerticalZipLines": [], "NonVerticalZipLines": [], "SingleDoors": [], "DoubleDoors": [], "HorzDoors": [], "VerticalDoors": [], "JumpTowers": [], "Buttons": [], "Jumppads": [], "LootBins": [
], "WeaponRacks": [], "Triggers": [], "BubbleShields": [], "SpawnPoints": [], "NewLocPairs": [], "TextInfoPanels": [], "FuncWindowHints": [], "Sounds": [], "CameraPaths": [], "PlayerSpawns": [], "RespawnableHeals": [], "SpeedBoosts": [], "AnimatedCameras": []}


with open("converted.json", "w") as file:
    json.dump(info, file, separators=(',', ":"))

print("Convertion finished...")
