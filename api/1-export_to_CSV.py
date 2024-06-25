#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""

import csv
import requests
import sys


if __name__ == "__main__":
    # Get the user ID from the command-line arguments provided to the script
    user_id = sys.argv[1]
