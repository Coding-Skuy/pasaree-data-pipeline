# pasaree-data-pipeline

Pipa data event katalog Marketplace Pasaree. Divisi Pasaree (Marketplace), org Coding-Skuy. Template Opsi A.

Rujukan utama: [Pasaree-TownHall](https://github.com/Coding-Skuy/Pasaree-TownHall) — baca `katalog/10-model-data.md` dan `metrik/10-lapak-aktif.md`.

## Peran

- Menyalurkan event katalog: produk dibuat, harga berubah, stok berubah, status tayang berubah.
- Sumber ke metrik lapak aktif dan ke pencarian katalog.
- Tidak membawa data armada, gudang, atau kas. Itu ranah Lumbung.

## Struktur

```
config/pipeline.yaml          Sumber, antrean, tujuan
src/pipeline/event_katalog.py Validasi dan teruskan event
docs/SKEMA_EVENT.md           Skema event dan contoh
```

## Mulai Cepat

1. Pasang Python 3.12.
2. Jalankan `pip install -e .`.
3. Jalankan `python -m pipeline.event_katalog` untuk validasi contoh.
