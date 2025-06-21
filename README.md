# ETL Raw Data to SQL Database

Sistem ETL (Extract, Transform, Load) untuk memproses data raw jaringan telekomunikasi dan meng-upload ke database SQL dengan antarmuka GUI yang user-friendly.

## 📥 Download

### Executable Application
Untuk mendownload aplikasi yang sudah dikompilasi dalam bentuk executable (.exe):

**[🔗 Download SQL Upload Processing Tool.exe](bit.ly/3HAZAyC)**

- **File Size**: ~164 MB
- **Format**: Windows Executable (.exe)
- **Requirements**: Windows 10 atau lebih tinggi
- **No Installation Required**: Portable application

### Source Code
Repository ini berisi sample/demo code yang menunjukkan konsep dan arsitektur sistem:

**[🔗 GitHub Repository](https://github.com/hfhafan/etl-raw-to-sql)**

## 🚀 Fitur Utama

### 1. Data Processing
- **Multi-Network Support**: Mendukung pemrosesan data 2G, 4G, dan 5G
- **Batch Processing**: Pemrosesan data dalam batch dengan parallel processing
- **Data Validation**: Validasi otomatis struktur dan format data
- **Error Handling**: Penanganan error komprehensif dengan logging detail

### 2. Database Integration
- **SQL Server Connection**: Koneksi ke database SQL Server dengan pooling
- **Automated Upload**: Upload otomatis hasil pemrosesan ke database
- **Transaction Management**: Manajemen transaksi untuk data integrity
- **Rollback Capability**: Kemampuan rollback jika terjadi error

### 3. User Interface
- **Modern GUI**: Antarmuka grafis dengan DearPyGUI
- **Real-time Monitoring**: Monitor real-time proses dan progress
- **Multi-tab Interface**: Interface multi-tab untuk berbagai fungsi
- **Interactive Dashboard**: Dashboard interaktif untuk monitoring

### 4. Security & Authentication
- **User Authentication**: Sistem autentikasi pengguna yang aman
- **Role-based Access**: Akses berbasis peran pengguna
- **Session Management**: Manajemen sesi pengguna
- **Audit Trail**: Pencatatan aktivitas pengguna

## 🏗️ Arsitektur Sistem

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Raw Data      │    │   ETL Engine    │    │   SQL Database  │
│   Files         │──▶│   Processing    │───▶│   Storage       │
│   (2G/4G/5G)    │    │   & Transform   │    │   & Analytics   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 📁 Struktur Project

```
etl-raw-to-sql/
├── src/                    # Source code utama
│   ├── main.py            # Main application
│   ├── gui/               # GUI components
│   └── processing/        # Data processing modules
├── modules/               # Processing modules
│   ├── network_2g/        # 2G data processing
│   ├── network_4g/        # 4G data processing
│   └── network_5g/        # 5G data processing
├── auth/                  # Authentication system
├── config/                # Configuration files
├── data/                  # Sample data
└── docs/                  # Documentation
```

## 🔧 Teknologi yang Digunakan

- **Python 3.8+**: Bahasa pemrograman utama
- **DearPyGUI**: Framework untuk GUI
- **Pandas**: Data manipulation dan analysis
- **SQLAlchemy**: Database ORM
- **Multiprocessing**: Parallel processing
- **Threading**: Concurrent operations

## 📋 Prerequisites

- Python 3.8 atau lebih tinggi
- SQL Server Database
- Windows OS (untuk executable)
- Memory minimum 4GB RAM
- Storage minimum 2GB untuk temporary files

## 🚀 Quick Start

### Option 1: Download Executable (Recommended)
1. **Download aplikasi** dari [Google Drive link](https://drive.google.com/drive/folders/1WSzitOLnPO3ilwKAl1NwxyQnIO6nEzwf?usp=drive_link)
2. **Extract file** ke folder pilihan Anda
3. **Jalankan** `SQL Upload Processing Tool.exe`
4. **Login** dengan kredensial yang diberikan
5. **Mulai processing** data Anda

### Option 2: Run from Source Code
1. **Clone Repository**
   ```bash
   git clone https://github.com/hfhafan/etl-raw-to-sql.git
   cd etl-raw-to-sql
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Database**
   - Edit file `config/database.yaml`
   - Sesuaikan connection string database

4. **Run Application**
   ```bash
   python src/main.py
   ```

## 📊 Workflow Processing

1. **Data Input**: Load raw data files (CSV, Excel)
2. **Data Validation**: Validasi format dan struktur data
3. **Data Transformation**: Transform sesuai schema database
4. **Quality Check**: Quality assurance data
5. **Database Upload**: Upload ke SQL Server
6. **Monitoring**: Monitor status dan generate reports

## 🔐 Security Features

- User authentication dengan secure credential storage
- Role-based access control untuk different user levels
- Session management dengan automatic timeout
- Audit logging untuk compliance requirements
- Data encryption untuk sensitive information

## 📈 Performance Features

- **Parallel Processing**: Proses multiple files simultaneously
- **Memory Optimization**: Efficient memory usage untuk large datasets
- **Progress Tracking**: Real-time progress monitoring
- **Error Recovery**: Automatic retry mechanisms
- **Batch Operations**: Optimized batch processing

## 🛠️ Configuration

Sistem menggunakan file konfigurasi YAML untuk:
- Database connection settings
- Processing parameters
- User interface preferences
- Logging configurations
- Network-specific parameters

## 📝 Logging & Monitoring

- **Comprehensive Logging**: Detail logs untuk debugging
- **Real-time Monitoring**: Monitor proses secara real-time
- **Performance Metrics**: Metrics untuk optimisasi
- **Error Tracking**: Tracking dan reporting errors
- **Audit Trail**: Complete audit trail untuk compliance

## 🤝 Contributing

Silakan baca [CONTRIBUTING.md](CONTRIBUTING.md) untuk detail tentang code of conduct dan proses submit pull requests.

## 📄 License

Project ini dilisensikan di bawah MIT License - lihat file [LICENSE](LICENSE) untuk detail.

## 📞 Support

Untuk support dan pertanyaan:
- Create issue di [GitHub repository](https://github.com/hfhafan/etl-raw-to-sql/issues)
- Email: [support email]
- Documentation: Lihat folder `docs/`

## 🎯 Roadmap

- [ ] Support untuk format data tambahan
- [ ] Integration dengan cloud storage
- [ ] Advanced analytics dan reporting
- [ ] API endpoints untuk integration
- [ ] Mobile companion app
- [ ] Real-time data streaming

## 📥 Download Links

### Production Application
- **[Google Drive Download](https://drive.google.com/drive/folders/1WSzitOLnPO3ilwKAl1NwxyQnIO6nEzwf?usp=drive_link)** - Ready-to-use executable
- **File**: `SQL Upload Processing Tool.exe` (164.3 MB)

### Source Code & Documentation
- **[GitHub Repository](https://github.com/hfhafan/etl-raw-to-sql)** - Sample code dan dokumentasi
- **[Documentation](https://github.com/hfhafan/etl-raw-to-sql/tree/main/docs)** - Detailed documentation

---

**Note**: Ini adalah sample/demo version yang menunjukkan konsep dan arsitektur sistem. Production version memiliki additional security dan enterprise features. 
