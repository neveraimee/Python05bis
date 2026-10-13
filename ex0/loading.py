import sys


def check_reagents(name: str) -> str | None:
	try:
		module = __import__(name)
		return getattr(module, "__version__", "unknown")
	except ImportError:
		return None

def main() -> None:
	print("REAGENT STATUS: Loading reagents...\n")
	print("Checking dependencies:")
	
	pandas_version = check_reagant("pandas")
	numpy_version = check_reagant("numpy")

	missing = False

	if pandas_version:
		print(f"[OK] pandas {pandas_version} - Data manipulation ready")
	else:
		print("[KO] pandas - Data manipulation not installed")
		missing = True
	
	if numpy_version:
		print(f"[OK] numpy {numpy_version} - Numerical computation ready")
	else:
		print("[KO] numpy - Numerical computation not ready")
		missing = True

	print("pip vs Poetry:")
	print("requirements.txt declares what"
	"to install; pip resolves it at install time."
	"pyproject.toml declares the same constraints,"
	"and Poetry pins the resolved versions in poetry."
	"lock so every install is identical.")

	print("All reagents present and accounted for.")

#research getattr buildin