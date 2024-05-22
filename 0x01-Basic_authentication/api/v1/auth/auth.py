#!/usr/bin/env python3
"""Auth module: Task 3"""

from flask import request


class Auth:
    """Class to manage the API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Return: False"""
        return False

    def authorization_header(self, request=None) -> str:
        """Return: None"""
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """Return: None"""
        return None
