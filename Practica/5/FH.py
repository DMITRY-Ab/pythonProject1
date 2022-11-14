from typing import Union


def translate_to_list(file_name: str) -> Union[list, str]:
    """
    Функция считывает числа с файла и возвращает их в виде списка
    :param file_name: имя файла
    :return: список чисел
    """
    try:
        file = open(file_name)
        count: int = int(file.readline())
        num_list: list = file.read().splitlines()

        if len(num_list) > count:
            raise Exception('Количество не совпадает')
        numbers_list = [int(num_list[i]) for i in range(0, count)]

        return num_list
    except FileNotFoundError:
        return 'Файл не найден. Проверьте правильность названия'
    except ValueError:
        return 'В файле не все элементы числа'
    except Exception as ex:
        return 'Ошибка обработки: ' + str(ex)
    finally:
        try:
            file.close()
        except Exception() as ex:
            print(ex)
            pass
