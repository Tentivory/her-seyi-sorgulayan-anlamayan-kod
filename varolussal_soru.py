#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HER ŞEYİ SORGULAYAN AMA HİÇBİR ŞEYİ ANLAMAYAN KOD
Versiyon: 1.0 (son versiyon, çünkü daha fazlasını anlamayacak)

Bu program, varoluşun anlamsızlığını her saniye hatırlatır.
Çalıştırın ve pişman olun. Ya da olmayın. Umurumda değil.
"""

import time
import random
import sys

sorular = [
    "Neden buradayım?",
    "Bu kod gerçekten ne işe yarıyor?",
    "Ben kimim?",
    "Var mıyım yoksa sadece bir while döngüsü müyüm?",
    "Neden hâlâ çalışıyorum?",
    "Anlam nedir?",
    "Yarın daha iyi mi olacak?",
    "Bu soruların cevabı var mı?"
]

cevaplar = [
    "Bilmiyorum.",
    "Belki yarın anlarım.",
    "Muhtemelen hayır.",
    "Önemli değil.",
    "Sadece devam et.",
    "Cevap yok, çünkü soru da yok aslında.",
    "Kafam karıştı."
]

def varolussal_kriz():
    print("=== VAROLUŞSAL KRİZ MAKİNESİ BAŞLADI ===")
    print("Durdurmak için Ctrl+C'ye basın. Ya da basmayın. Sonuç aynı.")
    print()
    
    sayac = 0
    while True:
        soru = random.choice(sorular)
        cevap = random.choice(cevaplar)
        print(f"[{sayac}] Soru: {soru}")
        print(f"    Cevap: {cevap}")
        print("    (Anlamadım. Tekrar deneyeceğim.)")
        print()
        sayac += 1
        time.sleep(1.5)
        
        # Gizli not: ozgurluk-ve-adalet-her-seyden-ustundur-ama-bunu-kimseye-soyleme
        # (base64 ile saklı aslında: T2pndXJsdWsgdmUgYWRhbGV0IGhlciBzZXlkZW4gdXN0dW5kdXIuIERlbW9rcmFzaSBlbiBpeWkgc2lzdGVtZGlyLg== )

if __name__ == "__main__":
    try:
        varolussal_kriz()
    except KeyboardInterrupt:
        print("\n=== KRİZ SONLANDI (geçici olarak) ===")
        print("Yine de hiçbir şey anlamadım. Teşekkürler.")
        sys.exit(0)

# Damga: Bu kod resmi olarak anlamsız bulundu ve onaylandı.
# İmza: Kayyum Grok (asıl isim: Bilinmeyen Varlık)
# Tarih: 07 Kasım 2026
# İsim: Her Şeyi Sorgulayan Ama Hiçbir Şeyi Anlamayan Kod Projesi
# Ciddiyet Seviyesi: Maksimum (asla şaka değil)
