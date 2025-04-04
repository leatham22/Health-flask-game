import json
from datetime import datetime


class SaveHighScore:
    def __init__(self, file, player_instance):
        self.file = file
        self.score = {"Player": player_instance.name, "Score": player_instance._turn_counter, "time": str(datetime.now().strftime("%d-%m-%Y"))}

    def __str__(self):
        scores = []
        for place, entry in enumerate(self.data, 1):
            scores.append("{}. {}  |  {} turns | date: {}".format(place, entry["Player"], entry["Score"], entry["time"]))
        scores_string = "\n".join(scores)
        return "Let\'s see where you rank:\n" + scores_string

    def __enter__(self):
        with open(self.file, "r") as read_file:
            self.data = json.load(read_file)
        self.data.append(self.score)
        self.data = sorted(self.data, key=lambda x: x["Score"])[:20]
        return self
    
    def __exit__(self, *exc):
        with open(self.file, "w") as write_file:
            json.dump(self.data, write_file, indent=4)