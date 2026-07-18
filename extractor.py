import re
import os

def get_file_path():
    path = input("Enter the path of the incident report: ").strip()

    if path.startswith('"') and path.endswith('"'):
        path = path[1:-1]

    return path


def validate_file(path):
    if not os.path.isfile(path):
        raise FileNotFoundError(f"File not found: {path}")

    if not path.lower().endswith(".txt"):
        raise ValueError("Please select a .txt file.")

    if os.path.getsize(path) == 0:
        raise ValueError("The file is empty.")

    return path


def read_file(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as file:
        return file.read()


def extract_ips(text):
    pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    ips = re.findall(pattern, text)
    return sorted(set(ips))


def extract_emails(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(pattern, text)
    return sorted(set(emails))


def extract_urls(text):
    pattern = r"https?://[^\s\"'<>]+"
    urls = re.findall(pattern, text)
    return sorted(set(urls))


def print_section(title, items):
    print(f"\n{title}")
    print("-" * len(title))

    if len(items) == 0:
        print("None found.")
    else:
        for item in items:
            print(item)


def main():
    print("\n===== IOC EXTRACTOR =====")

    file_path = get_file_path()

    try:
        validate_file(file_path)
        data = read_file(file_path)

    except FileNotFoundError as e:
        print(f"\nError: {e}")
        return

    except ValueError as e:
        print(f"\nError: {e}")
        return

    except PermissionError:
        print("\nError: Permission denied.")
        return

    except OSError as e:
        print(f"\nError: {e}")
        return

    ip_addresses = extract_ips(data)
    email_addresses = extract_emails(data)
    url_addresses = extract_urls(data)

    print_section("IP Addresses", ip_addresses)
    print_section("Email Addresses", email_addresses)
    print_section("URLs", url_addresses)


if __name__ == "__main__":
    main()