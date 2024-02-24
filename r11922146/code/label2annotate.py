import json
import argparse

def adjust_json_format(input_json_path, output_json_path):
    with open(input_json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    transformed_data = {}
    for i in range(len(data)):
        transformed_data[data[i]["file_upload"].split("-")[1]] = []
        # print(len(data[i]["annotations"][0]["result"]))
        for j in range(len(data[i]["annotations"][0]["result"])):
            transformed_data[data[i]["file_upload"].split("-")[1]].append({
                "start_frame": data[i]["annotations"][0]["result"][j]["value"]["sequence"][0]["frame"],
                "end_frame": data[i]["annotations"][0]["result"][j]["value"]["sequence"][1]["frame"],
                "action_type": data[i]["annotations"][0]["result"][j]["value"]["labels"][0],
                "down_coordinate": [data[i]["annotations"][0]["result"][j]["value"]["sequence"][0]["x"], data[i]["annotations"][0]["result"][j]["value"]["sequence"][0]["y"]] if data[i]["annotations"][0]["result"][j]["value"]["labels"][0]!="type" else None,
                "up_coordinate": [data[i]["annotations"][0]["result"][j]["value"]["sequence"][1]["x"], data[i]["annotations"][0]["result"][j]["value"]["sequence"][1]["y"]] if data[i]["annotations"][0]["result"][j]["value"]["labels"][0]!="type" else None,
                "type_word": None,
            })
    ## need to change swipe and type_word
    
    with open(output_json_path, 'w', encoding='utf-8') as file:
        json.dump(transformed_data, file, ensure_ascii=False, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Read a JSON file, process it, and write the output to another JSON file.")
    parser.add_argument('input_file', type=str, help="The path to the input JSON file.")
    parser.add_argument('output_file', type=str, help="The path to the output JSON file.")
    args = parser.parse_args()

    adjust_json_format(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
