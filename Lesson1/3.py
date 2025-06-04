def quiz_game():
    print("Вітаємо у грі-вікторині!")
    print("Відповідайте на запитання з різних категорій.")
    print("------------------------------------------------\n")

    score = 0
    total_questions = 0

    questions = [
        {
            "question": "Яка столиця України?",
            "answer": "київ"
        },
        {
            "question": "Скільки буде 5 + 7?",
            "answer": "12"
        },
        {
            "question": "Яка планета найбільша у Сонячній системі?",
            "answer": "юпітер"
        },
        {
            "question": "Хто написав 'Кобзар'?",
            "answer": "шевченко"
        },
        {
            "question": "У якому році була проголошена незалежність України?\nA) 1989\nB) 1991\nC) 1994",
            "answer": "b"
        },
        {
            "question": "скільки кілограмів в тонні?",
            "answer": "1000"
        },
        {
            "question": "Скільки в кілограмі грамів?",
            "answer": "1000"
        },
        {
            "question": "Яке найбільше море в світі?",
            "answer": "філіппінське"
        },
        {
            "question": "Скільки лап у павука?",
            "answer": "8"
        },
        {
            "question": "Який знак зодіаку йде після Лева?\nA) Діва\nB) Терези\nC) Рак",
            "answer": "a"
        }
    ]

    for q in questions:
        print("\n" + q["question"])
        user_answer = input("Ваша відповідь: ").strip().lower()
        total_questions += 1

        if user_answer == q["answer"]:
            print("✅ Правильно! Молодець!")
            score += 1
        else:
            print(f"❌ Неправильно. Правильна відповідь: {q['answer'].capitalize()}")

    print("\n🎉 Гру завершено!")
    print(f"Ви відповіли правильно на {score} з {total_questions} питань.")

# Запуск гри
quiz_game()
