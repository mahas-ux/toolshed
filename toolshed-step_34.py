# === Stage 34: Add support for multiple local user profiles ===
# Project: ToolShed
import json
import os
from pathlib import Path


def get_user_profiles_dir() -> Path:
    """Return the directory where user profile JSON files are stored."""
    return Path(__file__).parent / "profiles"


def load_user_profile(profile_name: str) -> dict:
    """Load a single user profile by name.

    Args:
        profile_name: The name of the profile (e.g. 'alice', 'bob').

    Returns:
        A dict with keys: name, email, role, tools, loans, maintenance_log.

    Raises:
        FileNotFoundError: If the profile file does not exist.
    """
    profiles_dir = get_user_profiles_dir()
    profile_file = profiles_dir / f"{profile_name}.json"
    if not profile_file.exists():
        raise FileNotFoundError(f"Profile '{profile_name}' not found at {profile_file}")
    with open(profile_file, "r") as f:
        return json.load(f)


def save_user_profile(profile_name: str, profile_data: dict) -> None:
    """Save a user profile to disk.

    Args:
        profile_name: The name of the profile (e.g. 'alice', 'bob').
        profile_data: The profile dict to save.
    """
    profiles_dir = get_user_profiles_dir()
    profiles_dir.mkdir(parents=True, exist_ok=True)
    profile_file = profiles_dir / f"{profile_name}.json"
    with open(profile_file, "w") as f:
        json.dump(profile_data, f, indent=2)
