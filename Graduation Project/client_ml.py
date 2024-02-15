import requests

if __name__ == '__main__':

    r = requests.post('http://localhost:5000/predict', json=['active', 'single family', 2, 'Philadelphia', 1000, 'PA', 1, 2019, 'central a/c, heat pump', 'central', 3])
    print(r.json()['prediction'])
