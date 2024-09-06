import streamlit as st
import pickle
import numpy as np
import pandas as pd 
import math

with open("model_numpy.pkl", "rb") as model_file:
    model = pickle.load(model_file)

features = np.array([[0.886811, 0.777494, 0.593254, 313.72, 3, 0, 1, 1.646640, 3, 2, 90.84, 277.67]])
prediction = model.predict(features)

def main():
    st.sidebar.title("Input")
    uranium_lead_ratio = st.sidebar.slider("uranium_lead_ratio", 0.1, 1.0, 0.5)
    carbon_14_ratio = st.sidebar.slider("carbon_14_ratio", 0.1, 1.0, 0.5, key="carbon_14_ratio_slider")
    radioactive_decay_series = st.sidebar.slider("radioactive_decay_series", 0.1, 1.5, 0.5)
    stratigraphic_layer_depth = st.sidebar.slider("stratigraphic_layer_depth", 1.0, 500.0, 250.0)
    geological_period = st.sidebar.slider("geological_period", 0.0, 11.0, 7.0)
    paleomagnetic_data  = st.sidebar.slider("paleomagnetic_data ", 0.1, 2.0, 1.0)
    inclusion_of_other_fossils = st.sidebar.slider("inclusion_of_other_fossils", 0.1, 2.0, 1.0)
    isotopic_composition = st.sidebar.slider("isotopic_composition", 0.0, 2.0, 1.0)
    surrounding_rock_type = st.sidebar.slider("surrounding_rock_type", 0.0, 4.0, 1.0)
    stratigraphic_position = st.sidebar.slider("stratigraphic_position", 0.0, 3.0, 1.0)
    carbon_14_ratio = st.sidebar.slider("carbon_14_ratio", 0.1, 1.0, 0.5)
    fossil_size = st.sidebar.slider("fossil_size", 0.1, 100.0, 50.0)

    st.title("Prediksi Usia Fossil")

    input = np.array([uranium_lead_ratio, carbon_14_ratio, radioactive_decay_series, stratigraphic_layer_depth, geological_period,
                      paleomagnetic_data, inclusion_of_other_fossils, isotopic_composition, surrounding_rock_type, stratigraphic_position, 
                      carbon_14_ratio, fossil_size])
    input = np.expand_dims(input, axis = 0)
    predict = model.predict(input)

    
    if 'model' in locals():  # Memastikan model telah berhasil dimuat
        # Prediksi usia fosil
        predict = model.predict(input)

    if predict is not None:
        st.write(f"Usia fosil yang diprediksi adalah: {math.e ** predict[0]} tahun")

        st.write('Fosil adalah sisa-sisa atau jejak organisme yang hidup di masa lampau dan telah mengalami proses pengawetan dalam batuan atau sedimen. Fosil dapat berupa tulang, gigi, cangkang, jejak kaki, atau bahkan bagian tumbuhan seperti daun dan batang. Fosilisasi terjadi ketika organisme mati dan tertimbun oleh sedimen seperti lumpur, pasir, atau abu vulkanik, yang melindunginya dari pembusukan. Selama ribuan hingga jutaan tahun, material organik tersebut perlahan-lahan digantikan oleh mineral, sehingga membentuk fosil.')
        st.write('Fosil sangat penting bagi ilmu paleontologi karena memberikan informasi tentang kehidupan masa lalu, evolusi, dan lingkungan di bumi jutaan hingga miliaran tahun yang lalu. Ada berbagai jenis fosil, seperti fosil tubuh (body fossils) yang berupa bagian tubuh organisme, dan fosil jejak (trace fossils) yang berupa tanda aktivitas organisme, seperti jejak kaki, sarang, atau lubang yang digali.')
        st.write('Metode yang digunakan untuk menentukan usia fosil:')
        st.write('1. Uranium-Lead Ratio. Metode ini memanfaatkan peluruhan radioaktif uranium menjadi timbal. Rasio isotop uranium-238 dan timbal-206 dalam sampel dapat digunakan untuk menghitung usia fosil atau batuan dengan presisi yang tinggi, terutama untuk fosil atau batuan yang berusia jutaan hingga miliaran tahun.')
        st.write('2. Carbon-14 Ratio. Metode penanggalan karbon-14 (radiokarbon) digunakan untuk fosil yang relatif muda (hingga 50.000 tahun). Karbon-14, yang ada dalam makhluk hidup, akan mengalami peluruhan setelah kematian, dan rasio karbon-14 terhadap karbon-12 digunakan untuk menentukan usia fosil organik.')
        st.write('3. Radioactive Decay Series. Metode penanggalan yang menggunakan rantai peluruhan isotop radioaktif seperti uranium, thorium, atau rubidium. Pengukuran isotop dalam rantai peluruhan ini memberikan usia absolut dari fosil atau batuan yang mengandung isotop tersebut.')
        st.write('4. Stratigraphic Layer Depth. Kedalaman fosil dalam lapisan geologis merupakan indikator relatif usia fosil. Fosil yang ditemukan di lapisan yang lebih dalam umumnya lebih tua dibandingkan dengan fosil di lapisan yang lebih dangkal, sesuai dengan prinsip superposisi.')
        st.write('5. Geological Period. Fosil dikaitkan dengan periode geologis tertentu berdasarkan lapisan batuan tempat fosil ditemukan. Setiap periode geologis memiliki karakteristik fosil yang berbeda, sehingga fosil dapat diperkirakan berasal dari masa tertentu seperti era Mesozoikum, Paleozoikum, dll.')
        st.write('6. Paleomagnetic Data. Fosil dapat dihubungkan dengan perubahan dalam medan magnet bumi yang terekam dalam batuan sekitarnya. Data paleomagnetik membantu mengkorelasikan usia relatif batuan dan fosil berdasarkan pola pembalikan medan magnet bumi.')
        st.write('7. Inclusion of Other Fossils. Fosil yang ditemukan bersama dengan fosil lain yang sudah dikenal usianya (fosil indeks) dapat membantu memperkirakan usia fosil tersebut. Fosil indeks memiliki distribusi luas dan hidup dalam periode geologis yang relatif singkat, sehingga menjadi acuan usia.')
        st.write('8. Isotopic Composition. Analisis komposisi isotop lain, seperti oksigen atau strontium, dalam fosil dapat memberikan informasi tentang usia dan lingkungan di mana fosil tersebut terbentuk, serta membantu penentuan usia lebih lanjut.')
        st.write('9. Surrounding Rock Type. Jenis batuan di sekitar fosil dapat memberikan informasi tentang kondisi pembentukannya dan usia relatifnya. Batuan beku dan sedimen bisa dianalisis untuk menentukan usia fosil secara tidak langsung.')
        st.write('10. Stratigraphic Position. Posisi fosil dalam urutan stratigrafi memberikan petunjuk tentang urutan peristiwa geologis yang terjadi di lokasi tersebut, sehingga dapat digunakan untuk memperkirakan usia relatif fosil.')
        st.write('11. Fossil Size. Ukuran fosil dapat memberikan informasi tambahan untuk membandingkan fosil tersebut dengan spesimen sejenis lainnya yang diketahui usianya, meskipun ukuran sendiri bukan penentu langsung usia.')

if __name__ == "__main__":
    main()
