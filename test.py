# Try to open and read the content of the renamed file
with open('requirements.txt', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()


cleaned = ''.join(content.split())

print(cleaned)

with open('requirements_cleaned.txt', 'w', encoding='utf-8', errors='ignore') as file:
    file.write(cleaned)

print("Done")