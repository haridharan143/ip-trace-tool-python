import requests

def get_ipinfo(ip):
    try:
        r = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
        if r.status_code == 200:
            data = r.json()
            return {
                "ip": data.get("ip"),
                "city": data.get("city"),
                "region": data.get("region"),
                "country": data.get("country"),
                "loc": data.get("loc"),
                "org": data.get("org"),
                "source": "ipinfo.io"
            }
    except:
        pass
    return {}

def get_ipapi(ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        if r.status_code == 200:
            data = r.json()
            return {
                "ip": data.get("query"),
                "city": data.get("city"),
                "region": data.get("regionName"),
                "country": data.get("country"),
                "loc": f"{data.get('lat')},{data.get('lon')}",
                "org": data.get("org"),
                "source": "ip-api.com"
            }
    except:
        pass
    return {}

def get_ipwhois(ip):
    try:
        r = requests.get(f"https://ipwhois.app/json/{ip}", timeout=5)
        if r.status_code == 200:
            data = r.json()
            return {
                "ip": data.get("ip"),
                "city": data.get("city"),
                "region": data.get("region"),
                "country": data.get("country"),
                "loc": f"{data.get('latitude')},{data.get('longitude')}",
                "org": data.get("org"),
                "source": "ipwhois.app"
            }
    except:
        pass
    return {}

def trace_ip(ip):
    print("\n🔍 Tracing IP, please wait...")

    # Try each source
    result = get_ipinfo(ip)
    if not result:
        result = get_ipapi(ip)
    if not result:
        result = get_ipwhois(ip)

    if result:
        print(f"\n📊 IP Trace Report (via {result['source']})")
        print("---------------------------------------")
        print(f"IP Address: {result.get('ip')}")
        print(f"City: {result.get('city')}")
        print(f"Region: {result.get('region')}")
        print(f"Country: {result.get('country')}")
        print(f"Location (lat,lon): {result.get('loc')}")
        print(f"Organization: {result.get('org')}")
        if result.get("loc"):
            print(f"Google Maps: https://www.google.com/maps/search/?api=1&query={result.get('loc')}")
    else:
        print("❌ Could not retrieve IP details from any source.")

if __name__ == "__main__":
    ip_input = input("📝 Enter the IP address to trace: ")
    trace_ip(ip_input)
