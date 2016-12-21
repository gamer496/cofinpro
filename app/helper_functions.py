import os
import csv
from models import Game

def get_popular(user_obj, query_obj):
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    k = os.path.join(curr_dir, "engine")
    f = os.path.join(k, "test_new.csv")
    f = open(f, "wb")
    writer = csv.writer(f, delimiter = " ")
    writer.writerow([user_obj.id, "abcat0701002", query_obj.content, str(query_obj.queried_on), str(query_obj.executed_on)])
    f.close()
    l = os.path.join(k, "train6.py")
    command = "python " + l + " " + os.path.join(k, "train.csv") + " " + os.path.join(k, "test_new.csv") + " " + os.path.join(k, "prediction_new.csv") + " " + os.path.join(k, "sku_name_prepared.tsv")
    # print "*"*80
    # print command
    # print "*"*80
    os.system(command)
    f1 = open(os.path.join(k, "prediction_new.csv"))
    reader = csv.reader(f1, delimiter = " ")
    l = reader.next()
    data = []
    for k in l:
        k = int(k)
        h = Game.query.get(k)
        if h:
            data.append(h.name)
    return data
