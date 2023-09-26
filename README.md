## **CRISP-DM** (CRoss Industry Standard Process for Data Mining)

CRISP-DM (CRoss Industry Standard Process for Data Mining) adalah model proses dengan enam tahap yang secara alami menggambarkan siklus kehidupan ilmu data. Ini seperti seperangkat pagar pengaman untuk membantu untuk merencanakan, mengorganisir, dan melaksanakan proyek ilmu data (atau machine learning). Kerangka kerja inilah yang akan kami gunakan untuk membuat machine learning.

Terdapat beberapa tahapan kami lakukan :
1. Pemahaman bisnis - Apa yang dibutuhkan oleh bisnis?
2. Pemahaman data - Data apa yang kita miliki / butuhkan? Apakah bersih?
3. Persiapan data - Bagaimana kita mengorganisir data untuk pemodelan?
4. Pemodelan - Teknik pemodelan apa yang harus kita terapkan?
5. Evaluasi - Model mana yang paling memenuhi tujuan bisnis?
6. Pengimplementasian - Bagaimana pemangku kepentingan mengakses hasilnya?


## **1. Pemahaman bisnis**
Daegu adalah kota metropolitan terbesar ke-4 di Korea Selatan, dan resminya disebut Kota Metropolitan Daegu. Kota ini terletak di bagian tenggara Korea Selatan, di tepi Sungai Nakdong. Kota ini pertama kali disebutkan dalam catatan sejarah pada abad ke-6, dan pada abad ke-8 menjadi ibu kota Kerajaan Silla. Daegu menjadi pusat politik dan budaya penting selama periode Goryeo dan Joseon. Pada abad ke-19, Daegu menjadi pusat perdagangan dan industri, dan terus berkembang selama abad ke-20.
<br><br>
Luas kota Daegu adalah 886,12 km², termasuk daratan dan sungai. Menurut Badan Statistik Korea, populasi penduduk Daegu pada tahun 2023 adalah 2.463.490 jiwa (sumber [kosis.kr](https://kosis.kr/eng/index/index.do)). Jika luas kota Daegu dibagi dengan total populasi kota Daegu, maka setiap orang mendapatkan rata-rata 2,87 meter persegi. Dari hasil ini kita dapat menyimpulkan jika kita ambil contoh 1 keluarga terdapat 3 orang, maka 1 keluarga hanya mendapatkan 8,61 meter persegi. Sehingga sangat tidak dimungkinkan jika seluruh keluarga yang tinggal di Daegu memiliki rumah. Salah satu alternatif yang bisa dilakukan adalah dengan memiliki dan tinggal di apartemen.
<br><br>
Apartemen adalah solusi yang sangat menarik bagi masyarakat yang ingin menetap di Daegu. Dengan keterbatasan lahan perumahan dan tingginya harga rumah di kota ini, memiliki apartemen menjadi pilihan yang sangat rasional. Memiliki apartemen bukan hanya memberikan tempat tinggal yang nyaman, tetapi juga merupakan bentuk kepemilikan properti yang berharga di salah satu kota terbesar di Korea Selatan.

### **Permasalahan**

Menentukan harga jual apartemen adalah tugas yang penuh tantangan bagi individu atau perusahaan properti (tim pricing) yang ingin menjual unit apartemen mereka di Daegu. Penetapan harga yang tepat sangatlah penting, karena harga yang terlalu tinggi dapat menghambat proses penjualan. Sementara harga yang terlalu rendah dapat mengurangi potensi keuntungan. Keputusan ini tidak hanya bergantung pada faktor internal seperti fasilitas apartemen, tetapi juga sangat dipengaruhi oleh faktor eksternal seperti lokasi, jarak ke fasilitas publik, dsb.

Dalam konteks ini, permasalahan utama adalah :
1. Bagaimana mengidentifikasi dan memahami faktor-faktor yang paling berpengaruh terhadap harga jual apartemen di Daegu?
2. Selain itu, kita juga ingin mengeksplorasi apakah kita dapat mengembangkan model prediksi harga yang dapat membantu pemilik apartemen menentukan harga yang sesuai dengan kondisi pasar yang berubah-ubah?

Dengan demikian, penyelesaian masalah ini akan memberikan wawasan berharga bagi pemilik apartemen dan calon pembeli, serta mendukung kelancaran proses penjualan dan pembelian properti di Daegu.

### **Tujuan Penyelesaian Masalah**

Berikut adalah beberapa alasan mengapa penyelesaian masalah ini penting :
1. **Keuntungan Pemilik Apartemen**: Penentuan harga jual yang tepat dapat membantu pemilik apartemen memaksimalkan keuntungan dari penjualan properti mereka. Jika harga diatur terlalu tinggi, apartemen mungkin sulit terjual dan pemilik akan mengalami kerugian waktu dan finansial. Sebaliknya, harga terlalu rendah mengakibatkan kehilangan potensi keuntungan. 
2. **Efisiensi Waktu**: Dalam penentuan harga biasanya seseorang akan melakukannya dengan cara datang ke lingkungan sekitar unit, kemudian menanyakan harga apartemen yang dijual juga. Hal ini mungkin kurang efektif dikarenakan, pemilik harus mencari-cari unti apartemen lain yang sedang dijual dan harga yang didapat belum tentu sesuai. Dengan dibangun machine learning dalam memprediksi harga bertujuan agar pemilik lebih mengetahui harga unit apartemen yang tepat, mengurangi tenaga, dan mempersingkat waktu.

Oleh karena itu, dengan memahami harga properti secara lebih baik melalui machine learning, kita dapat membuat pemilik properti mendapatkan keuntungan dalam menjual apartemen dan mengefisiensi waktu penentuan harga jualnya.

### **Metriks Evaluasi**
Evaluasi Metriks yang akan kami gunakan adalah dengan RMSE, MAE dan MAPE. Semakin kecil nilainya, maka model semakin akurat dan akan memprediksi harga apartemen yang sesuai dengan limitasi fitur yang digunakan.
<br>

#### **RMSE (Root Mean Square Error)**
RMSE adalah salah satu metrik evaluasi yang umum digunakan dalam masalah regresi untuk mengukur sejauh mana perbedaan antara nilai prediksi dari model dan nilai sebenarnya dari data. RMSE mengukur rata-rata dari selisih kuadrat antara setiap prediksi dan nilai sebenarnya, kemudian diambil akar kuadratnya. Ini memberikan gambaran tentang seberapa besar deviasi atau kesalahan rata-rata dari prediksi model terhadap nilai sebenarnya.

#### **MAE (Mean Absolute Error)**
MAE digunakan sebagai metrik evaluasi karena memiliki beberapa keunggulan, terutama ketika digunakan dalam konteks memprediksi harga (price) seperti dalam kasus ini:
1. Tidak Sensitif terhadap Outliers: MAE tidak terlalu sensitif terhadap data yang menyimpang (outliers), sehingga jika ada beberapa nilai ekstrem dalam data, MAE tetap memberikan gambaran yang baik tentang seberapa baik model Anda memprediksi sebagian besar data.
2. Cocok untuk Prediksi Harga: MAE cocok digunakan dalam kasus prediksi harga (price) karena harga sering memiliki rentang nilai yang besar, mulai dari satuan hingga milyaran. MAE tidak memberikan bobot lebih besar kepada perbedaan harga yang lebih besar, sehingga berguna untuk mengukur kesalahan prediksi dalam skala yang seragam.

#### **MAPE (Mean Absolute Percentage Error)**
MAPE adalah metrik evaluasi yang digunakan untuk melihat kesalahan dalam bentuk persentase dari nilai sebenarnya. Ini memberikan gambaran tentang sejauh mana prediksi Machine Learning mendekati nilai sebenarnya dalam bentuk persentase.
1. Evaluasi dalam Bentuk Persentase: MAPE mengukur kesalahan prediksi dalam bentuk persentase, yang memungkinkan kita untuk menilai tingkat akurasi model relatif terhadap harga sebenarnya.
2. Cocok untuk Prediksi Harga:  MAPE cocok digunakan dalam kasus prediksi harga (price) karena harga umumnya tidak memiliki nilai 0, sehingga MAPE yang sensitif terhadap nilai 0 tidak mungkin terjadi pada kasus ini.

## **2. Pemahaman Data**

### **Kolom Dataset**
Berikut adalah kolom yang terdapat di dataset kami: 

- **HallwayType** : Tipe/jenis apartemen
- **TimeToSubway** : Waktu ke Stasiun Kereta Bawah Tanah Terdekat
- **SubwayStation** : Nama stasiun kereta bawah tanah terdekat
- **N_FacilitiesNearBy(ETC)** : Jumlah fasilitas terdekat
- **N_FacilitiesNearBy(PublicOffice)** : Jumlah fasilitas kantor publik terdekat
- **N_SchoolNearBy(University)** : Jumlah universitas terdekat
- **N_Parkinglot(Basement)** : Jumlah tempat parkir bawah tanah
- **YearBuilt** : Tahun apartemen dibagun
- **N_FacilitiesInApt**	: Jumlah fasilitas dalam apartemen
- **Size(sqf)** : Ukuran apartemen (dalam Square foot)
- **SalePrice** : Harga apartemen (dalam 1.000 Won)


## **3. Persiapan Data**

Terdapat beberapa langkah yang akan kami lakukan pada tahap ini :
1. Pada tahap ini kita akan lebih memahami data yang akan digunakan untuk membangun Machine Learning. 
2. Kami juga akan melakukan pembersihan data jika terdapat data yang missing value, duplicate, atau outliers. 
3. Kami juga akan melakukan transformasi data jika terdapat data yang masih belum sesuai formatnya. 

Tujuannya adalah agar kami dapat membuat keputusan yang lebih baik dan data ini lebih sesuai dan lebih siap digunakan. Data yang baik juga dapat meningkatkan performa dari Machine Learning yang akan kami buat.

### **Encoding dan Scaling Data**

**Feature Engineering**
<br>
Feature Engineering adalah proses di mana kita mengubah fitur-fitur yang ada dalam dataset untuk meningkatkan kualitas model dan meningkatkan kinerja algoritma Machine Learning. Tahap ini penting dilakukan agar data terrepresentasi menjadi lebih baik, sehingga model dapat memahami pola-pola yang ada dalam data dengan lebih baik. Berikut tahapan yang akan kami jalankan :

1. **Mengubah Data Kategorikal menjadi Numerik**
<br>
    Pada tahap ini kita akan mengubah/ encoding tipe data kategori menjadi numerik agar dapat menjadi fitur dalam Machine Learning.
    -  OneHot Encoding:
        - Kami akan menggunakan OneHot pada kolom **HallwayType**, dikarenakan jumlahnya hanya 3. Tipe setiap apartemen kami asumsikan adalah setara (variabel nominal)
    - Binary Encoding :
        - Kami akan menggunakan Binary pada kolom **SubwayStation**, dikarenakan jumlahnya lumayan banyak (8) dan diasumsikan setara (variabel nominal)
    - Ordinal Encoding:
        - Kami akan menggunakan Ordinal pada kolom **TimeToSubway**. Fitur ini merupakan variabel ordinal, dikarenakan datanya berisi waktu yang memiliki tingkatan. Maka kami akan membuat unit yang paling dekat dengan stasiun bawah tanah merupakan tingkatan tertinggi dan  unit yang tidak dekat dengan stasiun bawah tanah adalah tingkatan terendah. 
<br><br>

2. **Scaling Data Numerik**
<br>
Scaling adalah metode untuk melakukan transformasi terhadap data numerik agar antar variabel(fitur) memiliki skala yang sama. Kami akan melakukan Scaling (mengubah skala) pada seluruh data numerik agar memiliki nilai yang serupa atau setara. Pada kolom YearBuilt juga kami scaling, dikarenakan dilihat korelasinya YearBuilt dan SalePrice memiliki hubungan linear. 
<br><br>Metode scaling yang kami gunakan adalah Robust Scaler. Metode ini kami pilih karena saat kita melihat persebaran data kolom Size di atas, data masih memiliki data outliers. Robust Scaler cocok digunakan dikarenakan tidak sensitif terhadap data outliers. Cara Kerja Robust Scaler adalah dengan data dikurangi dengan nilai kuartil 1 lalu dibagi dengan selisih antara kuartil 3 dan kuartil 1. 

## **4. Permodelan dan Evaluasi**

#### **XGBoost Regressor**

XGBoost Regressor adalah algoritma untuk model regresi yang menggunakan teknik Boosted Tree. Algoritma ini memiliki beberapa parameter yang dapat diubah-ubah untuk mengatur kinerja model. Berikut adalah beberapa parameter yang akan kami gunakan untuk melakukan tuning :
1. **n_estimators** adalah jumlah pohon keputusan yang akan dibangun. Semakin besar jumlahnya, maka akan semakin kompleks modelnya.
2. **max_depth** adalah jumlah kedalaman maksimum dari setiap pohon. Nilai yang besar memungkinkan model untuk lebih memahami data training, namun dapat menyebabkan overfitting
3. **learning_rate** adalah tingkat pembelajaran yang akan mengontrol seberapa besar langkah pembelajaran yang diambil. Nilai yang lebih kecil membuat model akan belajar perlahan dan lebih stabil, tetapi membutuhkan lebih banyak pohon untuk mencapai kinerja yang baik. Nilai yang lebih besar dapat membuat belajar lebih cepat namun kurang stabil. 
4. **gamma** adalah parameter yang mengontrol ketidakmampuan (penurunan dalam fungsi tujuan) yang diperlukan untuk melakukan pemisahan pada tingkat node atau disebut regularisasi. Node adalah titik di mana model membuat keputusan yang membantu mencegah pohon terlalu rumit.
5. **colsample_bytree** adalah seberapa banyak fitur (kolom) yang digunakan dalam setiap iterasi pohon. Membantu mengontrol keragaman antar pohon dalam ensemble. 
6. **subsample** adalah seberapa banyak data training yang digunakan dalam setiap iterasi pohon. Ini dapat membantu masalah overfitting dengan mengizinkan model melihat subset yang berbeda dari setiap iterasi.
7. **reg_alpha** adalah parameter yang mengendalikan kompleksitas model dengan mencegah fitur yang tidak relevan
8. **reg_lambda** adalah parameter yang mengontrol kompleksitas model dengan mencegah bobot pohon yang sangat besar

Kami akan menjelaskan bagaimana cara kerja model terbaik kita, yaitu : **XGBoost Regressor**
- XGBoost memulai dengan model awal yang sederhana, biasanya berupa pohon kecil yang disebut dengan *weak learner* atau *base learner*. Pohon ini memiliki tingkat kedalaman yang dangkal dan biasanya tidak dapat menghasilkan prediksi yang baik. 
- Pada setiap pohon baru, XGBoost memberikan bobot (weight) kepada setiap data point berdasarkan kesalahan (error) dari prediksi sebelumnya. Data yang memiliki kesalahan prediksi yang lebih tinggi akan diberi bobot lebih tinggi juga. Hal ini bertujuan untuk agar fokus dalam memperbaiki prediksi tersebut atau yang kita kenal dengan teknik **Boosting**. 
- Cara yang dilakukan untuk memperbaiki hasil tersebut adalah dengan membangun pohon baru. Hal tersebut dilakukan dengan menghitung gradien(gradients) dari fungsi kerugian (loss function) terhadap prediksi sebelumnya. Pohon baru ini ditempatkan di atas pohon sebelumnya. Setiap pohon baru menambahkan sedikit lebih banyak informasi ke model, dan kesalahan prediksi berkurang secara bertahap.
- Hasil akhir dari XGBoost adalah hasil dari menggabungkan (ensemble) semua pohon yang telah dibangun. Prediksi akhir adalah hasil penjumlahan prediksi dari setiap pohon, yang telah diberi bobot berdasarkan performa mereka. Prediksi ini merupakan hasil dari kombinasi semua pohon keputusan yang telah "belajar" dari data.
- XGBoost juga menggunakan teknik regularisasi untuk mencegah overfitting. Ini termasuk regularisasi L1 (Lasso) dan L2 (Ridge) terhadap bobot pohon dan data.


## **5. Pengimplementasian**

Untuk mencapai tujuan yang telah kita tetapkan, kami berencana untuk mengembangkan Machine Learning ini dalam bentuk API (Application Programming Interface). Dalam konteks ini, API akan menjadi alat yang memungkinkan integrasi Machine Learning dengan berbagai platform, termasuk situs web dan aplikasi yang digunakan dalam penjualan properti.

**Bagaimana API ini akan digunakan?**
1. **Aplikasi Jual Beli Properti**: Aplikasi atau situs web jual beli properti akan dapat menggunakan API ini untuk memprediksi harga apartemen yang sesuai. Ketika seorang individu ingin menjual unit properti mereka, mereka dapat mengisi informasi tentang unit tersebut pada aplikasi atau situs web tersebut. API ini akan memberikan prediksi harga yang realistis, membantu individu membuat keputusan yang lebih baik.
2. **Perusahaan Pengembang Properti**: Perusahaan pengembang properti juga dapat mengintegrasikan API ini dalam situs web atau aplikasi internal mereka. Ini memungkinkan mereka untuk dengan cepat menentukan harga yang sesuai untuk unit apartemen yang mereka jual.

**Manfaat Penggunaan API ini:**
- API ini akan memberikan kemudahan dan efisiensi dalam menentukan harga properti, menggantikan proses manual yang memakan waktu.
- Dengan menggunakan Machine Learning, API ini dapat memberikan perkiraan harga yang lebih akurat, membantu pemilik properti dan perusahaan menghindari kesalahan penentuan harga yang signifikan.
- Dengan harga yang sesuai, pemilik properti dapat menjual unit mereka dengan lebih cepat, menghemat waktu dan upaya.
- Pembeli properti juga akan mendapatkan manfaat dari prediksi harga yang tepat, membantu mereka membuat keputusan yang lebih baik dalam pembelian properti.
- API ini dapat membantu mengembangkan dan meningkatkan pasar properti Daegu, menciptakan ekosistem yang lebih sehat dan efisien.

## **Kesimpulan**
Hasil prediksi ini dapat diukur pencapaiannya melalui metrik RMSE, MAE, dan MAPE yang telah dihitung:
- RMSE **46775**
- MAE **38185**
- MAPE **19.31%**

Kemudian kita juga dapat mengidentifikasi dan memahami 5 faktor yang paling berpengaruh terhadap harga jual apartemen di Daegu, yaitu :
1. **Tahun Pembangunan** (Year Built) menjadi faktor yang paling berpengaruh terhadap harga apartemen, dengan skor Feature Importance sekitar 0.20. Apartemen yang lebih baru biasanya memiliki fitur dan fasilitas yang lebih modern, sehingga harganya menjadi lebih tinggi.
2. **Ukuran Apartemen** (Size(sqf)) juga memiliki pengaruh yang lumayan besar terhadap harga, dengan skor Feature Importance sekitar 0.18. Apartemen yang lebih besar biasanya memiliki lebih banyak kamar dan ruang, sehingga harganya lebih tinggi.
3. **Jumlah Fasilitas di Sekitar Apartemen** (N_FacilitiesNearBy(ETC)) memiliki pengaruh yang signifikan dengan skor Feature Importance sekitar 0.10. Apartemen yang dekat dengan fasilitas yang lebih lengkap membuat harga apartemen menjadi lebih tinggi
4. **Waktu ke Stasiun Bawah Tanah** (TimetoSubway) juga berpengaruh terhadap harga apartemen, dengan skor Feature Importance sekitar 0.09. Apartemen yang dekat dengan stasiun bawah tanah membuat harganya menjadi lebih tinggi.
5. **Jumlah Tempat Parkir di Basement** (N_Parkinglot(Basement)) memiliki pengaruh, dengan skor Feature Importance sekitar 0.09. Apartemen yang memiliki jumlah tempat parkir kendaraan yang banyak membuat harganya tinggi.

Dengan mengimplementasikan Machine Learning ini, kita dapat mencapai beberapa tujuan yang telah disebutkan sebelumnya. Namun, penting untuk memahami sejauh mana model ini dapat memberikan kontribusi terhadap pencapaian tujuan-tujuan tersebut:
1. **Keuntungan Pemilik Apartemen**: Model ini dapat membantu pemilik apartemen dalam menentukan harga jual yang lebih tepat. Dengan tingkat kesalahan yang relatif rendah seperti RMSE dan MAE yang masih dalam skala yang terjangkau, pemilik apartemen dapat menggunakan prediksi harga model sebagai panduan untuk menetapkan harga yang kompetitif. Namun, perlu diingat bahwa nilai MAPE sebesar 0.193163 mengindikasikan bahwa ada potensi kesalahan sebesar 19.31% dari harga sebenarnya, sehingga pemilik harus menggunakannya dengan bijak.
2. **Efisiensi Waktu**: Model ini dapat mempersingkat waktu yang diperlukan dalam menentukan harga jual properti. Pemilik tidak perlu lagi secara fisik datang ke lingkungan sekitar untuk menyelidiki harga apartemen yang dijual. Dengan memasukkan fitur-fitur yang ada di apartemennya, pemilik langsung mendapatkan prediksi harga yang sesuai. Namun, pemilik harus mengingat bahwa faktor-faktor seperti perubahan kondisi pasar dan lokasi properti tetap relevan, dan model ini hanya memberikan perkiraan.
