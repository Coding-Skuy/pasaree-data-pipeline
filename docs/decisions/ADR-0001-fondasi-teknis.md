# ADR-0001 — Fondasi teknis pasaree-data-pipeline

Status: Diterima | Tanggal: 2026-10-14

## Konteks

pasaree-data-pipeline adalah repo `data-pipeline` divisi Pasaree. Spesifikasi v1.0.0 dibekukan 2026-10-07 di Pasaree-TownHall (`platform/versions/v1.0.0/`). Dokumen TECHSTACK dan BLAST-RADIUS v1.0.0 di repo ini masih ringkas, sehingga fondasi teknis dikunci di ADR ini sebelum coding kickoff.

## Keputusan

1. Kontrak event berversi dengan amplop idempoten (`event_id`, `schema_version`, `source: pasaree`, `occurred_at`/`received_at`, `batch_id`).
2. Registry event Titeny terkunci 11 `event_type`; Pasaree memproduksi `transaksi.dibuat`, `lapak.status_berubah`, `logistik.biaya_diperbarui`, `vendor.status_berubah`; penambahan jenis baru butuh bump versi + 30 hari dual-read.
3. Titeny read-only ke DB sumber; pipeline tidak menulis balik ke DB `pasaree`.
4. Uang selalu integer IDR; komisi dibulatkan ke bawah (`floor()`) per baris item. Komisi 8% (paket-hampers 10%, lapak baru 5% selama 30 hari) dipotong dari payout lapak, BUKAN dari pembeli; biaya layanan Rp2.000 per checkout masuk operasional Pasaree; ongkir 100% ke kas trip Lumbung; escrow via kasir, payout dieksekusi Lumbung T+1 hari kerja; uang integer IDR, komisi `floor()`.
5. Katalog jujur: harga tampil = harga bayar sebelum ongkir; komisi tertera terpisah dan tidak dibebankan ke pembeli; dilarang mark-up tersembunyi.
6. Fulfillment fisik wajib via trip Lumbung; Pasaree tidak membangun armada, gudang, atau kasir kas sendiri.
7. Rekonsiliasi Pasaree-Lumbung harian; selisih >Rp1.000 atau status menggantung >2x24 jam menjadi tiket prioritas tinggi.
8. Perubahan tarif umum diumumkan 14 hari sebelum berlaku.

## Konsekuensi

- Semua pekerjaan repo ini mengikuti `AGENTS.md`; menyimpang dari keputusan di atas butuh ADR baru bernomor berikutnya.
- Dokumen TownHall tetap sumber requirement; repo ini tidak menyalin requirement, hanya menautkannya.
- Pelanggaran batas (DB lintas divisi, komisi ke pembeli, fulfillment di luar trip Lumbung) dianggap cacat dan diblokir di review.
