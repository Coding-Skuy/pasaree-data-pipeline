"""Validasi event katalog Pasaree."""
JENIS_WAJIB = {"produk.dibuat", "harga.berubah", "stok.berubah", "tayang.berubah"}


def validasi_event(e: dict) -> list:
    """Kembalikan daftar kesalahan. Kosong berarti valid."""
    galat = []
    if e.get("jenis") not in JENIS_WAJIB:
        galat.append("jenis tidak dikenal")
    if not e.get("id"):
        galat.append("id wajib ada")
    if not e.get("waktu"):
        galat.append("waktu ISO-8601 UTC wajib ada")
    if "harga_idr" in e and (not isinstance(e["harga_idr"], int) or e["harga_idr"] < 0):
        galat.append("harga_idr harus integer nol atau lebih")
    return galat


if __name__ == "__main__":
    contoh = {"jenis": "harga.berubah", "id": "01J0000000000000000000001", "waktu": "2026-01-01T00:00:00Z", "harga_idr": 25000}
    print(validasi_event(contoh))
