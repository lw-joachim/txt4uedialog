"""
Impl of external interface
"""

import csv
import logging
import json

logger = logging.getLogger(__name__)

def get_node_dict(idCounter, xCord, yCord, rowDict):
    return  {
                "id": idCounter,
                "isPlayer": rowDict["is_player"],
                "text": rowDict["text"],
                "links": [],
                "coordinates": {
                    "x": xCord,
                    "y": yCord
                },
                "properties": {
                    "_ClassName": "DialogueNodeProperties_C",
                    "camera": "NewEnumerator0",
                    "uILabel": rowDict["ui_label"],
                    "intent": rowDict["intent"],
                    "intentEscalation": rowDict["intent_escalation"],
                    "audioId" : rowDict["key"]
                },
                "Events": [],
                "Conditions": [],
                "sound": "None",
                "dialogueWave": "None",
                "bubbleComment": "",
                "bDrawBubbleComment": True
            }


def convert_to_json(csv_input_path, json_output_path):
    nodesList = []
    logger.info(f"Reading file {csv_input_path}")
    with open(csv_input_path, newline=None) as csvfile:
        reader = csv.DictReader(csvfile)
        currXCord, currYCord = 0, 0
        for i, row in enumerate(reader):
            for k in list(row.keys()):
                if k.startswith("\ufeff"):
                    row[k.replace("\ufeff", "")] = row[k]
                    row.pop(k)
            if "key" not in row or row["key"] == "":
                continue
            if i % 5 == 0:
                currXCord = 0
                currYCord += 100
            nodesList.append(get_node_dict(i, currXCord, currYCord, row))
            currXCord += 300
    
    logger.info(f"Parsed {len(nodesList)} rows")
    jsonDict = {"Nodes" : nodesList}
    
    with open(json_output_path, "w") as fp:
        json.dump(jsonDict, fp, indent=2)
        
    logger.info(f"Resulting dialog json written to : {json_output_path}")
    
