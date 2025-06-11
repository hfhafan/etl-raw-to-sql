# Download & Installation Guide

## 📥 Download Options

### Option 1: Production Application (Recommended)

**[🔗 Download SQL Upload Processing Tool.exe](https://drive.google.com/drive/folders/1WSzitOLnPO3ilwKAl1NwxyQnIO6nEzwf?usp=drive_link)**

- **File Name**: `SQL Upload Processing Tool.exe`
- **File Size**: 164.3 MB
- **Platform**: Windows 10/11
- **Type**: Portable Application (No installation required)

### Option 2: Source Code

**[🔗 GitHub Repository](https://github.com/hfhafan/etl-raw-to-sql)**

- **Type**: Sample/Demo source code
- **Purpose**: Educational & development reference
- **Language**: Python 3.8+

## 🛠️ Installation Instructions

### Production Application

1. **Download File**
   - Klik link [Google Drive download](https://drive.google.com/drive/folders/1WSzitOLnPO3ilwKAl1NwxyQnIO6nEzwf?usp=drive_link)
   - Download file `SQL Upload Processing Tool.exe`

2. **Extract & Run**
   ```
   1. Buat folder baru (contoh: C:\ETL_Tool\)
   2. Copy file .exe ke folder tersebut
   3. Double-click untuk menjalankan aplikasi
   ```

3. **First Run Setup**
   - Aplikasi akan membuat folder konfigurasi otomatis
   - Login dengan kredensial yang diberikan
   - Konfigurasi database connection

### Source Code Setup

1. **Prerequisites**
   ```bash
   - Python 3.8 atau lebih tinggi
   - pip package manager
   - Git (untuk clone repository)
   ```

2. **Clone Repository**
   ```bash
   git clone https://github.com/hfhafan/etl-raw-to-sql.git
   cd etl-raw-to-sql
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Application**
   ```bash
   python src/main.py
   ```

## 📋 System Requirements

### Minimum Requirements
- **OS**: Windows 10 (64-bit)
- **RAM**: 4 GB
- **Storage**: 2 GB free space
- **Network**: Internet connection untuk database access

### Recommended Requirements
- **OS**: Windows 11 (64-bit)
- **RAM**: 8 GB atau lebih
- **Storage**: 5 GB free space
- **CPU**: Multi-core processor
- **Network**: Stable broadband connection

## 🔧 Configuration

### Database Setup
1. Pastikan SQL Server accessible
2. Buat database untuk aplikasi
3. Konfigurasi connection string dalam aplikasi

### File Permissions
- Aplikasi memerlukan read/write access ke folder instalasi
- Pastikan antivirus tidak memblokir aplikasi

## 🚨 Troubleshooting

### Common Issues

#### "Windows protected your PC" Error
```
Solution:
1. Klik "More info"
2. Klik "Run anyway"
3. Atau add file ke Windows Defender exceptions
```

#### Database Connection Error
```
Solution:
1. Verify SQL Server running
2. Check network connectivity
3. Validate connection string
4. Ensure firewall allows connection
```

#### Memory Error
```
Solution:
1. Close other applications
2. Increase virtual memory
3. Process files in smaller batches
```

## 📞 Support

Jika mengalami masalah:
1. **Check dokumentasi** di folder `docs/`
2. **Review log files** untuk error details
3. **Create issue** di [GitHub repository](https://github.com/hfhafan/etl-raw-to-sql/issues)
4. **Contact support** melalui email

## 🔄 Updates

### Production Updates
- Check Google Drive folder untuk versi terbaru
- Backup data sebelum update
- Replace executable dengan versi baru

### Source Code Updates
```bash
git pull origin master
pip install -r requirements.txt
```

## 📊 File Structure After Installation

```
ETL_Tool/
├── SQL Upload Processing Tool.exe
├── config/                     # Auto-generated
│   ├── settings.yaml
│   └── database.yaml
├── logs/                       # Auto-generated
│   └── app_YYYYMMDD.log
├── temp/                       # Auto-generated
└── data/                       # User data
    ├── input/
    └── output/
```

## ⚠️ Important Notes

1. **Backup Data**: Selalu backup data penting sebelum processing
2. **Antivirus**: Aplikasi mungkin dideteksi sebagai false positive
3. **Permissions**: Jalankan sebagai administrator jika diperlukan
4. **Network**: Pastikan koneksi stabil selama processing
5. **Resources**: Monitor penggunaan memory dan CPU

---

**Ready to start?** Download aplikasi sekarang: [Google Drive Link](https://drive.google.com/drive/folders/1WSzitOLnPO3ilwKAl1NwxyQnIO6nEzwf?usp=drive_link) 