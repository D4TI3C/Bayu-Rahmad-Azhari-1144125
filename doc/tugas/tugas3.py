print('Puzzle : Petani, Harimau, Ayam, Gabah')
print('1 = Petani menyebrang')
print('2 = Hairmau menyebrang')
print('3 = Ayam menyebrang')
print('4 = Gabah menyebrang')
print('5 = Petani balik')
print('6 = Hairmau balik')
print('7 = Ayam balik')
print('8 = Gabah balik')
print('\n[p, h, a, g]')
a = raw_input('Mulailah, Pilih ? : ')
if a == '1,3':
        print('\n[h, g] --> [p, a]')
        b = raw_input('Lanjutkan, pilih ? : ')
        if b == '5':
                print('\n[p, h, g] <-- [a]')
                c = raw_input('Lanjutkan, pilih ? : ')
                if c == '1,2':
                        print('\n[g] --> [p, h, a]')
                        d = raw_input('Lanjutkan, pilih ? : ')
                        if d == '5,7':
                                print('\n[p, a, g] <-- [h]')
                                e = raw_input('Lanjutkan, pilih ? : ')
                                if e == '1,4':
                                        print('\n[a] --> [p, h, g]')
                                        f = raw_input('Lanjutkan, pilih ? : ')
                                        if f == '5':
                                                print('\n[p, a] <-- [h, g]')
                                                g = raw_input('Lanjutkan, pilih ? : ')
                                                if g == '1,3':
                                                        print('\n[] --> [p, h, a, g]')
                                                        print('Selamat, Anda berhail')
                                                else:
                                                        print('Maaf, Anda gagal')
                                        else:
                                                print('Maaf, Anda gagal')
                                else:
                                        print('Maaf, Anda gagal')
                        else:
                                print('Maaf, Anda gagal')
                else:
                        print('Maaf, Anda gagal')
        else:
                print('Maaf, Anda gagal')
else:
        print('Maaf, Anda gagal')
