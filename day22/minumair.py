#python dasar

import time

def pengingat_minum_air():
    # Menentukan jam kerja dari jam 9 pagi sampai jam 5 sore (8 jam)
    jumlah_pengingat = 8
    interval = 3600  # Interval 1 jam dalam detik

    print("Program pengingat minum air dimulai...")
    for i in range(jumlah_pengingat):
        print(f"Pengingat {i + 1}: Waktunya minum air!")
        time.sleep(interval)  # Tunggu selama 1 jam (3600 detik)

    print("Program pengingat minum air selesai.")

if __name__ == "__main__":
    pengingat_minum_air()
