def level_up(experience: int, threshold: int, reward: int) -> bool:
    return (experience + reward) - threshold >= 0


def motor_time(n: int) -> int:
    h = n // 60
    m = n - (h * 60)

    result = 0
    result += sum(int(x) for x in str(h))
    result += sum(int(x) for x in str(m))

    return result


def time_converter(time_str: str) -> str:
    hours, minutes = map(int, time_str.split(':'))
    period = "a.m." if hours < 12 else "p.m."
    hours = 12 if hours == 0 else hours if hours <= 12 else hours - 12
    return f"{hours}:{minutes:02d} {period}"
