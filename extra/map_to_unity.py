import json

# prop = MapEditor_CreateProp( $"mdl/fx/energy_ring_edge.rmdl", < -30489.11, -2053.89, -30520 >, < 0, -90, 0 >, true, 50000, -1, 10 )
props = []
props_json = []
with open("prop_list.txt", "r") as f:
    for line in f:
        props.append(line.replace(" ", ""))


for prop in props:
    # removes useless text
    prop_info = prop[27:-2]

    # separate info
    prop_info = prop_info.split(",")

    if len(prop_info) != 11:
        print(
            f"The following prop was ignored for not following the pattern:\n{prop}\n"
        )
        continue

    prop_name = prop_info[0][1:-6].replace("/", "#")

    prop_location = {
        "z": prop_info[1].replace("<", ""),
        "x": prop_info[2],
        "y": prop_info[3].replace(">", ""),
    }
    prop_rotation = {
        "x": prop_info[4].replace("<", ""),
        "y": prop_info[5],
        "z": prop_info[6].replace(">", ""),
    }
    prop_mantle = True if prop_info[7] == "true" else False
    prop_fade_distance = prop_info[8]
    prop_realm_id = prop_info[9]
    prop_scale = prop_info[10]

    prop = {
        "TransformData": {
            "position": {
                "x": round(float(prop_location.get("x")), 2),
                "y": round(float(prop_location.get("y")), 2),
                "z": round(float(prop_location.get("z")), 2) * -1,
            },
            "eulerAngles": {
                "x": round(float(prop_rotation.get("x")), 2) * -1,
                "y": round(float(prop_rotation.get("y")), 2) * -1,
                "z": round(float(prop_rotation.get("z")), 2),
            },
            "localScale": {
                "x": round(float(prop_scale), 2),
                "y": round(float(prop_scale), 2),
                "z": round(float(prop_scale), 2),
            },
        },
        "PathString": "",
        "Path": [],
        "Name": prop_name,
        "AllowMantle": prop_mantle,
        "FadeDistance": float(prop_fade_distance),
        "RealmID": -1,
        "ClientSide": False,
        "Options": "",
    }

    props_json.append(prop)

with open("props.json", "w") as f:
    json.dump(props_json, f)
