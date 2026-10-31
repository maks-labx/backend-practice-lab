class SimpleManager:
    def __enter__(self):
        print("Вход в контекст.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            print("Работа завершена успешно")
        else:
            print("Произошла ошибка")

with SimpleManager() as manager:
    print("Первая операция")

print("---")

with SimpleManager() as manager:
    print("Вторая операция")
    raise ValueError("Тестовая ошибка")

