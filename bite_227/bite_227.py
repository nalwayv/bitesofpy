from pathlib import Path
import csv
import json
from json.decoder import JSONDecodeError

EXCEPTION = 'exception caught'
TMP = Path('bite_227/tmp')


def open_json(json_file: str) -> dict:
    """open_json
    
    Parameters
    ----------
    json_file : str
        json file path
    
    Returns
    -------
    dict
        json data decoded
    """
    data = None

    with Path(json_file).open() as j_file:
        data = json.load(j_file)

    return data


def mount_data(json_data: dict) -> list:
    """mount_data
    
    Parameters
    ----------
    json_data : dict
        mount data from json data
    
    Returns
    -------
    list
        list of dicts
    """
    if 'mounts' in json_data:
        mount_data = json_data['mounts']
        if 'collected' in mount_data:
            return mount_data['collected']

    return None


def write_csv(mount_data: list, file_name: str) -> None:
    """write_csv
    
    Parameters
    ----------
    mount_data : list
        list of mount data from json
    file_name : str
        file to save to
    """
    with Path(file_name).open('w', newline='') as csv_file:

        fieldnames = [
            'creatureId', 'icon', 'isAquatic', 'isFlying', 'isGround',
            'isJumping', 'itemId', 'name', 'qualityId', 'spellId'
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for md in mount_data:
            writer.writerow(md)


def convert_to_csv(json_file: str):
    """Read/load the json_file (local file downloaded to /tmp) and
       convert/write it to defined csv_file.
        The data is in mounts > collected

       Catch bad JSON (JSONDecodeError) file content, in that case print the defined
       EXCEPTION string ('exception caught') to stdout reraising the exception.
       This is to make sure you actually caught this exception.

       Example csv output:
       creatureId,icon,isAquatic,isFlying,isGround,isJumping,itemId,name,qualityId,spellId
       32158,ability_mount_drake_blue,False,True,True,False,44178,Albino Drake,4,60025
       63502,ability_mount_hordescorpionamber,True,...
       ...
    """
    csv_file = TMP / json_file.name.replace('.json', '.csv')

    # you code
    try:
        data = open_json(json_file)
        md = mount_data(data)
        write_csv(md, csv_file)
    except JSONDecodeError as err:
        print(EXCEPTION)
        raise err


if __name__ == "__main__":
    for f in list(TMP.absolute().glob('*json')):
        convert_to_csv(f)