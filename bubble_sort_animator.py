import pygame
import random
from copy import deepcopy

# Pygame başlatma
pygame.init()

# Ekran ayarları
WIDTH = 800
HEIGHT = 600
FPS = 60

# Renkler
BG_COLOR = (240, 240, 240)
BAR_COLOR = (65, 105, 225)
COMPARE_COLOR = (255, 69, 0)
SORTED_COLOR = (34, 139, 34)
TEXT_COLOR = (0, 0, 0)

# Ekran ve saat
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Sort Animasyonu - 800x600")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 24)

def bubble_sort_with_steps(dizi):
    """Bubble sort fonksiyonu - her adımdan sonra state döndürür"""
    N = len(dizi)
    dizi = deepcopy(dizi)
    steps = []
    steps.append((deepcopy(dizi), -1, -1, []))  # İlk state
    
    sorted_indices = []
    
    for i in range(N - 1):
        for j in range(N - i - 1):
            if dizi[j] > dizi[j + 1]:
                # Takas
                tmp = dizi[j]
                dizi[j] = dizi[j + 1]
                dizi[j + 1] = tmp
                steps.append((deepcopy(dizi), j, j + 1, deepcopy(sorted_indices)))
            else:
                steps.append((deepcopy(dizi), j, j + 1, deepcopy(sorted_indices)))
        
        sorted_indices.append(N - i - 1)
    
    sorted_indices.append(0)
    steps.append((dizi, -1, -1, sorted_indices))
    
    return steps

def draw_bars(dizi, comparing_indices, sorted_indices):
    """Bar grafik çiz"""
    screen.fill(BG_COLOR)
    
    n = len(dizi)
    bar_width = WIDTH // n
    max_height = HEIGHT - 100
    
    for i in range(n):
        # Bar yüksekliği hesapla (0-100 aralığında, max_height'a scale et)
        bar_height = (dizi[i] / 100) * max_height
        x = i * bar_width
        y = HEIGHT - bar_height - 30
        
        # Reng seç
        if i in comparing_indices:
            color = COMPARE_COLOR
        elif i in sorted_indices:
            color = SORTED_COLOR
        else:
            color = BAR_COLOR
        
        # Bar çiz
        pygame.draw.rect(screen, color, (x + 2, y, bar_width - 4, bar_height))
        
        # Border
        pygame.draw.rect(screen, TEXT_COLOR, (x + 2, y, bar_width - 4, bar_height), 1)
        
        # Değeri göster (sadece büyük değerleri göster, karışıklığı azaltmak için)
        if dizi[i] >= 90:
            text = font.render(str(dizi[i]), True, TEXT_COLOR)
            text_rect = text.get_rect(center=(x + bar_width // 2, HEIGHT - 15))
            screen.blit(text, text_rect)
    
    # Bilgi metni
    info_text = font.render(
        f"Mavi: Kırmızı: Karşılaştırılan  Yeşil: Sıralanmış  ESC: Çık",
        True,
        TEXT_COLOR
    )
    screen.blit(info_text, (10, 10))

def main():
    # Veriyi oluştur
    abc = [random.randrange(0, 100) for i in range(50)]
    
    # Sıralama adımlarını oluştur
    steps = bubble_sort_with_steps(abc)
    
    current_step = 0
    running = True
    paused = False
    step_delay = 0
    DELAY_FRAMES = 3  # Her adımda kaç frame bekle (hız kontrolü)
    
    print(f"Toplam adım sayısı: {len(steps)}")
    print("SPACE: Duraklat/Devam et, ESC: Çık, ← →: Adım geri/ileri")
    
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_LEFT:
                    current_step = max(0, current_step - 1)
                    step_delay = 0
                elif event.key == pygame.K_RIGHT:
                    current_step = min(len(steps) - 1, current_step + 1)
                    step_delay = 0
        
        # Otomatik ilerleme
        if not paused:
            step_delay += 1
            if step_delay >= DELAY_FRAMES:
                step_delay = 0
                if current_step < len(steps) - 1:
                    current_step += 1
        
        # Mevcut adımı al
        dizi, idx1, idx2, sorted_indices = steps[current_step]
        comparing = set()
        if idx1 >= 0:
            comparing.add(idx1)
        if idx2 >= 0:
            comparing.add(idx2)
        
        # Çiz
        draw_bars(dizi, comparing, sorted_indices)
        
        # Durum bilgisi
        status = "DURAKLATILDI" if paused else "ÇALIŞIYOR"
        status_text = font.render(
            f"Adım: {current_step + 1}/{len(steps)} | {status}",
            True,
            TEXT_COLOR
        )
        screen.blit(status_text, (10, HEIGHT - 25))
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
