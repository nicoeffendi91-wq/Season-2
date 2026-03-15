def sorting_array(data, mode):
    if mode == "ascending":
        return sorted(data)
    elif mode == "descending":
        return sorted(data, reverse=True)

input_str = input("Masukkan angka dipisahkan spasi: ")
array = [int(x) for x in input_str.split()]
mode = input("Pilih urutan (ascending/descending): ")
hasil = sorting_array(array, mode)

print("Hasil:", hasil)
