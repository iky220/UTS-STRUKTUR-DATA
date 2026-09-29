"""Program sederhana untuk mengelola playlist lagu."""


playlist = [
    {
        "judul": "Hati-Hati di Jalan",
        "artis": "Tulus",
        "genre": "Pop",
        "durasi": "4:02",
    },
    {
        "judul": "Sampai Jadi Debu",
        "artis": "Banda Neira",
        "genre": "Indie",
        "durasi": "3:48",
    },
]


def tampilkan_lagu():
    """Menampilkan semua lagu di dalam playlist."""
    if not playlist:
        print("Playlist masih kosong.")
        return

    print("\nDAFTAR LAGU")
    for nomor, lagu in enumerate(playlist, start=1):
        print(f"{nomor}. {lagu['judul']} - {lagu['artis']}")


def tambah_lagu():
    """Membaca data lagu dari pengguna dan menambahkannya ke playlist."""
    print("\nTAMBAH LAGU")
    judul = input("Judul: ").strip()
    artis = input("Artis: ").strip()
    genre = input("Genre: ").strip()
    durasi = input("Durasi (contoh 3:45): ").strip()

    if not judul or not artis or not genre or not durasi:
        print("Semua data lagu harus diisi.")
        return

    playlist.append(
        {
            "judul": judul,
            "artis": artis,
            "genre": genre,
            "durasi": durasi,
        }
    )
    print("Lagu berhasil ditambahkan.")


def hapus_lagu():
    """Menghapus lagu berdasarkan nomor pada daftar playlist."""
    tampilkan_lagu()
    if not playlist:
        return

    pilihan = input("Masukkan nomor lagu yang ingin dihapus: ").strip()
    if not pilihan.isdigit():
        print("Nomor lagu harus berupa angka.")
        return

    nomor = int(pilihan)
    if nomor < 1 or nomor > len(playlist):
        print("Nomor lagu tidak ditemukan.")
        return

    lagu = playlist.pop(nomor - 1)
    print(f"Lagu '{lagu['judul']}' berhasil dihapus.")


def cari_lagu():
    """Mencari lagu berdasarkan judul atau artis."""
    kata_kunci = input("Masukkan judul atau artis yang dicari: ").strip().lower()
    hasil = [
        lagu
        for lagu in playlist
        if kata_kunci in lagu["judul"].lower()
        or kata_kunci in lagu["artis"].lower()
    ]

    if not hasil:
        print("Lagu tidak ditemukan.")
        return

    print("\nHASIL PENCARIAN")
    for lagu in hasil:
        print(f"- {lagu['judul']} - {lagu['artis']}")


def detail_lagu():
    """Menampilkan detail lagu berdasarkan nomor pada daftar playlist."""
    tampilkan_lagu()
    if not playlist:
        return

    pilihan = input("Masukkan nomor lagu untuk melihat detail: ").strip()
    if not pilihan.isdigit():
        print("Nomor lagu harus berupa angka.")
        return

    nomor = int(pilihan)
    if nomor < 1 or nomor > len(playlist):
        print("Nomor lagu tidak ditemukan.")
        return

    lagu = playlist[nomor - 1]
    print("\nDETAIL LAGU")
    print(f"Judul : {lagu['judul']}")
    print(f"Artis : {lagu['artis']}")
    print(f"Genre : {lagu['genre']}")
    print(f"Durasi: {lagu['durasi']}")


def urutkan_lagu():
    """Menampilkan lagu yang diurutkan berdasarkan judul."""
    if not playlist:
        print("Playlist masih kosong.")
        return

    lagu_terurut = sorted(playlist, key=lambda lagu: lagu["judul"].lower())
    print("\nDAFTAR LAGU BERDASARKAN JUDUL")
    for nomor, lagu in enumerate(lagu_terurut, start=1):
        print(f"{nomor}. {lagu['judul']} - {lagu['artis']}")


def tampilkan_menu():
    """Menampilkan pilihan menu utama."""
    print("\n===== SISTEM PLAYLIST LAGU =====")
    print("1. Tampilkan Lagu")
    print("2. Tambah Lagu")
    print("3. Hapus Lagu")
    print("4. Cari Lagu")
    print("5. Detail Lagu")
    print("6. Urutkan Lagu Berdasarkan Judul")
    print("7. Keluar")


def jalankan_program():
    """Menjalankan menu playlist sampai pengguna memilih keluar."""
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-7): ").strip()

        if pilihan == "1":
            tampilkan_lagu()
        elif pilihan == "2":
            tambah_lagu()
        elif pilihan == "3":
            hapus_lagu()
        elif pilihan == "4":
            cari_lagu()
        elif pilihan == "5":
            detail_lagu()
        elif pilihan == "6":
            urutkan_lagu()
        elif pilihan == "7":
            print("Terima kasih telah menggunakan playlist.")
            break
        else:
            print("Pilihan menu tidak valid.")


if __name__ == "__main__":
    jalankan_program()