#!/usr/bin/env python3
"""Auth module: Task 3"""

from flask import request


class Auth:
    """Class to manage the API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Function that checks if auth is required
        Return:
            - False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Function that returns the auth header
            Return: None
        """
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """
        Function that returns the current user
            Return: None
        """
        return None
