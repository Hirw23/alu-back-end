#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to JSON format.

This script takes an employee ID as a command-line argument and exports
the corresponding user information and to-do list to a JSON file.
"""

import json
import requests
import sys
