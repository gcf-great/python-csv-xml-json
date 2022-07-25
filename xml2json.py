import xmltodict
import json
import os
import csv


def xml_to_json(xml_path):
    file_list = os.listdir(xml_path)
    read_list = []
    for i in file_list:
        a, b = os.path.splitext(i)
        if b == ".gold":
            read_list.append(i)
    print(read_list)

    for item in read_list:
        with open(xml_path + '/' + item, 'r', encoding='utf8') as f:
            xml = f.read()

        convertJson = xmltodict.parse(xml, encoding='utf-8')
        jsonStr = json.dumps(convertJson, indent=1)

        new_name = item.rsplit('.xml.gold')[0] + '.json'
        with open(xml_path + '\\' + new_name, 'w+', encoding='utf-8') as f:
            f.write(jsonStr)
            print('{} has finished'.format(new_name))


def csv_to_json(csv_path):
    file_list = os.listdir(csv_path)
    read_list = []
    for i in file_list:
        a, b = os.path.splitext(i)
        if b == ".csv":
            read_list.append(i)
    print(read_list)

    data = {}
    for item in read_list:
        with open(csv_path+'/'+item, 'r', encoding='utf-8-sig') as csvf:
            csvReader = csv.DictReader(csvf)
            for rows in csvReader:
                if 'index' in rows:
                    key = rows['index']
                    data[key] = rows
                else:
                    key = rows['id']
                    data[key] = rows

        jsonStr = json.dumps(data, indent=1)

        new_name = item.rsplit('.csv')[0] + '.json'
        with open(csv_path + '\\' + new_name, 'w+', encoding='utf-8') as f:
            f.write(jsonStr)
            print('{} has finished'.format(new_name))


if __name__ == '__main__':
    # paths = ["./SemEval-2014-4/", "./SemEval-2015-12/", "./SemEval-2016-5/"]
    # class_type = ["Laptop", "Rest"]
    # for i in class_type:
    #     xml_to_json("./SemEval-2014-4/" + i)
    csv_to_json("./ASAP")
    pass
