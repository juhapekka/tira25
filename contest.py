class Contest:
    def __init__(self, names, task_count):
        self.dada = {}
        for name in names:
            self.dada[name] = {
                "scores": [0] * task_count,
                "total": 0,
                "yrityksii": 0
            }

        self.task_count = task_count
        self.submission_cc = 0

    def add_submission(self, name, task, score):
        self.submission_cc += 1

        jannu = self.dada[name]
        ed_score = jannu["scores"][task - 1]
        # uudet pistet korkeammat
        if score > ed_score:
            jannu["scores"][task - 1] = score

            vanha_total = jannu["total"]
            uus_total = vanha_total - ed_score + score
            jannu["total"] = uus_total

            # kierros talteen
            if uus_total != vanha_total:
                jannu["yrityksii"] = self.submission_cc

    def create_scoreboard(self):
        itemit = list(self.dada.items())

        
        def sort_key(item):
            name, info = item
            t = info["total"]
            if t == 0:
                return (0, name)
            else:
                return (-t, info["yrityksii"])

        itemit.sort(key=sort_key)
        scoreboard = [(name, info["total"]) for name, info in itemit]
        return scoreboard
    
     
if __name__ == "__main__":
    names = ["anna", "pekka", "kalle", "tiina", "eeva"]
    contest = Contest(names, 3)

    contest.add_submission("tiina", 2, 30)
    contest.add_submission("pekka", 1, 40)
    contest.add_submission("tiina", 1, 20)
    contest.add_submission("pekka", 1, 50)
    contest.add_submission("pekka", 2, 0)
    contest.add_submission("eeva", 3, 100)
    contest.add_submission("anna", 1, 0)
    contest.add_submission("eeva", 3, 80)
    contest.add_submission("tiina", 2, 30)

    scoreboard = contest.create_scoreboard()
    print(scoreboard)
    # [('eeva', 100), ('tiina', 50), ('pekka', 50), ('anna', 0), ('kalle', 0)]