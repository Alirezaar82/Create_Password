import random,string

def generate_password(len_password):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(len_password))
    return password

def rate_password(password):
    score = 0
    rate = [
        'Medium',
        'Strong',
        'Very Strong'
    ]

    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    if len(password) >= 12:
        score += 1

    rates = [
        'Very Weak',
        'Weak',
        'Medium',
        'Strong',
        'Very Strong',
    ]
    return rates[min(score, len(rates) - 1)]


def main():
    while True:
        len_password = int(input('Enter the length of the password: \npassword must be longer than 4 characters.'))
        if len_password >= 4:
            break

    password = generate_password(len_password)
    rate = rate_password(password)
    with open('password.txt','w',encoding='utf-8') as f:
        f.write(f'Generated Password: {password}\n')
        f.write(f'Password Strength: {rate}\n')


if __name__ == '__main__':
    main()
