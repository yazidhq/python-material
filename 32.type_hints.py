# Type hints untuk fungsi

# fungsi standar
def fungsi(parameter):  # parameter:any
    print(parameter**2)


fungsi(3)
# error karna parameternya bisa apa saja dimasukkan
# fungsi("Yazid Dhiaulhaq Ismail")


# penggunaan type hint (untuk sharing program)
# parameter:int -> ekspresinya atau returnnya int juga
def sepuluh_pangkat(argument: int) -> int:
    output = 10**argument
    return output


print(sepuluh_pangkat(2))  # argument:int->return:int
