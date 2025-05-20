"""Placeholder utilities for Notion API integration.

This module defines a small client skeleton that will later communicate with the
Notion API. Network operations are not implemented in this offline environment.
"""

import json
from typing import Any, Dict


class NotionClient:
    def __init__(self, token: str, database_id: str) -> None:
        self.token = token
        self.database_id = database_id

    def create_page(self, data: Dict[str, Any]) -> None:
        """Create a page in the configured database.

        Raises:
            NotImplementedError: Always, since the API call is not implemented.
        """
        raise NotImplementedError("Notion API integration is not implemented yet")
