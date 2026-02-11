"""Base class for market definitions."""

from abc import ABC, abstractmethod


class Market(ABC):
    """Abstract base class representing a stock market."""

    name: str = "Market"

    @abstractmethod
    def format_ticker(self, code: str) -> str:
        """Convert a user-supplied code into a yfinance-compatible ticker symbol.

        Subclasses must implement this to add the appropriate exchange suffix.
        """

    @abstractmethod
    def get_default_symbols(self) -> list[str]:
        """Return a list of default ticker symbols (already formatted) for this market."""

    def get_thresholds(self) -> dict:
        """Return default thresholds for value-stock screening.

        Subclasses may override to customise per-market criteria.
        """
        return {
            "per_max": 15.0,
            "pbr_max": 1.0,
            "dividend_yield_min": 0.03,  # 3%
            "roe_min": 0.08,             # 8%
        }
