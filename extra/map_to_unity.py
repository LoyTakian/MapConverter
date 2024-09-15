import json

props = []
props_json = []
vertical_ziplines_json = []
horizontal_ziplines_json = []

with open("prop_list.txt", "r") as f:
    for line in f:
        props.append(line.replace(" ", ""))


for prop in props:
    # Manage prop options
    if prop[:5] == "prop.":
        if not props_json[-1]["Options"]:
            props_json[-1]["Options"] = prop[5:-1]
        else:
            props_json[-1]["Options"] = (
                props_json[-1]["Options"].strip("\n") + f"\n{prop[5:-1]}"
            )

    # Manage Ziplines
    elif prop[:32] == "MapEditor_CreateZiplineFromUnity":
        prop_info = prop[32:-1]
        prop_info = prop_info.split(",")

        if len(prop_info) != 33:
            print(
                f"The following prop was ignored for not following the 'zipline' pattern:\n{prop} -> {len(prop_info)}\n"
            )
            continue

        prop_location = {
            "z": prop_info[0][2:],
            "x": prop_info[1],
            "y": prop_info[2][:-1],
            "2z": prop_info[6][1:],
            "2x": prop_info[7],
            "2y": prop_info[8][:-1],
        }

        prop_rotation = {
            "x": prop_info[3][1:],
            "y": prop_info[4],
            "z": prop_info[5][:-1],
            "2x": prop_info[9][1:],
            "2y": prop_info[10],
            "2z": prop_info[11][:-1],
        }
        prop_is_vertical = prop_info[12]
        prop_fade_distance = prop_info[13]
        prop_scale = prop_info[14]
        prop_width = prop_info[15]
        prop_speed_scale = prop_info[16]
        prop_length_scale = prop_info[17]
        prop_preserve_velocity = prop_info[18]
        prop_drop_to_bottom = prop_info[19]
        prop_auto_detach_start = prop_info[20]
        prop_auto_detach_end = prop_info[21]
        prop_rest_point = prop_info[22]
        prop_push_off_in_direction = prop_info[23]
        prop_is_moving = prop_info[24]
        prop_detach_end_on_spawn = prop_info[25]
        prop_detach_end_on_use = prop_info[26]
        empty_list = []
        prop_panel_timer_min = prop_info[30]
        prop_panel_timer_max = prop_info[31]
        prop_panel_max_use = prop_info[32][:-1]

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
            "ShowZipline": True,
            "ShowZiplineDistance": round(float(prop_fade_distance), 2),
            "ShowAutoDetachDistance": True,
            "Name": "invisible_vertical_zipline"
            if prop_is_vertical == "true"
            else "invisible_invisible_non_vertical_zipline",
            "ZiplineStart": {
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
            "ZiplineEnd": {
                "position": {
                    "x": round(float(prop_location.get("2x")), 2),
                    "y": round(float(prop_location.get("2y")), 2),
                    "z": round(float(prop_location.get("2z")), 2) * -1,
                },
                "eulerAngles": {
                    "x": round(float(prop_rotation.get("2x")), 2) * -1,
                    "y": round(float(prop_rotation.get("2y")), 2) * -1,
                    "z": round(float(prop_rotation.get("2z")), 2),
                },
                "localScale": {
                    "x": round(float(prop_scale), 2),
                    "y": round(float(prop_scale), 2),
                    "z": round(float(prop_scale), 2),
                },
            },
            "ArmOffsetStart": 0.0,
            "ArmOffsetEnd": 0.0,
            "FadeDistance": 9.0,
            "Scale": round(float(prop_scale), 2),
            "Width": round(float(prop_width), 2),
            "SpeedScale": round(float(prop_speed_scale), 2),
            "LengthScale": round(float(prop_length_scale), 2),
            "PreserveVelocity": True if prop_preserve_velocity == "true" else False,
            "DropToBottom": True if prop_drop_to_bottom == "true" else False,
            "AutoDetachStart": round(float(prop_auto_detach_start), 2),
            "AutoDetachEnd": round(float(prop_auto_detach_end), 2),
            "RestPoint": True if prop_rest_point == "true" else False,
            "PushOffInDirectionX": True
            if prop_push_off_in_direction == "true"
            else False,
            "IsMoving": True if prop_is_moving == "true" else False,
            "DetachEndOnSpawn": True if prop_detach_end_on_spawn == "true" else False,
            "DetachEndOnUse": True if prop_detach_end_on_use == "true" else False,
            "Panels": [],
            "PanelTimerMin": round(float(prop_panel_timer_min), 2),
            "PanelTimerMax": round(float(prop_panel_timer_max), 2),
            "PanelMaxUse": int(prop_scale),
            "ShowArmOffsetStart": False,
            "ShowArmOffsetEnd": False,
        }

        if prop_is_vertical == "true":
            vertical_ziplines_json.append(prop)
        else:
            horizontal_ziplines_json.append(prop)

    # Manage common props
    else:
        prop_info = prop[27:-2]
        prop_info = prop_info.split(",")

        if len(prop_info) != 11:
            if len(prop_info) > 1:
                print(
                    f"The following prop was ignored for not following the 'prop' pattern:\n{prop} -> {len(prop_info)}\n"
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

data = {
    "props": props_json,
    "vertical_zips": vertical_ziplines_json,
    "horizontal_zips": horizontal_ziplines_json,
}

with open("props.json", "w") as f:
    json.dump(data, f)
