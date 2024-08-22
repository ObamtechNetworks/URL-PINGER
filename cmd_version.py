import requests

def ping_urls(urls):
    results = {}
    for url in urls:
        try:
            response = requests.get(url.strip(), timeout=5)
            if response.status_code == 200:
                results[url] = "OK"
            else:
                results[url] = f"Failed with status code: {response.status_code}"
        except requests.exceptions.RequestException as e:
            results[url] = f"Error: {str(e)}"
    return results

# Continuous loop to input URLs
while True:
    # Accept user input with ; separated URLs
    urls_input = input("Enter a list of URLs separated by ';' (or type 'exit' to quit): ")
    
    # Exit condition
    if urls_input.lower() == 'exit':
        print("Exiting the program.")
        break
    
    # Split the input based on ';'
    urls = urls_input.split(';')

    # Ping the URLs
    results = ping_urls(urls)

    # Display the results in the desired format
    for url, result in results.items():
        print(f"{url}: {result}")

