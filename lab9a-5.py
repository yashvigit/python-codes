faculty = ['Dr. Sharma', 'Prof. Radhakrishnan', 'Ms. Patel', 'Dr. Suresh', 'Professor Mehta']
long_names = list(filter(lambda name: len(name) > 8, faculty))

print("Names longer than 8 characters:")
for name in long_names:
    print(name)