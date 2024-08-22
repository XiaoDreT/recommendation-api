# **SISTEM REKOMENDASI FILM: CONTENT-BASED FILTERING**

## Data Understanding
Data yang digunakan pada proyek ini diambil dari data The Movie Database (TMDb) yang didapat dari hasil generate The Movie Database API dimana pada dataset ini berisikan tentang 5000 film yang disajikan dalam sebuah dataset format CSV dengan berbagai macam variabel seperti ID film, judul film, cast, crew, dan lain-lain. 

Proyek ini menggunakan dataset sebagai bahan dalam membuat sistem rekomendasi film ini, dimana dataset ini digunakan untuk memprediksi peringkat atau preferensi yang akan diberikan pengguna pada suatu item.

Pada dataset TMDB 5000 Movie Dataset, jumlah data yang digunakan pada proyek ini dari dataset tersebut berjumlah **5000 data dengan matriks baris dan kolom sebanyak 5000 baris dan 24 kolom** yang berupa film-film yang akan diolah dalam membuat sebuah sistem rekomendasi. Kondisi data yang digunakan pada proyek ini masih terlihat **noise** untuk dilatih dalam model rekomendasi dengan adanya beberapa variabel yang masih memiliki **nilai null atau missing value**. 

Dataset:
[TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata/data)

**Variabel-variabel pada TMDB 5000 Movie Dataset adalah sebagai berikut:**
- movie_id : merupakan id unik setiap film. 
- cast : merupakan variabel yang berisi informasi mengenai nama aktor dan karakter yang dimainkan.
- title: merupakan variabel yang berisi judul-judul film. 
- crew : merupakan variabel yang berisi informasi mengenai sutradara film, produser, dan kru lainnya. 
- budget : merupakan anggaran produksi film (dolar AS).
- genres : merupakan genre film seperti aksi, komedi, horror, dan sebagainya.
- homepage : merupakan URL halaman web resmi film.
- id : merupakan id unik setiap film. 
- keywords : merupakan kata kunci yang menggambarkan film.
- original_language : merupakan bahasa yang digunakan dalam pembuatan film.
- original_title : merupakan judul film dalam tulisan bahasa aslinya.
- title : merupakan judul film dalam distribusi internasional.
- overview: merupakan sinopsis singkat tentang film.
- popularity : merupakan skor popularitas film. 
- production_companies : merupakan kumpulan perusahaan yang terlibat dalam pembuatan film. 

### Exploratory Data Analysis (EDA)

- **Melakukan pengecekan missing value pada dataset gabungan.** 

    Tahapan ini merupakan pengecekan nilai null pada variabel-variabel yang ada dalam dataset gabungan. Pengecekan ini merupakan hal yang krusial karena dalam membuat sistem rekomendasi, model rekomendasi bisa dilatih berdasarkan data yang lengkap dan akurat. 

    Output:
    
        budget                     0
        genres                     0
        homepage                3091
        id                         0
        keywords                   0
        original_language          0
        original_title             0
        overview                   3
        popularity                 0
        production_companies       0
        production_countries       0
        release_date               1
        revenue                    0
        runtime                    2
        spoken_languages           0
        status                     0
        tagline                  844
        title                      0
        vote_average               0
        vote_count                 0
        tittle                     0
        cast                       0
        crew                       0
        dtype: int64

#### Data Understanding untuk Pendekatan Content-Based Filtering

- **Mengecek fitur 'overview' pada dataset gabungan.**

    Melakukan pengecekan fitur overview untuk dilakukan vektorisasi. 

        Output:
        0    In the 22nd century, a paraplegic Marine is di...
        1    Captain Barbossa, long believed to be dead, ha...
        2    A cryptic message from Bond’s past sends him o...
        3    Following the death of District Attorney Harve...
        4    John Carter is a war-weary, former military ca...
        Name: overview, dtype: object   

## Data Preparation

