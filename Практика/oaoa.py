class Task:
    def __init__(self, task_id, name, priority, status="не выполнено"):
        if not isinstance(task_id, int):
            raise TypeError("ID задачи должен быть целым числом.")
        if not name or not isinstance(name, str):
            raise ValueError("Название задачи не может быть пустым и должно быть строкой.")
        if not isinstance(priority, int) or not (1 <= priority <= 5):
            raise ValueError("Приоритет должен быть целым числом от 1 до 5.")
        if status not in ["не выполнено", "выполнено"]:
            raise ValueError("Статус может быть только 'не выполнено' или 'выполнено'.")

        self.task_id = task_id
        self.name = name
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"[{self.task_id}] {self.name} | Приоритет: {self.priority} | Статус: {self.status}"

    def update_status(self, new_status):
        if new_status not in ["не выполнено", "выполнено"]:
            print("Неверный ввод статуса. Выбор из двух: 'выполнено' или 'не выполнено'.")
            return
        self.status = new_status
        print(f"Статус задачи [{self.task_id}] изменен на '{self.status}'.")


class taskscheduler:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self):
        print("\n~ Добавление новой задачи")
        name = input("Введите название задачи: ").strip()
        if not name:
            print("Название задачи не может быть пустым. Повторите ввод.")
            return

        while True:
            try:
                priority_str = input("Введите приоритет задачи (целое число от 1 до 5): ")
                priority = int(priority_str)
                if 1 <= priority <= 5:
                    break
                else:
                    print("Приоритет должен быть числом от 1 до 5.")
            except ValueError:
                print("Приоритет должен быть целым числом.")

        try:
            task = Task(self.next_id, name, priority)
            self.tasks.append(task)
            print(f"Задача \"{name}\" с ID {self.next_id} успешно добавлена.")
            self.next_id += 1
        except (TypeError, ValueError) as e:
            print(f"Ошибка при создании задачи: {e}")

    def _find_task_by_id(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def show_tasks(self, tasks_to_show=None, header="~ Список всех задач"):
        display_list = tasks_to_show if tasks_to_show is not None else self.tasks
        print(f"\n{header}")
        if not display_list:
            print("Список задач пуст.")
            return
        for task in display_list:
            print(task)

    def delete_task(self):
        print("\n~ Удаление задачи")
        if not self.tasks:
            print("Список задач пуст, удалять нечего.")
            return
        try:
            task_id_str = input("Введите ID задачи для удаления: ")
            task_id = int(task_id_str)
            task_to_delete = self._find_task_by_id(task_id)
            if task_to_delete:
                self.tasks.remove(task_to_delete)
                print(f"Задача с ID {task_id} \"{task_to_delete.name}\" успешно удалена.")
            else:
                print(f"Задача с ID {task_id} не найдена.")
        except ValueError:
            print("ID задачи должен быть целым числом.")

    def change_task_status(self):
        print("\n~ Изменение статуса задачи")
        if not self.tasks:
            print("Список задач пуст, для изменения статуса внесите хотя бы одну задачу.")
            return
        try:
            task_id_str = input("Введите ID задачи для изменения статуса: ")
            task_id = int(task_id_str)
            task = self._find_task_by_id(task_id)
            if task:
                print(f"Текущий статус задачи \"{task.name}\": {task.status}")
                while True:
                    new_status_choice = input("Выберите новый статус (1 - выполнено, 2 - не выполнено): ").strip()
                    if new_status_choice == '1':
                        task.update_status("выполнено")
                        break
                    elif new_status_choice == '2':
                        task.update_status("не выполнено")
                        break
                    else:
                        print("Неверный ввод. Пожалуйста, введите 1 или 2.")
            else:
                print(f"Задача с ID {task_id} не найдена.")
        except ValueError:
            print("ID задачи должен быть целым числом.")

    def filter_tasks_by_status(self):
        print("\n~ Фильтрация задач по статусу")
        if not self.tasks:
            print("Список задач пуст, нечего фильтровать.")
            return
        while True:
            status_choice = input("Показать задачи (1 - выполненные, 2 - не выполненные): ").strip()
            if status_choice == '1':
                status_filter = "выполнено"
                header = "~ Список выполненных задач"
                break
            elif status_choice == '2':
                status_filter = "не выполнено"
                header = "~ Список невыполненных задач"
                break
            else:
                print("Неверный ввод. Пожалуйста, введите 1 или 2.")

        filtered_tasks = [task for task in self.tasks if task.status == status_filter]
        if filtered_tasks:
            self.show_tasks(filtered_tasks, header=header)
        else:
            print(f"Задачи со статусом '{status_filter}' не найдены.")

    def sort_tasks_by_priority(self):
        if not self.tasks:
            print("\nСписок задач пуст, нечего сортировать.")
            return
        # Сортировка копии списка, чтобы не изменять исходный порядок для других операций
        sorted_tasks = sorted(self.tasks, key=lambda task: task.priority, reverse=True)
        self.show_tasks(sorted_tasks, header="--- Задачи, отсортированные по приоритету (по убыванию) ---")

def main_menu(manager):
    while True:
        print("\n+-------------------------------+")
        print("|    Спланируйте свой день ~    |")
        print("+-------------------------------+")
        print("| 1. Добавить новую задачу      |")
        print("| 2. Показать список всех задач |")
        print("| 3. Удалить задачу по ID       |")
        print("| 4. Изменить статус задачи     |")
        print("| 5. Показать выполненные/      |")
        print("|    невыполненные задачи       |")
        print("| 6. Сортировать по приоритету  |")
        print("| 0. Завершить работу           |")
        print("+-------------------------------+")

        choice = input("Выберите действие: ").strip()

        if choice == '1':
            manager.add_task()
        elif choice == '2':
            manager.show_tasks()
        elif choice == '3':
            manager.delete_task()
        elif choice == '4':
            manager.change_task_status()
        elif choice == '5':
            manager.filter_tasks_by_status()
        elif choice == '6':
            manager.sort_tasks_by_priority()
        elif choice == '0':
            print("Успешный выход из программы")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите существующий пункт меню.")
        input("\nНажмите Enter для продолжения...") # Пауза для удобства чтения

if __name__ == "__main__":
    task_scheduler = taskscheduler()
    main_menu(task_scheduler)