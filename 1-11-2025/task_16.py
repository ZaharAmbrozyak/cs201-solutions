def task_16():

    def calc(operation: str, *args, precision: int = 2, **options) -> float:
        match operation:
            case 'add':
                output = 0
                for arg in args:
                    output += arg
            case 'mul':
                output = 1
                for arg in args:
                    output *= arg
            case 'avg':
                output = 0
                for arg in args:
                    output += arg
                output /= len(args)
            case _:
                raise ValueError('Unknown operation')
        match options:
            case {'negative': True}:
                return round(output*(-1), precision)
            case {'negative': False} | {}:
                return round(output, precision)
            case _:
                raise ValueError('Unknown operation')
    return calc

calculate = task_16()

print(calculate('add', 2, 3, 5, prec=1))
print(calculate('mul', 2, 3, negative=True))
print(calculate('avg', 4, 8, 10, precision=3))