- **Melakukan penggabungan data pada kolom id dalam dataset TMDB 5000 Movie Dataset.** 
    
    Penggabungan data pada kolom id digunakan untuk mendapatkan keseluruhan data yang ada pada file credits dan file movie pada dataset TMDB 5000 Movie Dataset. 

    Output:
    
        Index(['budget', 'genres', 'homepage', 'id', 'keywords', 'original_language',
        'original_title', 'overview', 'popularity', 'production_companies',
        'production_countries', 'release_date', 'revenue', 'runtime',
        'spoken_languages', 'status', 'tagline', 'title', 'vote_average',
        'vote_count', 'tittle', 'cast', 'crew'],
        dtype='object')

#### Data Preparation untuk Pelatihan Model dengan Pendekatan Content-Based Filtering:

- **Menghitung vektor pada setiap 'overview' dengan menggunakan teknik Term Frequency-Inverse Document Frequency (TF-IDF).** 
    
    Ini akan memberikan sebuah matriks dimana setiap kolom mewakili sebuah kata dalam overview kosakata (semua kata yang muncul di setidaknya satu dokumen) dan setiap baris mewakili sebuah film, seperti sebelumnya, hal ini dilakukan untuk mengurangi pentingnya kata-kata yang sering muncul di overview plot dan oleh karena itu, pentingnya kata-kata tersebut dalam penghitungan nilai kemiripan akhir.

## Modeling

### Model Development dengan Content-Based Filtering

#### Dalam sistem rekomendasi ini, fitur film 'overview' digunakan untuk menemukan kemiripannya dengan film lain. Kemudian film yang paling mungkin mirip akan direkomendasikan.

#### Proses dan Tahapan Pembuatan Function Untuk Merekomendasikan Film:

    1. Membuat sebuah function untuk mendapatkan rekomendasi dengan mengembalikan data berupa top 10 film yang paling mirip dengan indeks aslinya. 

       Function film_recommendations ini dirancang untuk memberikan rekomendasi film berdasarkan judul film yang diberikan sebagai input. Fungsi ini bekerja dengan menghitung kemiripan antara film input dengan semua film lain dalam dataset, lalu mengembalikan 10 film yang paling mirip.

       Parameter yang digunakan dalam function ini:
       - title: Input berupa string yang berisi judul film yang ingin dicari film serupa.
       - cosine_sim: Matriks yang berisi nilai cosine similarity antara setiap pasangan film. Matriks ini diasumsikan sudah dihitung sebelumnya dan berisi nilai kemiripan antara 0 hingga 1, di mana nilai 1 menunjukkan kemiripan yang sempurna.

       Langkah (Flow) pada function film_recommendations:
       - Input Judul Film : Memasukkan judul film sebagai input fungsi. Sebagai contoh, judul film yang dimasukkan adalah "The Shawshank Redemption".
       - Mencari Indeks Film : Fungsi akan mencari di mana letak film "The Shawshank Redemption" dalam matriks cosine similarity. Misalkan, film ini berada pada baris ke-100 dalam matriks.
       - Mendapatkan Similarity Score (Skor Kemiripan) : Baris ke-100 dari matriks cosine similarity akan diambil. Baris ini berisi nilai kemiripan antara film "The Shawshank Redemption" dengan semua film lainnya. 
         Misalkan, nilai kemiripan dengan film "The Green Mile" adalah 0.8, dengan "Forrest Gump" adalah 0.7, dan seterusnya.
       - Mengurutkan Berdasarkan Kemiripan : Pasangan (indeks film, nilai kemiripan) diurutkan dari nilai kemiripan tertinggi ke terendah.
       - Memilih 10 Film Teratas : Hanya 10 pasangan pertama (kecuali pasangan pertama yang merupakan film itu sendiri) yang diambil.
       - Mendapatkan Judul Film : Indeks dari 10 film teratas digunakan untuk mencari judul film yang sesuai dalam DataFrame df1. Misalkan, indeks 150 ternyata adalah film "Shawshank Redemption 2", dan indeks 10 adalah film "The Green Mile".

    2. Mendapatkan rekomendasi film. 
 
#### Hasil Rekomendasi:

    # Mendapatkan rekomendasi film yang mirip dengan The Dark Knight Rises
    film_recommendations('The Dark Knight Rises')

    Output:

    65                              The Dark Knight
    299                              Batman Forever
    428                              Batman Returns
    1359                                     Batman
    3854    Batman: The Dark Knight Returns, Part 2
    119                               Batman Begins
    2507                                  Slow Burn
    9            Batman v Superman: Dawn of Justice
    1181                                        JFK
    210                              Batman & Robin
    Name: title, dtype: object

