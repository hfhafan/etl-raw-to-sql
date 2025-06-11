# Panduan Penggunaan ETL Raw Data to SQL

## Quick Start

### 1. Instalasi

```bash
# Clone repository
git clone https://github.com/hfhafan/etl-raw-to-sql.git
cd etl-raw-to-sql

# Install dependencies
pip install -r requirements.txt

# Konfigurasi database (opsional)
cp config/settings.yaml.example config/settings.yaml
# Edit config/settings.yaml sesuai kebutuhan
```

### 2. Konfigurasi Database

Edit file `config/settings.yaml`:

```yaml
database:
  type: "mssql"
  host: "your-server"
  port: 1433
  name: "your-database"
  timeout: 30
```

**Note**: Untuk keamanan, kredensial database dikonfigurasi terpisah melalui environment variables atau dialog input.

### 3. Menjalankan Aplikasi

```bash
python src/main.py
```

## Interface Pengguna

### Login Screen
1. Masukkan username dan password
2. Sistem akan memvalidasi kredensial
3. Setelah login berhasil, aplikasi utama akan terbuka

### Main Interface

#### Tab 1: File Processing
- **Select Files**: Pilih file data (CSV/Excel)
- **Network Type**: Pilih jenis jaringan (2G/4G/5G)
- **Process**: Mulai pemrosesan data
- **Progress**: Monitor progress real-time

#### Tab 2: Database Management
- **Connection**: Test koneksi database
- **Upload**: Upload data ke database
- **History**: Lihat riwayat upload

#### Tab 3: Export/Reports
- **Export Data**: Export data dari database
- **Generate Reports**: Buat laporan
- **Statistics**: Lihat statistik pemrosesan

## Workflow Processing

### 1. Persiapan Data
- Pastikan file data dalam format CSV atau Excel
- Validasi struktur kolom sesuai jenis jaringan
- Backup data original (opsional)

### 2. Processing Steps
```
Input Files → Validation → Transformation → Quality Check → Database Upload
```

#### Data 2G
Required columns:
- `site_id`: ID site
- `cell_id`: ID cell
- `date`: Tanggal data
- `kpi_value`: Nilai KPI

#### Data 4G
Required columns:
- `site_id`: ID site  
- `cell_id`: ID cell
- `date`: Tanggal data
- `kpi_value`: Nilai KPI
- `technology`: Teknologi (4G)

#### Data 5G
Required columns:
- `site_id`: ID site
- `cell_id`: ID cell  
- `date`: Tanggal data
- `kpi_value`: Nilai KPI
- `technology`: Teknologi (5G)
- `band`: Frequency band

### 3. Post-Processing
- Review upload results
- Check error logs jika ada
- Generate reports

## Error Handling

### Common Errors

#### File Format Error
```
Error: Unsupported file format
Solution: Gunakan file CSV atau Excel (.xlsx/.xls)
```

#### Missing Columns
```
Error: Missing required columns
Solution: Pastikan semua kolom wajib tersedia
```

#### Database Connection Error
```
Error: Database connection failed
Solution: Periksa konfigurasi database dan koneksi
```

#### Authentication Error
```
Error: Authentication failed
Solution: Periksa username/password atau hubungi admin
```

### Log Files
- Location: `logs/app_YYYYMMDD.log`
- Level: DEBUG, INFO, WARNING, ERROR, CRITICAL
- Auto rotation: 10MB per file, 5 backup files

## Advanced Configuration

### Environment Variables
```bash
# Database credentials
export DB_USERNAME="your_username"
export DB_PASSWORD="your_password"

# Application settings
export APP_DEBUG="false"
export LOG_LEVEL="INFO"
```

### Custom Settings
Edit `config/settings.yaml` untuk customisasi:

```yaml
processing:
  batch_size: 1000        # Records per batch
  max_workers: 4          # Parallel workers
  chunk_size: 10000       # Memory chunk size
  timeout: 300            # Processing timeout

networks:
  supported: ["2G", "4G", "5G"]
  default_tables:
    "2G": "custom_2g_table"
    "4G": "custom_4g_table"
    "5G": "custom_5g_table"
```

## Tips & Best Practices

### Performance
- Gunakan file CSV untuk file besar (>100MB)
- Set batch_size sesuai kapasitas memory
- Monitor resource usage saat processing

### Data Quality
- Validasi data sebelum upload
- Backup data original
- Review error logs regularly

### Security
- Gunakan strong password
- Jangan hardcode credentials
- Enable audit logging

### Maintenance
- Clean up log files regularly
- Monitor disk space
- Update dependencies berkala

## Troubleshooting

### Performance Issues
1. Reduce batch_size di config
2. Close aplikasi lain yang memory-intensive
3. Check disk space availability

### Database Issues
1. Test koneksi database terlebih dahulu
2. Periksa firewall dan network access
3. Validate database permissions

### File Processing Issues
1. Check file format dan encoding
2. Validate column names dan data types
3. Ensure file tidak sedang dibuka aplikasi lain

## Support

Untuk bantuan lebih lanjut:
- Buat issue di GitHub repository
- Check dokumentasi di folder `docs/`
- Review log files untuk detail error 