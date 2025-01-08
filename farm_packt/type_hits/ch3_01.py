from typing import Union

def print_name_x_times(name:str, times:int) -> None:
    for _ in range(times):
        print(name)


# print_name_x_times(2, 'hola')

text:str = 'John'

## if you need multiple type you can use Union
x: Union[str, int]
## you can do this too with pip | character
x: str | int