#### Kelebihan: 

- **Relevansi awal yang tinggi** : Bagi pengguna baru, sistem ini dapat memberikan rekomendasi yang relevan dengan cepat berdasarkan informasi profil pengguna.
- **Penjelasan yang jelas** : Sistem dapat memberikan alasan mengapa suatu film direkomendasikan, karena rekomendasi didasarkan pada kesamaan fitur antara film yang sudah pernah dinikmati.
- **Tidak memerlukan banyak data pengguna** : Sistem ini tidak memerlukan banyak data interaksi pengguna lain untuk memberikan rekomendasi.

#### Kekurangan:

- **Rekomendasi yang terbatas** : Sistem cenderung memberikan rekomendasi yang mirip dengan apa yang sudah dikenal pengguna, sehingga sulit untuk menemukan film baru yang berbeda.
- **Masalah cold start untuk item baru** : Film baru yang tidak memiliki banyak informasi atau metadata akan sulit direkomendasikan.
- **Ketergantungan pada kualitas metadata** : Kualitas metadata film sangat berpengaruh pada akurasi rekomendasi.

## Evaluation

### Evaluasi Model Content-Based Filtering

Tahap evaluasi model ini menggunakan metrik presisi (precision metric).

**Penjelasan Metrik Evaluasi**
Metrik Presisi (Precision Metric) melakukan perbandingan antara rekomendasi film yang relevan dan rekomendasi yang diberikan sistem. Untuk jelasnya, bisa diliat rumus daripada Presisi Sistem Rekomendasi berikut ini:  

![Rumus Presisi](https://github.com/user-attachments/assets/83777201-c68b-45dd-a23d-5dc85e2df07d)

Jika dilihat dari output hasil rekomendasi yang diberikan sistem rekomendasi pada Modeling Content-Based Filtering, dimana 10 film yang direkomendasikan, terdapat 8 film yang similar (mirip) dengan indeks film aslinya ("The Dark Knight Rises"). 

Jika diformulakan dengan rumus presisi akan mendapatkan hasil sebagai berikut:

    film yang relevan/rekomendasi film yang diberikan sistem = 8/10. 

Presisi yang didapat adalah 80%. 

### Kesimpulan

*Dengan adanya dua pendekatan algoritma dalam membuat sistem rekomendasi yaitu Content-Based Filtering dan Collaborative Filtering dengan menggunakan metrik evaluasi Precision, membuktikan bahwa pendekatan algoritma ini dapat membuat dan mengembangkan sistem rekomendasi film yang mampu memberikan saran film yang relevan dan personal sehingga pengguna mendapatkan kepuasan dan pengalaman yang menyenangkan dalam menonton film. Solution statements ini dapat dibuktikan dengan adanya sistem rekomendasi yang memberikan "Top 10 Movie Recommendation" kepada pengguna.*

## Deployment

Pada tahapan ini, Sistem Rekomender yang telah dibuat akan di deploy menggunakan platform Render pada website render.com. Anda dapat mencoba tautan API yang telah di deploy dengan menggunakan aplikasi Postman:

**Link:** 

https://recommendation-api-4an0.onrender.com

**Format JSON Request:** 

{

    "title": "(movie-full-title)"

}

**Contoh:**

- {

        "title": "Spider-Man"

    }

- {

        "title": "The Dark Knight Rises"
    
    }

## Run Proyek di Lokal

Clone the project

```
  $ git clone https://github.com/XiaoDreT/recommendation-api
```

Go to the project directory

```
  $ cd recommendation-api
```

Install dependencies

```
  $ pip install -r requirements.txt

  or 

  $ pip install pandas scikit-learn flask gunicorn
```

Start the server

```
  $ python recommendation_api.py
```

### Catatan:

### Pada proyek ini, versi python yang digunakan adalah **3.10.12** dan juga menggunakan environtment **Virtualenv** yang tersedia pada python, Anda dapat menggunakan environtment “conda” sebagai environtment alternatif yang lain. Ini dapat membantu untuk deploy API Rekomendasi. 
