import random

def play_game():
    total_score = 0  # 3 oyun boyunca toplam puan

    # 3 oyun oynama döngüsü
    for game_number in range(1, 4):
        print(f"\n{game_number}. Oyun Başlıyor!")
        secret_number = random.randint(1, 10)
        attempts = 3  # Haklar
        points = 0  # Bu oyunda kazanılan puan

        print("1 ile 10 arasında bir sayı tuttum. Bakalım tahmin edebilecek misin!")

        # Tahmin döngüsü
        while attempts > 0:
            try:
                guess = int(input(f"\nTahmininizi girin ({attempts} hakkınız kaldı): "))
                
                if guess < 1 or guess > 10:
                    print("Lütfen 1 ile 10 arasında bir sayı girin.")
                    continue

                if guess == secret_number:
                    points = attempts  # Kalan hak kadar puan
                    print(f"Tebrikler! {attempts}. hakkınızda doğru tahmin ettiniz. Kazandığınız puan: {points}")
                    break
                elif guess < secret_number:
                    print("Daha yüksek bir sayı tahmin edin.")
                else:
                    print("Daha düşük bir sayı tahmin edin.")
                
                attempts -= 1  # Hak azalır

            except ValueError:
                print("Lütfen geçerli bir sayı girin.")
        
        # Tüm haklar bittiğinde
        if attempts == 0 and points == 0:
            points = -1
            print(f"Maalesef bilemediniz. Doğru sayı {secret_number} idi. Kaybettiniz, puanınız: {points}")

        # Oyun skorunu toplam skora ekle
        total_score += points
        print(f"Bu oyundaki toplam puanınız: {points}")

    # 3 oyun tamamlandıktan sonra
    print("\nTüm oyunlar tamamlandı!")
    print(f"Toplam 3 oyundaki puanınız: {total_score}")

# Ana program döngüsü
while True:
    play_game()  # Oyunu başlat
    play_again = input("\nYeni bir oyuna başlamak için herhangi bir tuşa basın (Çıkmak için 'q' yazın): ")
    if play_again.lower() == 'q':
        print("Oyun sona erdi. Hoşça kal!")
        break