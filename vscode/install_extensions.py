#!/usr/bin/env python3
"""Install VS Code extensions from extensions.json"""

import json
import subprocess
import sys
from pathlib import Path

def main():
    # Get the directory of this script
    script_dir = Path(__file__).parent
    extensions_file = script_dir / "extensions.json"
    
    if not extensions_file.exists():
        print(f"Error: {extensions_file} not found")
        sys.exit(1)
    
    # Read extensions from extensions.json
    with open(extensions_file) as f:
        data = json.load(f)
    
    extensions = data.get("extensions", [])
    
    if not extensions:
        print("No extensions found in extensions.json")
        return
    
    print(f"Installing {len(extensions)} extensions...")
    
    failed = []
    for ext in extensions:
        print(f"  Installing {ext}...", end=" ")
        try:
            subprocess.run(
                ["code", "--install-extension", ext],
                check=True,
                capture_output=True,
                text=True
            )
            print("✓")
        except subprocess.CalledProcessError as e:
            print("✗")
            failed.append(ext)
        except FileNotFoundError:
            print("\nError: 'code' command not found. Make sure VS Code is installed and in your PATH")
            sys.exit(1)
    
    if failed:
        print(f"\n{len(failed)} extension(s) failed to install:")
        for ext in failed:
            print(f"  - {ext}")
        sys.exit(1)
    
    print(f"\n✅ All {len(extensions)} extensions installed successfully!")

if __name__ == "__main__":
    main()
