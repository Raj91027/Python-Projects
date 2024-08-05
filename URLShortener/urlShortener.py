import random
import zipfile

def generate_test_cases(num_cases, filename):
    with open(filename, 'w') as f:
        for _ in range(num_cases):
            N = random.randint(1, 10**5)
            arr = [random.randint(1, 10**6) for _ in range(N)]
            f.write(str(N) + '\n')
            f.write(' '.join(map(str, arr)) + '\n')

def create_zip_archive(zip_filename, text_filename):
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        zipf.write(text_filename)

if __name__ == "__main__":
    num_test_cases = 5
    test_cases_filename = "test_cases.txt"
    zip_filename = "test_cases.zip"

    generate_test_cases(num_test_cases, test_cases_filename)
    create_zip_archive(zip_filename, test_cases_filename)

    print(f"Test cases generated and saved in {zip_filename}")
