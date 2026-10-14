# Arsitektur AI-dev pasaree-data-pipeline

Dokumen tambahan untuk `versions/v1.0.0/docs/40-TECHSTACK.md` dan `60-BLAST-RADIUS.md` (kedua file itu beku v1.0.0 dan hanya berisi ringkasan; jangan ditimpa). Rujukan versi: [Pasaree-TownHall v1.0.0](https://github.com/Coding-Skuy/Pasaree-TownHall/blob/main/platform/versions/v1.0.0/CHANGELOG.md).

## Matriks stack dan fitur

| Aspek | Terkunci | Catatan |
|---|---|---|
| Bahasa | Python >=3.12 + `pyyaml` | `pyproject.toml`, `config/pipeline.yaml` |
| Kontrak event | berversi (`schema_version`) | amplop mengikuti KONTEKS §3 |
| Idempotensi | `event_id` (`evt_YYYYMMDD_NNNNNN`), header `X-Idempotency-Key` | duplikat diabaikan |
| Pengiriman | `POST /api/v1/event/masuk`, retry 3x (5/30/300 dtk) lalu DLQ | |
| Jadwal & konsumen | tercatat di `config/pipeline.yaml` | konsumen: pencarian-katalog, metrik-lapak-aktif, Titeny |

Larangan: menambah `event_type` di luar registry 11 event Titeny tanpa bump versi + 30 hari dual-read; menulis ke DB sumber (Titeny read-only).

| Event lokal | Registry Titeny | Konsumen |
|---|---|---|
| `produk.dibuat`, `tayang.berubah` | `lapak.status_berubah` (bila relevan) | pencarian-katalog, metrik-lapak-aktif |
| `harga.berubah`, `stok.berubah` | internal Pasaree; dipetakan di PSR-DATA-002 | pencarian-katalog |
| transaksi selesai | `transaksi.dibuat` | Titeny |
| ongkir/biaya trip berubah | `logistik.biaya_diperbarui` | Titeny |

## Blast radius

Batas context repo (townhall-roadmap §2: komisi 8% transparan, escrow T+1; katalog jujur; fulfillment wajib via trip Lumbung).

Boleh disentuh:

- Validasi, transformasi, dan penerusan event katalog/transaksi Pasaree; konfigurasi jadwal.
- Menghitung metrik lapak aktif dari event + snapshot stok harian.

Dilarang:

- Membawa data armada, gudang, atau kas (ranah Lumbung).
- Mengubah registry Titeny atau menulis ke DB sumber.
- Event tanpa amplop idempoten.

Kontrak dikonsumsi:

- Event dan snapshot dari `pasaree-backend-service`.

Kontrak diproduksi:

- Event ber-amplop ke Titeny (`POST /api/v1/event/masuk`), indeks pencarian, metrik lapak aktif.

Catatan: Pasaree tidak mengonsumsi modul `:shared:pantry-resep` (milik Pawonee). Failure utama: kontrak berubah tanpa update SRS, test tidak mengikuti acceptance criteria, rollback tidak siap. Rollback: revert commit repo ini dan kembali ke kontrak Pasaree-TownHall v1.0.0.
