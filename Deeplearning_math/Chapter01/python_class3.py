class grader:
    def __init__(self, score_list):
        self.score_list = score_list
        
        self._grade_list = None
        self._cutoff_list = None
        
        self._init_grader()
        
    def _init_grader(self):
        self._grade_list = ['A', 'B', 'C', 'F']
        self._cutoff_list = [100, 90, 80, 70, 0]
        
    def score2grade(self):
        return_grade_list = []
        for score_idx, score in enumerate(self.score_list):
            if score >= self._cutoff_list[1] and score < self._cutoff_list[0]:
                return_grade_list.append(self._grade_list[0])
            elif score >= self._cutoff_list[2] and score < self._cutoff_list[1]:
                return_grade_list.append(self._grade_list[1])
            elif score >= self._cutoff_list[3] and score < self._cutoff_list[2]:
                return_grade_list.append(self._grade_list[2])
            elif score >= self._cutoff_list[4] and score < self._cutoff_list[3]:
                return_grade_list.append(self._grade_list[3])
            else:
                class scoreError(Exception):
                    pass
                raise scoreError("Invalid Score Detected!")
                
        print(return_grade_list)
                
score_list = [50, 70, 40, 90, 95, 20, 15, 85, 77]

tmp = grader(score_list)

print(tmp._grade_list)
print(tmp._cutoff_list)
print(score_list)
tmp.score2grade()