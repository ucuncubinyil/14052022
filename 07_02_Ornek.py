# Kendi isminiz ile bir modül oluşturunuz.
# Modül içerisnde bir sansur(cumlelistesi,yasaklıkelime,yenikelime) isminde bir metot oluşturun
# Bu metot kendisine gönderilen cümle listesindeki yasaklı kelimeyi yeni kelimeyle sansürlesin
# sansur("Çocuklar kahve içerse kararır.","kahve","k")

from Sansur import sansur

cumleler = []
for i in range(3):
    cumle =  input("Cümle girin: ")
    cumle =  cumle.strip()
    cumleler.append(cumle)


yeni_liste =  sansur(cumleler, "kahve", "**")
print(yeni_liste)