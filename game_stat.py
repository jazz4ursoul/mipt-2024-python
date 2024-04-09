class GameStat:
    def __init__(self):
        self.last_errors_cnt = 0
        self.last_symb_cnt = 0
        self.last_time = 0

        self.sum_errors_cnt = 0
        self.sum_symb_cnt = 0
        self.sum_time = 0

        self.run_cnt = 0

    def upd(self, errors: int, symb_cnt: int, time: float):
        self.run_cnt += 1

        self.last_time = time
        self.last_symb_cnt = symb_cnt
        self.last_errors_cnt = errors

        self.sum_time += time
        self.sum_symb_cnt += symb_cnt
        self.sum_errors_cnt += errors

    def get_last_errors(self) -> int:
        return self.last_errors_cnt

    def get_last_speed(self) -> int:
        return (self.last_symb_cnt // self.last_time) * 60

    def get_avg_errors(self) -> int:
        return self.last_errors_cnt // self.run_cnt

    def get_avg_speed(self) -> int:
        return (self.sum_symb_cnt // self.sum_time) * 60
