# generate auth token for enphase inverter api access
def generate_token() -> str:
    print('generating token')


# test token generator
if __name__ == "__main__":
    print('generating test token')
    token = generate_token()
    print(f'token: {token}')
