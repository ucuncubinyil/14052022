def sansur(cumle_listesi, yasakli_kelime, yeni_kelime):
    for i in range(len(cumle_listesi)):
        cumle_listesi[i] = cumle_listesi[i].replace(yasakli_kelime, yeni_kelime)

    return cumle_listesi