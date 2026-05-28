"""Homework scaffold — sqlite lesson `l3_backup_and_vacuum` (Vibe Learn).

Задача: утилита обслуживания: hot_backup через Online Backup API (conn.backup), verify (integrity_check), compact (VACUUM).

Реализуй функции ниже — сигнатуры и тестовая поверхность фиксированы;
CI (.github/workflows/ci.yml) ставит зависимости и гоняет `pytest`.
Подробности и критерии приёмки — в README.md.

SQLite встроена в Python через stdlib `sqlite3` — никакого драйвера ставить
не нужно, сервера нет. БД это файл (DATABASE_PATH) или ":memory:" в тестах.
"""

import os
import sqlite3


def database_path() -> str:
    """Путь к файлу БД из env. Дефолт ":memory:" — БД живёт в процессе."""
    return os.environ.get("DATABASE_PATH", ":memory:")


def connect(path: str | None = None) -> sqlite3.Connection:
    """Открыть соединение sqlite3 (по умолчанию из database_path())."""
    return sqlite3.connect(path if path is not None else database_path())


# ----- TODO #1: hot_backup -----
def hot_backup(src_path: str, dst_path: str) -> str:
    """горячий бэкап через conn.backup — консистентен под параллельной записью; вернуть dst_path"""
    raise NotImplementedError("hot_backup: реализуй меня")


# ----- TODO #2: verify -----
def verify(path: str) -> bool:
    """PRAGMA integrity_check — вернуть True при 'ok'"""
    raise NotImplementedError("verify: реализуй меня")


# ----- TODO #3: compact -----
def compact(path: str) -> tuple[int, int]:
    """VACUUM; вернуть размер файла (до, после)"""
    raise NotImplementedError("compact: реализуй меня")



def main() -> None:
    """Точка входа: подключиться и напомнить, что реализовать.

    Замени тело на демонстрацию реализованных функций.
    """
    print("Vibe Learn — sqlite lesson scaffold up")
    print(f"DATABASE_PATH: {database_path()} (stdlib sqlite3, no server)")
    print("Реализуй TODO-функции, затем `pytest`. README.md содержит задачу.")


if __name__ == "__main__":
    main()
