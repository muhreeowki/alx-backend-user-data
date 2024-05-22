#!/usr/bin/env python3
"""
Definition of class Auth
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    Manages the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines whether a given path requires authentication or not
        Args:
            - path(str): Url path to be checked
            - excluded_paths(List of str): List of paths that do not require
              authentication
        Return:
            - True if path is not in excluded_paths, else False
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path in excluded_paths:
            return False
        for i in excluded_paths:
            if i.startswith(path) or path.startswith(i):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the authorization header from a request object
        """
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """
        Returns a User instance from information from a request object
        """
        return None
