
from aiogram import Dispatcher

from abc import ABC, abstractmethod

class Handler(ABC):
    """Interface for any storage saving weather"""
    @abstractmethod
    def regisetr_hendlers(self, dp: Dispatcher) -> None:
        """Реализация метода регистрации хендлера"""
        pass