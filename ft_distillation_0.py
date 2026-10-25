import alchemy


def main() -> None:
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(f"Testing strength_potion: {alchemy.strength_potion()}")
    print(f"Testing healing_potion: {alchemy.healing_potion()}")


if __name__ == "__main__":
    main()