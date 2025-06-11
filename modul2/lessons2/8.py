import time
import random

print("Готовий? У тебе є 3 секунди, щоб натиснути Enter, як тільки з'явиться повідомлення!")
time.sleep(3)

# Затримка на випадковий час від 2 до 5 секунд
delay = random.uniform(2, 5)
time.sleep(delay)

print("Натискай Enter!")

# Вимірюємо час реакції
start_time = time.time()
input()  # Очікуємо на Enter від користувача
end_time = time.time()

reaction_time = end_time - start_time
print(f"Твій час реакції: {reaction_time:.3f} секунд")