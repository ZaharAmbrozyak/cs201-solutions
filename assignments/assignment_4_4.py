# Zahar Ambrozyak property

from random import choice


class RPS:
    """
    Клас RPS, батьківський клас інших класів
    """
    def __init__(self) -> None:
        """
        moves — список можливих ходів
        """
        self.moves = ['камінь', 'ножиці', 'папір']


class Player(RPS):
    """
    Клас Player
    Реалізує людського гравця.
    """
    def make_move(self) -> str:
        """
        make_move()
        Запитує у користувача хід:
        'камінь', 'ножиці', 'папір'

        Повертає введене значення.
        """
        print("Можливі ходи: " + ', '.join(self.moves))
        move = input('Введіть ваш хід: ')
        while move not in self.moves:
            print("Неправильний хід, спробуйте ще раз.")
            move = input('Введіть ваш хід: ')
        return move


class Bot(RPS):
    """
    Клас Bot
    Реалізує комп’ютерного супротивника.
    """
    def make_move(self) -> str:
        """
        make_move()
        Повертає випадковий вибір бота.
        """
        return choice(self.moves)


class FileLogger:
    """
    Клас FileLogger
    Відповідає лише за запис раундів у файл.
    """
    def __init__(self, filename: str = 'log.txt') -> None:
        """
        filename — ім’я файла, куди записуються результати
        """
        self.filename =  filename

    def write(self, result_dict: dict) -> None:
        """
        write(result_dict) - записує результат у файл
        Приймає словник формату:
        {'player': '...
         ', 'ai': '...
         ', 'win': '...'}

        Записує кожен результат раунду новим рядком у файл.
        Приклад рядка у файлі:
        {'player': 'камінь', 'ai': 'ножиці', 'win': 'player'}
        """
        with open(self.filename, 'a') as f:
            f.write(str(result_dict) + '\n')

    def leaderboard(self) -> str:
        """
        leaderboard() - читає файл та повертає
        кількість перемог для гравця та бота, а
        також загальну кількість ігор

        Приклад:
        '''
        Ігор: 102
        Переможці:
        Гравець - 44
        Бот - 40
        Нічия - 18
        '''
        """
        try:
            with open(self.filename, 'r') as f:
                data = f.readlines()
        except FileNotFoundError:
            print("Упс, помилка!")
            return 'FileNotFound'
        output = {
            'player': 0,
            'ai': 0,
            'draw': 0,
        }
        for line in data:
            game = eval(line)
            try:
                output[game['win']] += 1
            except KeyError as f:
                print('Неправильний ключ', f)

        text_output = f'''
Ігор: {sum(output.values())}
Переможці:
Гравець - {output['player']}
Бот - {output['ai']}  
Нічия - {output['draw']}
        '''
        return text_output.strip()


class Game(RPS):
    """
    Клас Game
    Основний клас, який організовує повний процес гри.
    """
    def __init__(self):
        """
        Поля:
        player — об’єкт Player
        bot — об’єкт Bot
        logger — об’єкт FileLogger
        moves — список ходів для перевірки правил
        """
        super().__init__()

        self.player = Player()
        self.bot = Bot()
        self.logger = FileLogger()

    def play_round(self):
        """
        Виконує один раунд гри:
        1. Отримує хід гравця:
            player_move = self.player.make_move()
        2. Отримує хід бота:
            ai_move = self.bot.make_move()
        3. Визначає переможця за правилами:
            камінь перемагає ножиці
            ножиці перемагають папір
            папір перемагає камінь
        4. Формує словник
        5. Записує результат у файл через
        6. Виводить підсумок раунду в консоль
        """
        player_move = self.player.make_move()
        ai_move = self.bot.make_move()
        print("Хід комп'ютера: " + ai_move)

        output = {
            'player': player_move,
            'ai': ai_move,
            'win': None
        }

        win_con = [('камінь', 'ножиці'),
                   ('ножиці', 'папір'),
                   ('папір', 'камінь')]

        for winner, looser in win_con:
            if winner == player_move and looser == ai_move:
                output['win'] = 'player'
                break
            elif winner == ai_move and looser == player_move:
                output['win'] = 'ai'
                break

        if output['win']:
            print(f"Переміг {output['win']}!")
        else:
            print("Нічия!")
            output['win'] = 'draw'

        self.logger.write(output)

    def result(self) -> None:
        """
        result()
        Повертає результат всіх ігор
        """
        print("Результати ігор:")
        print(self.logger.leaderboard())

    def run(self):
        """
        Запускає гру у циклі, доки користувач хоче грати далі:
        викликає play_round()
        після раунду запитує:
        'Зіграти ще раз? (y/n):'
        якщо n, завершує гру
        """
        game = 'y'
        while game != 'n':
            self.play_round()
            game = input('Зіграти ще раз? (y/n): ')
            while game not in ['y', 'n']:
                print("Неправильне значення, спробуйте ще раз.")
                game = input('Зіграти ще раз? (y/n): ')

my_game = Game()
my_game.run()
my_game.result()
