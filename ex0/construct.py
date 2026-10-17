import sys
import site
import os.path

def in_venv() -> bool:
	return sys.prefix != sys.base_prefix

def main() -> None:
	site_package = site.getsitepackages()[0]
	if not in_venv():
		print("LABORATORY STATUS: You are working in the open")
		print(f"Current Python: {sys.executable}")
		print("Virtual Environment: None detected")
		print(f"Global package path: {site_package}")
		print()
		print("WARNING: You are in the global environment!")
		print("Every reagent you install here leaks into the whole system.")
		print()
		print("To seal the laboratory, run:")
		print("python3 -m venv lab_env")
		print("source lab_env/bin/activate # On Unix")
		print("lab_env\\Scripts\\activate # On Windows")
		print()
		print("Then run this program again.")
	else:
		venv_name = os.path.basename(sys.prefix)
		print("LABORATORY STATUS: The laboratory is sealed")
		print(f"Current Python: {sys.executable}")
		print(f"Virtual Environment: {venv_name}")
		print(f"Environment Path: {sys.prefix}")
		print()
		print("SUCCESS: You are working in an isolated environment!")
		print("Safe to install reagents without affecting the global system.")
		print()
		print(f"Reagent installation path: {site_package}")

if __name__ == "__main__":
    main()
            



