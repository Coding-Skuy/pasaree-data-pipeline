# Skema Event Katalog Pasaree

Jenis: `produk.dibuat`, `harga.berubah`, `stok.berubah`, `tayang.berubah`.

Medan wajib: `id` ULID string, `jenis`, `waktu` ISO-8601 UTC, `lapak_id`, `produk_id`.

Contoh harga berubah:

```json
{
  "id": "01J0000000000000000000001",
  "jenis": "harga.berubah",
  "waktu": "2026-01-01T00:00:00Z",
  "lapak_id": "01J0000000000000000000000",
  "produk_id": "01J0000000000000000000002",
  "harga_idr": 25000
}
```

Uang selalu integer IDR. Paginasi cursor mengikuti kontrak TownHall.
