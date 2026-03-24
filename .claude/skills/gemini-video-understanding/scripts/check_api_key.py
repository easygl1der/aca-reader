#!/usr/bin/env python3
"""
Gemini Video Understanding - API Key Checker
"""

import os
import sys


def check_api_key():
    """Check if GEMINI_API_KEY is configured"""

    # Check in various locations
    locations = [
        ("Environment variable ($GEMINI_API_KEY)", os.environ.get('GEMINI_API_KEY')),
        (".env file in skill directory", None),
        (".env file in project root", None),
    ]

    api_key = os.environ.get('GEMINI_API_KEY')

    # Check skill directory .env
    skill_dir = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(skill_dir):
        with open(skill_dir) as f:
            for line in f:
                if line.startswith('GEMINI_API_KEY='):
                    api_key = line.split('=', 1)[1].strip()
                    locations[1] = (".env file in skill directory", api_key)
                    break

    # Check project root .env
    if not api_key:
        root_env = '.env'
        if os.path.exists(root_env):
            with open(root_env) as f:
                for line in f:
                    if line.startswith('GEMINI_API_KEY='):
                        api_key = line.split('=', 1)[1].strip()
                        locations[2] = (".env file in project root", api_key)
                        break

    print("=" * 50)
    print("GEMINI API Key Configuration Check")
    print("=" * 50)

    for name, value in locations:
        if value:
            masked = value[:8] + "..." + value[-4:] if len(value) > 12 else "***"
            print(f"✅ {name}: {masked}")
        else:
            print(f"❌ {name}: Not found")

    print("=" * 50)

    if api_key:
        if api_key.startswith('AIza'):
            print("✅ API Key format appears valid (starts with AIza)")
            return True
        else:
            print("⚠️  API Key format may be invalid (should start with AIza)")
            return True
    else:
        print("❌ No API Key found!")
        print("\nTo get an API key:")
        print("1. Go to https://aistudio.google.com/apikey")
        print("2. Create a new API key")
        print("3. Set it with: export GEMINI_API_KEY='your-key-here'")
        return False


if __name__ == '__main__':
    success = check_api_key()
    sys.exit(0 if success else 1)
