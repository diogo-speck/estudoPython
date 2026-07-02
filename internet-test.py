# Speedtest com Python
import speedtest

st = speedtest.Speedtest()

print("Procurando servidor...")
st.get_best_server()

print("Testando download...")
download = st.download() / 1_000_000  # Mbps

print("Testando upload...")
upload = st.upload() / 1_000_000  # Mbps

ping = st.results.ping

print(f"Download: {download:.2f} Mbps")
print(f"Upload: {upload:.2f} Mbps")
print(f"Ping: {ping:.2f} ms")